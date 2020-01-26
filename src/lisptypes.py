class Symbol(str): pass

class LispException(BaseException): pass

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

class Fn():
    def __init__(self, body, binds, env, evaluate):
        self.body = body
        self.binds = binds
        self.env = env
        self.evaluate = evaluate
    
    def newenv(self, a):
        return Environment(self.env, self.binds, a)

    def call(self, a):
        return self.evaluate(self.body, self.newenv(a))

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
    env.set('car', lambda l: l[0])
    env.set('cdr', lambda l: l[1:])
    env.set('cons', lambda item, l: [item, *l])
    env.set('nth', lambda pos, l: l[pos-1])

    env.set('=', lambda a,b: a == b)
    env.set('>', lambda a,b: a > b)
    env.set('<', lambda a,b: a < b)
    env.set('>=', lambda a,b: a >= b)
    env.set('<=', lambda a,b: a <= b)

    env.set('not', lambda a: False if a is 0 else not a)

    env.set('prn', lambda v: print(v))

    

    return env