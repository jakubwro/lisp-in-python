from sys import stdin, stdout, stderr

prompt = "lisp-in-python>"
def displayprompt(morenewlines = False):
    if morenewlines:
        stdout.write("\n")
    stdout.write(f"{prompt} ")
    stdout.flush()

def readexpression():
    return stdin.readline()