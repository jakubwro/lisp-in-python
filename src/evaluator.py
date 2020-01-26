from lisptypes import Symbol, LispException
from environment import Environment

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

    if callable(form):
        return form(ast[1:])

    if isspecial(form):
        return specialform(form, ast, env)
        
    evaluated = evaluateast(ast, env)
    func, args = evaluated[0], evaluated[1:]
    if not callable(func):
        raise(LispException(f"{func} is not callable. Are you missing a quotation?"))
    return func(*args)

def car(ast, env): #TODO: move car, cdr, nth and cons to default env
    return evaluate(ast[1], env)[0]

def cdr(ast, env):
    return evaluate(ast[1], env)[1:]

def nth(ast, env):
    if not isinstance(ast[1], int):
        raise LispException("'nth' expects' numeric index")
    return evaluate(ast[2], env)[ast[1]-1]
    
def cons(ast, env):
    return [ast[1], *ast[2]]

def quote(ast, env):
    if len(ast) != 2:
        raise(LispException("'quote' special form requires 1 argument"))
    return ast[1]

def _def(ast, env):
    if len(ast) != 3:
        raise(LispException("'def!' special form requires 2 arguments"))
    return env.set(ast[1], evaluate(ast[2], env))

def _let(ast, env):
    if len(ast) != 3:
        raise(LispException("'let*' special form requires 2 arguments"))
    letenv = Environment(env)
    t = ast[1]
    for i in range(0, len(ast[1]), 2):
        letenv.set(t[i], evaluate(t[i+1], letenv))
    return evaluate(ast[2], letenv)

def _if(ast, env):
    if len(ast) < 3:
        raise(LispException("'if' special form requires at least 2 arguments"))
    cond = evaluate(ast[1], env)
    if cond is None or cond is False:
        if len(ast) > 3:
            return evaluate(ast[3], env)
        return None
    return evaluate(ast[2], env)

def _fn(ast, env):
    if len(ast) != 3:
        raise(LispException("'fn*' special form requires 2 arguments"))
    binds = ast[1]
    return lambda *a: evaluate(ast[2], Environment(env, binds, a))


def _do(ast, env):
    result = None
    for expr in ast[1:]:
        result = evaluate(expr, env)
    return result

specials = {
    "car": car,
    "cdr": cdr,
    "nth": nth,
    "cons": cons,
    "quote": quote,
    "def!": _def,
    "let*": _let,
    "if": _if,
    "fn*": _fn,
    "do": _do
}

def isspecial(form):
    if isinstance(form, list):
        return False
    return form in specials

def specialform(form, ast, env):
    f = specials[form]
    return f(ast, env)