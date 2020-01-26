import sys
import os
sys.path.append(os.path.abspath('src'))
from src.lexer import Lexer
from src.parser import parse
from src.evaluator import evaluate, defaultenv
from src.presenter import present
from src.lisptypes import LispException

def execute(expr, env = None):
    if env == None:
        env = defaultenv()
    lexer = Lexer(expr)
    parsetree = parse(lexer)
    try:
        result = present(evaluate(parsetree, env))
        return result
    except BaseException as exc:
        return str(exc)

class Interpreter():
    def __init__(self):
        self.env = defaultenv()

    def run(self, expr):
        return execute(expr, self.env)