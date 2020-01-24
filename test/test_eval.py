import sys
import os
sys.path.append(os.path.abspath('src'))
import pytest
from src.lexer import Lexer
from src.parser import parse
from src.evaluator import evaluate
from src.environment import defaultenv
from src.presenter import present

@pytest.mark.parametrize("expression,expected", [
    ("(+ (+ 1 1) (+ 1 (+ 1 1)))", "5"), # simple nested expression
    ("(car '(1 2 3 4))", "1"),
    ("(cdr '(1 2 3 4))", "(2, 3, 4)"),
    ("(nth 3 '(1 2 3 4))", "3"),
    ("(car (cdr '(1 2 3 4)))", "2")
])
def test_simple_addition(expression, expected):
    env = defaultenv()
    lexer = Lexer(expression)
    parsetree = parse(lexer)
    actual = present(evaluate(parsetree, env))
    assert expected == actual

if __name__ == '__main__':
    pytest.main()