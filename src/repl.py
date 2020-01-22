from parser import parse
from prompter import displayprompt, readexpression
from presenter import present

def read():
    line = readexpression()
    ast = parse(line)
    return ast

def eval(ast):
    return str(ast)

def print(str):
    present(str)

def loop():
    displayprompt()
    while True:
        print(eval(read()))

loop()
