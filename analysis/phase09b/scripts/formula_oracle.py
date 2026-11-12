"""Restricted formula-intent oracle, independent of LibreOffice caches.
It supports only the seven functions present in this workbook and is NOT an Excel engine.
"""
import openpyxl, statistics, math, re
from decimal import Decimal, ROUND_HALF_UP
from openpyxl.formula.tokenizer import Tokenizer
from openpyxl.utils.cell import range_boundaries

class Parse:

    def __init__(self, t):
        self.t = [x for x in Tokenizer('=' + t.lstrip('=')).items if x.type != 'WHITE-SPACE']
        self.i = 0

    def expression(self, p=0):
        t = self.t[self.i]
        self.i += 1
        if t.type == 'FUNC' and t.subtype == 'OPEN':
            args = []
            if not (self.t[self.i].type == 'FUNC' and self.t[self.i].subtype == 'CLOSE'):
                while True:
                    args.append(self.expression())
                    if self.t[self.i].type == 'SEP':
                        self.i += 1
                        continue
                    break
            assert self.t[self.i].subtype == 'CLOSE'
            self.i += 1
            n = ('fn', t.value[:-1].upper(), args)
        elif t.type == 'PAREN' and t.subtype == 'OPEN':
            n = self.expression()
            assert self.t[self.i].subtype == 'CLOSE'
            self.i += 1
        elif t.type == 'OPERATOR-PREFIX':
            n = ('unary', t.value, self.expression(6))
        elif t.subtype == 'RANGE':
            n = ('ref', t.value)
        elif t.subtype == 'TEXT':
            n = ('val', t.value[1:-1].replace('""', '"'))
        elif t.subtype == 'NUMBER':
            n = ('val', float(t.value))
        elif t.subtype == 'LOGICAL':
            n = ('val', t.value == 'TRUE')
        else:
            raise ValueError(('token', t.value, t.type, t.subtype))
        bp = {'=': 1, '<>': 1, '>': 1, '<': 1, '>=': 1, '<=': 1, '&': 2, '+': 3, '-': 3, '*': 4, '/': 4, '^': 5}
        while self.i < len(self.t) and self.t[self.i].type == 'OPERATOR-INFIX' and (bp[self.t[self.i].value] > p):
            op = self.t[self.i].value
            self.i += 1
            n = ('op', op, n, self.expression(bp[op] - int(op == '^')))
        return n

    def all(self):
        n = self.expression()
        assert self.i == len(self.t), (self.i, len(self.t))
        return n

def refparts(r, s):
    if '!' in r:
        s, r = r.rsplit('!', 1)
        s = s.strip("'").replace("''", "'")
    return (s, r.replace('$', ''))

def evaluate_all(path, excluded='18_内部一致性检查'):
    w = openpyxl.load_workbook(path, data_only=False)
    trees = {}
    for sheet in w:
        if sheet.title == excluded:
            continue
        for row in sheet:
            for c in row:
                if c.data_type == 'f':
                    trees[sheet.title, c.coordinate] = Parse(c.value).all()
    memo = {}
    active = set()

    def flatten(v):
        if isinstance(v, list):
            for x in v:
                yield from flatten(x)
        else:
            yield v

    def num(v):
        if v in (None, ''):
            return 0
        if isinstance(v, (float, int)):
            return v
        raise ValueError('not numeric ' + str(v))

    def cell(s, a):
        k = (s, a)
        if k in memo:
            return memo[k]
        if k in active:
            raise ValueError('cycle ' + str(k))
        active.add(k)
        c = w[s][a]
        r = ev(trees[k], s) if c.data_type == 'f' else c.value
        r = 0 if c.data_type == 'f' and trees[k][0] == 'ref' and (r is None) else r
        active.remove(k)
        memo[k] = r
        return r

    def ev(n, s):
        t = n[0]
        if t == 'val':
            return n[1]
        if t == 'ref':
            ss, rr = refparts(n[1], s)
            if ':' not in rr:
                return cell(ss, rr)
            return [cell(ss, c.coordinate) for row in w[ss][rr] for c in row]
        if t == 'unary':
            return num(ev(n[2], s)) * (-1 if n[1] == '-' else 1)
        if t == 'op':
            op = n[1]
            a = ev(n[2], s)
            b = ev(n[3], s)
            if op in ['=', '<>']:
                r = ('' if a is None else a) == ('' if b is None else b)
                return r if op == '=' else not r
            if op == '&':
                return str(a) + str(b)
            a = num(a)
            b = num(b)
            if op == '+':
                return a + b
            if op == '-':
                return a - b
            if op == '*':
                return a * b
            if op == '/':
                return a / b
            if op == '^':
                return a ** b
            if op == '>':
                return a > b
            if op == '<':
                return a < b
            if op == '>=':
                return a >= b
            if op == '<=':
                return a <= b
        if t == 'fn':
            fn, args = n[1:]
            if fn == 'IF':
                return ev(args[1] if ev(args[0], s) else args[2], s)
            vv = [ev(a, s) for a in args]
            if fn == 'OR':
                return any(flatten(vv))
            if fn == 'ROUND':
                return float(Decimal(str(vv[0])).quantize(Decimal(1).scaleb(-int(vv[1])), rounding=ROUND_HALF_UP))
            vv = [x for x in flatten(vv) if isinstance(x, (float, int)) and (not isinstance(x, bool))]
            if fn == 'COUNT':
                return len(vv)
            if fn == 'SUM':
                return sum(vv)
            if fn == 'AVERAGE':
                return statistics.mean(vv)
            if fn == 'STDEV':
                return statistics.stdev(vv)
        raise ValueError(n)
    result = {k: cell(*k) for k in trees}
    w.close()
    return result
