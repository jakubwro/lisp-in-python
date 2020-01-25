# most of test cases copied from https://github.com/kanaka/mal/tree/master/tests

import pytest
import sys
import os
sys.path.append(os.path.abspath('test'))
from runner import execute, Interpreter

def test_empty_list():
    assert "()" == execute("()")

@pytest.mark.parametrize("expression,expected", [
    ("(car '(1 2 3 4))", "1"),
    ("(cdr '(1 2 3 4))", "(2, 3, 4)"),
    ("(nth 3 '(1 2 3 4))", "3"),
    ("(car (cdr '(1 2 3 4)))", "2")
])
def test_basic_car_cdr_cons(expression, expected):
    assert expected == execute(expression)

@pytest.mark.parametrize("expression,expected", [
    ("(+ (+ 1 1) (+ 1 (+ 1 1)))", "5"),
    ("(/ (- (+ 515 (* 87 311)) 302) 27)", "1010"),
    ("(/ (- (+ 515 (* -87 311)) 296) 27)", "-994"),
])
def test_basic_arithmetic(expression, expected):
    assert expected == execute(expression)

if __name__ == '__main__':
    pytest.main()