from parser import parse
from prompter import displayprompt, readexpression, displayerror, welcome, bye
from presenter import present
from lisptypes import Symbol, LispException
from environment import defaultenv, Environment

def read():
    return parse(readexpression())

def eval_ast(ast, env):
    if isinstance(ast, Symbol):
        return env.get(ast)
    if isinstance(ast, list):
        return list(map(lambda x: eval(x, env), ast))
    return ast

def eval(ast, env):
    if not isinstance(ast, list):
        return eval_ast(ast, env)
    if not ast: # empty list
        return []
    if ast[0] == 'car':
        return ast[1][0]
    if ast[0] == 'cdr':
        return ast[1][1:]
    if ast[0] == 'nth':
        return ast[2][ast[1]]
    if ast[0] == 'cons':
        return [ast[1], *ast[2]] #TODO
    if ast[0] == 'quote':
        if len(ast) != 2:
            raise(LispException("'quote' special form requires 1 argument"))
        return ast[1]
    if ast[0] == 'def!':
        if len(ast) != 3:
            raise(LispException("'def!' special form requires 2 arguments"))
        return env.set(ast[1], eval(ast[2], env))
    if ast[0] == 'let*':
        if len(ast) != 3:
            raise(LispException("'let*' special form requires 2 arguments"))
        letenv = Environment(env)
        t = ast[1]
        for i in range(0, len(ast[1]), 2):
            letenv.set(t[i], eval(t[i+1], letenv))
        return eval(ast[2], letenv)
    evaluated = eval_ast(ast, env)
    func, args = evaluated[0], evaluated[1:]
    if not callable(func):
        raise(LispException(f"{func} is not callable. Are you missing a quotation?"))
    return func(*args)

def print(str):
    present(str)

def loop():
    welcome()
    displayprompt()
    env = defaultenv()
    while True:
        try:
            print(eval(read(), env))
        except LispException as e:
            displayerror(str(e))
        except (KeyboardInterrupt, EOFError):
            bye()
            return
        except BaseException as e:
            displayerror(str(type(e)))
loop()
