from specialforms import isspecial, specialform
from lisptypes import Symbol, LispException

def evaluateast(ast, env):
    if isinstance(ast, Symbol):
        return env.get(ast)
    if isinstance(ast, list):
        return list(map(lambda x: evaluate(x, env), ast))
    return ast

def evaluate(ast, env):
    if not isinstance(ast, list):
        return evaluateast(ast, env)
    if not ast: # empty list
        return []

    form = ast[0]
    if isspecial(form):
        return specialform(form, ast, env, evaluate)
        
    evaluated = evaluateast(ast, env)
    func, args = evaluated[0], evaluated[1:]
    if not callable(func):
        raise(LispException(f"{func} is not callable. Are you missing a quotation?"))
    return func(*args)