from sys import stdin, stdout, stderr

prompt = "lisp-in-python> "
def displayprompt(morenewlines = False):
    if morenewlines:
        stdout.write("\n")
    stdout.write(prompt)
    stdout.flush()

def readexpression():
    expression = ""
    open_parens = 0
    indent = len(prompt) #TODO: dynamic indent update
    while True:
        stdout.flush()
        line = stdin.readline()
        expression = f"{expression} {line}"
        open_parens += (line.count("(") - line.count(")")) # TODO: handle escaped parens
        if not open_parens:
            return expression
        stdout.write(" " * indent)
