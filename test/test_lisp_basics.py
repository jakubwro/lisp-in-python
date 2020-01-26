# most of test cases copied from https://github.com/kanaka/mal/tree/master/tests

import pytest
import sys
import os
sys.path.append(os.path.abspath('test'))
from runner import execute, Interpreter

def test_empty_list():
    assert "()" == execute("()")
    assert "nil" == execute("")
    assert "nil" == execute("nil")

@pytest.mark.parametrize("expression,expected", [
    ("(+ (+ 1 1) (+ 1 (+ 1 1)))", "5"),
    ("(/ (- (+ 515 (* 87 311)) 302) 27)", "1010"),
    ("(/ (- (+ 515 (* -87 311)) 296) 27)", "-994"),
])
def test_basic_arithmetic(expression, expected):
    assert expected == execute(expression)

def test_operators():
    run = Interpreter().run
    assert run("(= 2 1)") == "false"
    assert run("(= 1 1)") == "true"
    assert run("(= 1 2)") == "false"
    assert run("(= 1 (+ 1 1))") == "false"
    assert run("(= 2 (+ 1 1))") == "true"
    assert run("(= nil 1)") == "false"
    assert run("(= nil nil)") == "true"

    assert run("(> 2 1)") == "true"
    assert run("(> 1 1)") == "false"
    assert run("(> 1 2)") == "false"

    assert run("(>= 2 1)") == "true"
    assert run("(>= 1 1)") == "true"
    assert run("(>= 1 2)") == "false"

    assert run("(< 2 1)") == "false"
    assert run("(< 1 1)") == "false"
    assert run("(< 1 2)") == "true"

    assert run("(<= 2 1)") == "false"
    assert run("(<= 1 1)") == "true"
    assert run("(<= 1 2)") == "true"


    assert run("(= 1 1)") == "true"
    assert run("(= 0 0)") == "true"
    assert run("(= 1 0)") == "false"
    assert run("(= true true)") == "true"
    assert run("(= false false)") == "true"
    assert run("(= nil nil)") == "true"

    assert run("(= (list) (list))") == "true"
    assert run("(= (list 1 2) (list 1 2))") == "true"
    assert run("(= (list 1) (list))") == "false"
    assert run("(= (list) (list 1))") == "false"
    assert run("(= 0 (list))") == "false"
    assert run("(= (list) 0)") == "false"
    assert run("(= (list nil) (list))") == "false"

if __name__ == '__main__':
    pytest.main()