import unittest
import sys
import os
sys.path.append(os.path.abspath('src'))
from src.lexer import Lexer
from src.parser import parse
from src.evaluator import evaluate
from src.environment import defaultenv

class TestEval(unittest.TestCase):

    def test_simple_addition(self):
        expr = "(+ (+ 1 1) (+ 1 (+ 1 1)))"
        env = defaultenv()
        lexer = Lexer(expr)
        parsetree = parse(lexer)
        actual = str(evaluate(parsetree, env))
        expected = "5"
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()