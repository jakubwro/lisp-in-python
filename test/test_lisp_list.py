import pytest
import sys
import os
sys.path.append(os.path.abspath('test'))
from runner import execute, Interpreter

def test_list_functions():
    run = Interpreter().run
    assert run("(list)") == "()"
    assert run("(list? (list))") == "true"
    assert run("(empty? (list))") == "true"
    assert run("(empty? (list 1))") == "false"
    assert run("(list 1 2 3)") == "(1 2 3)"
    assert run("(count (list 1 2 3))") == "3"
    assert run("(count (list))") == "0"
    assert run("(count nil)") == "0"
    assert run("(if (> (count (list 1 2 3)) 3) 89 78)") == "78"
    assert run("(if (>= (count (list 1 2 3)) 3) 89 78)") == "89"

@pytest.mark.parametrize("expression,expected", [
    ("(car '(1 2 3 4))", "1"),
    ("(cdr '(1 2 3 4))", "(2 3 4)"),
    ("(nth 3 '(1 2 3 4))", "3"),
    ("(car (cdr '(1 2 3 4)))", "2")
])
def test_basic_car_cdr_cons(expression, expected):
    assert expected == execute(expression)