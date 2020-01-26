import sys
import os
sys.path.append(os.path.abspath('test'))
from runner import execute, Interpreter

def test_list_functions():
    run = Interpreter().run

    # Testing recursive sumdown function
    run("(def! sumdown (fn* (N) (if (> N 0) (+ N (sumdown  (- N 1))) 0)))")
    assert run("(sumdown 1)") == "1"
    assert run("(sumdown 2)") == "3"
    assert run("(sumdown 6)") == "21"

    # Testing recursive fibonacci function
    run("(def! fib (fn* (N) (if (= N 0) 1 (if (= N 1) 1 (+ (fib (- N 1)) (fib (- N 2)))))))")
    assert run("(fib 1)") == "1"
    assert run("(fib 2)") == "2"
    assert run("(fib 4)") == "5"

    # Testing recursive function in environment.
    assert run("(let* (cst (fn* (n) (if (= n 0) nil (cst (- n 1))))) (cst 1))") == "nil"
    assert run("(let* (f (fn* (n) (if (= n 0) 0 (g (- n 1)))) g (fn* (n) (f n))) (f 2))") == "0"
