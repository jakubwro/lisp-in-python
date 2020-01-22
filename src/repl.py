from parser import parse
from prompter import displayprompt, readexpression
from presenter import present
from lisptypes import Symbol

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
    displayprompt()
    while True:
        print(eval(read(), environment))

loop()
