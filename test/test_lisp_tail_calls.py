import pytest
import sys
import os
sys.path.append(os.path.abspath('test'))
from runner import execute, Interpreter

def test_tail_calls():
    run = Interpreter().run

    run("(def! sum2 (fn* (n acc) (if (= n 0) acc (sum2 (- n 1) (+ n acc)))))")
    assert run('(sum2 10 0)') == '55'
    assert run('(def! res2 nil)') == 'nil'
    assert run("(def! res2 (sum2 10000 0))") == '50005000'
    assert run('res2') == '50005000'

    run("(def! foo (fn* (n) (if (= n 0) 0 (bar (- n 1)))))")
    run("(def! bar (fn* (n) (if (= n 0) 0 (foo (- n 1)))))")
    assert run('(foo 10000)') == '0'
