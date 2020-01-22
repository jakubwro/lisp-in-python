from parser import parse
from prompter import displayprompt, readexpression, displayerror, welcome, bye
from presenter import present
from lisptypes import Symbol, Keyword, LispException

def read():
    line = readexpression()
    ast = parse(line)
    return ast

def eval_ast(ast, env):
    if isinstance(ast, Symbol):
        return env[ast]
    if isinstance(ast, list):
        return list(map(lambda x: eval(x, env), ast))
    return ast

def eval(ast, env):
    if not isinstance(ast, list):
        return eval_ast(ast, env)
    if not ast: # empty list
        return []
    evaluated = eval_ast(ast, env)
    func, args = evaluated[0], evaluated[1:]
    if not callable(func):
        raise(LispException(f"{func} is not callable. Are you missing quotation?"))
    return func(*args)

def print(str):
    present(str)

environment = {
    '+': lambda a,b: a+b,
    '-': lambda a,b: a-b,
    '*': lambda a,b: a*b,
    '/': lambda a,b: int(a/b)
}

def loop():
    welcome()
    displayprompt()
    while True:
        try:
            print(eval(read(), environment))
        except LispException as e:
            displayerror(str(e))
        except KeyboardInterrupt:
            bye()
            return
        except BaseException as e:
            displayerror(str(type(e)))
loop()
