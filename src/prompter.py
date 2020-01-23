from sys import stdin, stdout, stderr

prompt = "lisp-in-python> "
def displayprompt(morenewlines = False):
    if morenewlines:
        stdout.write("\n")
    stdout.write("\033[92m\033[1m")
    stdout.write(prompt)
    stdout.write("\033[0m")
    stdout.flush()

def displayerror(message):
    stdout.write("\033[91m")
    stdout.write(f"ERROR: {message}\n")
    stdout.write("\033[0m")
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