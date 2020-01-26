# most of test cases copied from https://github.com/kanaka/mal/tree/master/tests

import pytest
import sys
import os
sys.path.append(os.path.abspath('test'))
from runner import execute, Interpreter

def test_specialform_if():
    run = Interpreter().run
    assert run("(if true 7 8)") == "7"
    assert run("(if false 7 8)") == "8"
    assert run("(if false 7 false)") == "false"
    assert run("(if true (+ 1 7) (+ 1 8))") == "8"
    assert run("(if false (+ 1 7) (+ 1 8))") == "9"
    assert run("(if nil 7 8)") == "8"
    assert run("(if 0 7 8)") == "7"
    assert run("(if (list) 7 8)") == "7"
    assert run("(if (list 1 2 3) 7 8)") == "7"
    assert run("(= (list) nil)") == "false"

def test_specialform_if_oneway():
    run = Interpreter().run
    assert run("(if false (+ 1 7))") == "nil"
    assert run("(if nil 8)") == "nil"
    assert run("(if nil 8 7)") == "7"
    assert run("(if true (+ 1 7))") == "8"
