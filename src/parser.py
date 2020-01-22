from re import compile, match
from lexer import Lexer
from lisptypes import Symbol

integer_regex = compile(r"-?[0-9]+$")

def parseform(lexer):
    if lexer.peek() == None:
        return None
    if lexer.peek() == "(":
        return parselist(lexer)
    else:
        return parseatom(lexer)

def parselist(lexer):
    ast = list()
    token = lexer.next()
    assert(token == "(")
    token = lexer.peek()
    while token != ")":
        assert(token != None) #todo
        ast.append(parseform(lexer))
        token = lexer.peek()
    lexer.next()
    return ast

def parseatom(lexer):
    token = lexer.next()
    if match(integer_regex, token):
        return int(token)
    elif token == "nil":
        return None
    elif token == "true":
        return True
    elif token == "false":
        return False

    return Symbol(token)

def parse(str):
    lexer = Lexer(str)
    ast = parseform(lexer)
    return ast
