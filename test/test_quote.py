import pytest
import sys
import os
sys.path.append(os.path.abspath('test'))
from runner import execute, Interpreter

def test_list_functions():
    run = Interpreter().run
    assert run("(quote (1 2 3))") == "(1 2 3)"
    assert run("(quote (+ 1 3))") == "(+ 1 3)"

    # Testing cons function
    assert run('(cons 1 (list))') == '(1)'
    assert run('(cons 1 (list 2))') == '(1 2)'
    assert run('(cons 1 (list 2 3))') == '(1 2 3)'
    assert run('(cons (list 1) (list 2 3))') == '((1) 2 3)'

    run("(def! a (list 2 3))")
    assert run('(cons 1 a)') == '(1 2 3)'
    assert run('a') == '(2 3)'

    # Testing concat function
    assert run('(concat)') == '()'
    assert run('(concat (list 1 2))') == '(1 2)'
    assert run('(concat (list 1 2) (list 3 4))') == '(1 2 3 4)'
    assert run('(concat (list 1 2) (list 3 4) (list 5 6))') == '(1 2 3 4 5 6)'
    assert run('(concat (concat))') == '()'
    assert run('(concat (list) (list))') == '()'

    run("(def! a (list 1 2)))")
    run("(def! b (list 3 4)))")
    assert run('(concat a b (list 5 6))') == '(1 2 3 4 5 6)'
    assert run('a') == '(1 2)'
    assert run('b') == '(3 4)'

    # Testing regular quote
    assert run('(quote 7)') == '7'
    assert run('(quote (1 2 3))') == '(1 2 3)'
    assert run('(quote (1 2 (3 4)))') == '(1 2 (3 4))'

    # Testing simple quasiquote
    assert run('(quasiquote 7)') == '7'
    assert run('(quasiquote (1 2 3))') == '(1 2 3)'
    assert run('(quasiquote (1 2 (3 4)))') == '(1 2 (3 4))'
    assert run('(quasiquote (nil))') == '(nil)'

    # Testing unquote
    assert run('(quasiquote (unquote 7))') == '7'
    assert run('(def! a 8)') == '8'
    assert run('(quasiquote a)') == 'a'
    assert run('(quasiquote (unquote a))') == '8'
    assert run('(quasiquote (1 a 3))') == '(1 a 3)'
    assert run('(quasiquote (1 (unquote a) 3))') == '(1 8 3)'
    assert run('(def! b (quote (1 "b" "d")))') == '(1 "b" "d")'
    assert run('(quasiquote (1 b 3))') == '(1 b 3)'
    assert run('(quasiquote (1 (unquote b) 3))') == '(1 (1 "b" "d") 3)'
    assert run('(quasiquote ((unquote 1) (unquote 2)))') == '(1 2)'

    # Testing splice-unquote
    assert run('(def! c (quote (1 "b" "d")))') == '(1 "b" "d")'
    assert run('(quasiquote (1 c 3))') == '(1 c 3)'
    assert run('(quasiquote (1 (splice-unquote c) 3))') == '(1 1 "b" "d" 3)'

    # Testing symbol equality
    assert run('(= (quote abc) (quote abc))') == 'true'
    assert run('(= (quote abc) (quote abcd))') == 'false'
    assert run('(= (quote abc) "abc")') == 'false'
    assert run('(= "abc" (quote abc))') == 'false'
    assert run('(= (quote abc) nil)') == 'false'
    assert run('(= nil (quote abc))') == 'false'
