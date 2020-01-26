from lisptypes import LispException

class Environment():
    def __init__(self, outer, binds=[], exprs=[]):
        self.outer = outer
        self.data = {}
        for k,v in zip(binds, exprs):
            self.data[k] = v

    def set(self, key, value):
        self.data[key] = value
        return self.data[key]

    def has(self, key):
        return key in self.data or (self.outer and self.outer.has(key))
        
    def get(self, key):
        if key in self.data:
            return self.data[key]
        if self.outer and self.outer.has(key):
            return self.outer.get(key)
        raise LispException(f"Symbol '{key}' is not defined!")

def defaultenv():
    env = Environment(None)
    env.set('+', lambda a,b: a+b)
    env.set('-', lambda a,b: a-b)
    env.set('*', lambda a,b: a*b)
    env.set('/', lambda a,b: int(a/b))

    env.set('list', lambda *a: [*a])
    env.set('list?', lambda l: isinstance(l, list))
    env.set('empty?', lambda l: l is None or len(l) == 0)
    env.set('count', lambda l: 0 if l == None else len(l))

    env.set('=', lambda a,b: a == b)
    env.set('>', lambda a,b: a > b)
    env.set('<', lambda a,b: a < b)
    env.set('>=', lambda a,b: a >= b)
    env.set('<=', lambda a,b: a <= b)

    env.set('prn', lambda v: print(v))
    return env
