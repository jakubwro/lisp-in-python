import pytest
import sys
import os
sys.path.append(os.path.abspath('test'))
from runner import execute, Interpreter

def test_list_functions():
    run = Interpreter().run
    # assert run("(quote (1 2 3))") == "(1 2 3)"
    # assert run("(quote (+ 1 3)") == "(+ 1 3)"
