# most of test cases copied from https://github.com/kanaka/mal/tree/master/tests

import pytest
import sys
import os
sys.path.append(os.path.abspath('test'))
from runner import execute, Interpreter

sys.path.append(os.path.abspath('src'))
from src.lisptypes import LispException

def test_specialform_def():
    run = Interpreter().run
    assert run("(def! x 3)")        == "3"
    assert run("x")                 == "3"
    assert run("(def! x 4)")        == "4"
    assert run("x")                 == "4"
    assert run("(def! y (+ 1 7))")  == "8"
    assert run("y")                 == "8"
    assert run("(+ x y)")           == "12"

def test_specialform_def_lookup_failure():
    # with pytest.raises(BaseException) as excinfo:
    #     run = Interpreter().run
    #     run("(asdf 1 2 3 4)")
    # assert "Symbol 'asdf' is not defined!" == str(excinfo.value)
    run = Interpreter().run
    assert run("(asdf 1 2 3 4)") == "Symbol 'asdf' is not defined!"

def test_specialform_def_error_abort():
    run = Interpreter().run
    assert run("(asdf 1 2 3 4)")  == "Symbol 'asdf' is not defined!"
    assert run("(def! w 44)")     == "44"
    assert run("(def! w (asdf))") == "Symbol 'asdf' is not defined!"
    assert run("w")               == "44"

# ^(.*)\n.*;=>(.*)$
# assert run("$1") == "$2"
def test_specialform_let():
    run = Interpreter().run
    #basic tests
    assert run("(def! x 4)")                            == "4"
    assert run("(let* (z 9) z)")                        == "9"
    assert run("(let* (x 9) x)")                        == "9"
    assert run("x")                                     == "4"
    assert run("(let* (z (+ 2 3)) (+ 1 z))")            == "6"
    assert run("(let* (p (+ 2 3) q (+ 2 p)) (+ p q))")  == "12"
    assert run("(def! y (let* (z 7) z))")               == "7"
    assert run("y")                                     == "7"
    #outer environment tests
    assert run("(def! a 4)")                            == "4"
    assert run("(let* (q 9) q)")                        == "9"
    assert run("(let* (q 9) a)")                        == "4"
    assert run("(let* (z 2) (let* (q 9) a))")           == "4"