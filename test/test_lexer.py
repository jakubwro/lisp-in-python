import pytest
from src.lexer import Lexer

def alltokens(lexer):
    while (lexer.peek() != None):
        yield lexer.next()

@pytest.mark.parametrize("expression,expected", [
    ("", []),
    ("()", ['(', ')']),
    ("(+ 3 4",  ['(', '+', '3', '4']),
    ("(nil)", ['(', 'nil', ')']),
    ("(true false)", ['(', 'true', 'false', ')']),
    ("(1 2 3.14 -4 -5.0)", ['(', '1', '2', '3.14', '-4', '-5.0', ')'])
])
def test_lexer(expression, expected):
    lexer = Lexer(expression)
    actual = list(alltokens(lexer))
    assert actual == expected