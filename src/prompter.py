from sys import stdin, stdout, stderr

prompt = "lisp-in-python> "
def displayprompt():
    stdout.write(f"\033[92m\033[1m{prompt}\033[0m")
    stdout.flush()

def displayerror(message):
    stdout.write(f"\033[91mERROR: {message}\033[0m\n")
    stdout.flush()
    displayprompt()

def displayresult(result):
    stdout.write(result)
    stdout.write("\n")
    stdout.flush()
    displayprompt()

def readexpression():
    expression = ""
    open_parens = 0 #TODO: match parens with stack to aviod )(
    indent = len(prompt) #TODO: dynamic indent update
    while True:
        stdout.flush()
        line = input()
        expression = f"{expression} {line}"
        open_parens += (line.count("(") - line.count(")")) # TODO: handle escaped parens
        if not open_parens:
            return expression
        stdout.write(" " * indent)

def welcome():
    stdout.write("\nWelcome to the REPL!\nPress CTRL+C to quit.\n\n")

def bye():
    stdout.write("\n\nGood bye!\n\n")