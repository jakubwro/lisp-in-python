from lexer import Lexer
from parser import parse
from prompter import displayprompt, readexpression, displayerror, welcome, bye, displayresult
from presenter import present
from lisptypes import LispException, defaultenv
from evaluator import evaluate

welcome()
displayprompt()
env = defaultenv()
while True:
    try:
        displayresult(present(evaluate(parse(Lexer(readexpression())), env)))
    except LispException as e:
        displayerror(str(e))
    except (KeyboardInterrupt, EOFError):
        bye()
        exit(0)
    except BaseException as e:
        displayerror(str(e))

