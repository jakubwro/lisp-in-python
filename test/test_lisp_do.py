# most of test cases copied from https://github.com/kanaka/mal/tree/master/tests

import pytest
import sys
import os
sys.path.append(os.path.abspath('test'))
from runner import execute, Interpreter

def test_specialform_do():
    run = Interpreter().run
    assert run("(do (def! a 6) 7 (+ a 8))") == "14"
    assert run("a") == "6"

    assert run("(do (prn 101))") == "nil"
    assert run("(do (prn 102) 7)") == "7"
    assert run("(do (prn 101) (prn 102) (+ 1 2))") == "3"

  

    assert run("(do (def! a 6) 7 (+ a 8))") == "14"
    assert run("a") == "6"

    # Testing special form case-sensitivity
    run("(def! DO (fn* (a) 7))")
    assert run("(DO 3)") == "7"
