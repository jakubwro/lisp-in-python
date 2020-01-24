from lexer import Lexer
from parser import parse
from prompter import displayprompt, readexpression, displayerror, welcome, bye
from presenter import present
from lisptypes import LispException
from environment import defaultenv
from evaluator import evaluate

def read():
    
    return parse(Lexer(readexpression()))

def eval(ast, env):
    return evaluate(ast, env)

def print(str):
    present(str)

def loop():
    welcome()
    displayprompt()
    env = defaultenv()
    while True:
        try:
            print(evaluate(read(), env))
        except LispException as e:
            displayerror(str(e))
        except (KeyboardInterrupt, EOFError):
            bye()
            return
        # except BaseException as e:
        #     displayerror(str(type(e)))
loop()
