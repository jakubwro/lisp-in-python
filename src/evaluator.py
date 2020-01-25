from specialforms import isspecial, specialform
from lisptypes import Symbol, LispException

def expandquotes(ast):
    expanded = []
    quotemode = False
    for node in ast:
        if node == "'":
            quotemode = True
            continue
        if not quotemode:
            expanded.append(node)
        else:
            expanded.append(['quote', node])
        quotemode = False
    if quotemode == True:
        raise LispException("Unexpected closed paren!")
    return expanded

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

    ast = expandquotes(ast)

    form = ast[0]
    if isspecial(form):
        return specialform(form, ast, env, evaluate)
        
    evaluated = evaluateast(ast, env)
    func, args = evaluated[0], evaluated[1:]
    if not callable(func):
        raise(LispException(f"{func} is not callable. Are you missing a quotation?"))
    return func(*args)