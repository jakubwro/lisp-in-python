import unittest
from src.lexer import Lexer

def alltokens(lexer):
    while (lexer.peek() != None):
        yield lexer.next()

class TestLexer(unittest.TestCase):

    def test_empty_input(self):
        lexer = Lexer("")
        self.assertEqual(lexer.peek(), None)

    def test_empty_list(self):
        lexer = Lexer("()")
        tokens = list(alltokens(lexer))
        self.assertEqual(tokens, ['(', ')'])

    def test_missing_closing_paren(self):
        lexer = Lexer("(+ 3 4")
        tokens = list(alltokens(lexer))
        self.assertEqual(tokens, ['(', '+', '3', '4'])

    def test_nil_token(self):
        lexer = Lexer("(nil)")
        tokens = list(alltokens(lexer))
        self.assertEqual(tokens, ['(', 'nil', ')'])

    def test_booleans(self):
        lexer = Lexer("(true false)")
        tokens = list(alltokens(lexer))
        self.assertEqual(tokens, ['(', 'true', 'false', ')'])

    def test_numbers(self):
        lexer = Lexer("(1 2 3.14 -4 -5.0)")
        tokens = list(alltokens(lexer))
        self.assertEqual(tokens, ['(', '1', '2', '3.14', '-4', '-5.0', ')'])

if __name__ == '__main__':
    unittest.main()