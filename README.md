# Lisp in Python
[![Build Status](https://travis-ci.org/jakubwro/lisp-in-python.svg?branch=master)](https://travis-ci.org/jakubwro/lisp-in-python)
[![Coverage Status](https://coveralls.io/repos/github/jakubwro/lisp-in-python/badge.svg)](https://coveralls.io/github/jakubwro/lisp-in-python)

Just a simple Lisp with macros, quotations and tail calls.

## Example

To run REPL use `run-repl.sh` script

```
$./run-repl.sh

Welcome to the REPL!
Press CTRL+C to quit.

lisp-in-python> (+ 1 (+ 2 3))
6
lisp-in-python> (def! fib (fn* (N)
                	(if (= N 0)
                		1
                		(if (= N 1)
                			1
                			(+ (fib (- N 1)) (fib (- N 2)))))))
<function>
lisp-in-python> (fib 8)
34
lisp-in-python> (fib 11)
144
lisp-in-python> (defmacro! unless (fn* (pred a b) (quasiquote (if (unquote pred) (unquote b) ( unquote a)))))
<function>
lisp-in-python> (unless false 1 2)
1
lisp-in-python> (unless true 1 2)
2
lisp-in-python> (macroexpand (unless true 1 2))
(if true 2 1)
```

## Resources
I was inspired by these projects:
-   [Make-A-Lisp](https://github.com/kanaka/mal/blob/master/process/guide.md)
-   [femtolisp](https://github.com/JeffBezanson/femtolisp)
-   [ChezScheme](https://github.com/cisco/ChezScheme)
