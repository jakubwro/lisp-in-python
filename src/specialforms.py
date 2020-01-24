from lisptypes import LispException
from environment import Environment

def car(ast, env, evaluate):
    return evaluate(ast[1], env)[0]

def cdr(ast, env, evaluate):
    return evaluate(ast[1], env)[1:]

def nth(ast, env, evaluate):
    if not isinstance(ast[1], int):
        raise LispException("'nth' expects' numeric index")
    return evaluate(ast[2], env)[ast[1]-1]
    
def cons(ast, env, evaluate):
    return [ast[1], *ast[2]]

def quote(ast, env, evaluate):
    if len(ast) != 2:
        raise(LispException("'quote' special form requires 1 argument"))
    return ast[1]

def sf_def(ast, env, evaluate):
    if len(ast) != 3:
        raise(LispException("'def!' special form requires 2 arguments"))
    return env.set(ast[1], evaluate(ast[2], env))

def sf_let(ast, env, evaluate):
    if len(ast) != 3:
        raise(LispException("'let*' special form requires 2 arguments"))
    letenv = Environment(env)
    t = ast[1]
    for i in range(0, len(ast[1]), 2):
        letenv.set(t[i], evaluate(t[i+1], letenv))
    return evaluate(ast[2], letenv)

specials = {
    "car": car,
    "cdr": cdr,
    "nth": nth,
    "cons": cons,
    "quote": quote,
    "def!": sf_def,
    "let*": sf_let
}

def isspecial(form):
    if isinstance(form, list):
        return False
    return form in specials

def specialform(form, ast, env, evaluate):
    f = specials[form]
    return f(ast, env, evaluate)
