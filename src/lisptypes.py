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
