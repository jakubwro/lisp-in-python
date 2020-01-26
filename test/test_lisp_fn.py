# most of test cases copied from https://github.com/kanaka/mal/tree/master/tests

import pytest
import sys
import os
sys.path.append(os.path.abspath('test'))
from runner import execute, Interpreter

def test__fn():
    run = Interpreter().run
    assert run("(+ 1 2)") == "3"
    assert run("( (fn* (a b) (+ b a)) 3 4)") == "7"
    assert run("( (fn* () 4) )") == "4"
    assert run("( (fn* (f x) (f x)) (fn* (a) (+ 1 a)) 7)") == "8"

    # Testing closures
    assert run("( ( (fn* (a) (fn* (b) (+ a b))) 5) 7)") == "12"
    run("(def! gen-plus5 (fn* () (fn* (b) (+ 5 b))))")
    run("(def! plus5 (gen-plus5))")
    assert run("(plus5 7)") == "12"

    run("(def! gen-plusX (fn* (x) (fn* (b) (+ x b))))")
    run("(def! plus7 (gen-plusX 7))")
    assert run("(plus7 8)") == "15"
