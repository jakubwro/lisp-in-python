from lisptypes import LispException

class Environment():
    def __init__(self, outer):
        self.outer = outer
        self.data = {}

    def set(self, key, value):
        self.data[key] = value

    def has(self, key):
        return key in self.data or (self.outer and self.outer.has(key))
        
    def get(self, key):
        if key in self.data:
            return self.data[key]
        if self.outer and self.outer.has(key):
            return self.outer.get(key)
        raise LispException(f"Symbol '{key}'' is not defined!")

def defaultenv():
    env = Environment(None)
    env.set('+', lambda a,b: a+b)
    env.set('-', lambda a,b: a-b)
    env.set('*', lambda a,b: a*b)
    env.set('/', lambda a,b: int(a/b))
    return env
