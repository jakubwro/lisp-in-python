import pytest
import sys
import os
sys.path.append(os.path.abspath('test'))
from runner import execute, Interpreter

def test_list_functions():
    run = Interpreter().run

    # Testing trivial macros
    run("(defmacro! one (fn* () 1))")
    assert run('(one)') == '1'
    run("(defmacro! two (fn* () 2))")
    assert run('(two)') == '2'

    # Testing unless macros
    run("(defmacro! unless (fn* (pred a b) (quasiquote (if (unquote pred) (unquote b) ( unquote a)))))")
    assert run('(unless false 7 8)') == '7'
    assert run('(unless true 7 8)') == '8'
    run("(defmacro! unless2 (fn* (pred a b) (list (quote if) (list (quote not) pred) a b)))")
    assert run('(unless2 false 7 8)') == '7'
    assert run('(unless2 true 7 8)') == '8'

    # Testing macroexpand
    assert run('(macroexpand (unless2 2 3 4))') == '(if (not 2) 3 4)'

    # Testing evaluation of macro result
    run("(defmacro! identity (fn* (x) x))")
    assert run('(let* (a 123) (identity a))') == '123'

    # Test that macros do not break empty list
    assert run('()') == '()'

