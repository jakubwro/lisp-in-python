import sys
import os
sys.path.append(os.path.abspath('src'))
import pytest
from src.lexer import Lexer
from src.parser import parse
from src.evaluator import evaluate
from src.environment import defaultenv

@pytest.mark.parametrize("expression,expected", [
    ("(+ (+ 1 1) (+ 1 (+ 1 1)))", "5"),
])
def test_simple_addition(expression, expected):
    env = defaultenv()
    lexer = Lexer(expression)
    parsetree = parse(lexer)
    actual = str(evaluate(parsetree, env))
    assert expected == actual

if __name__ == '__main__':
    pytest.main()