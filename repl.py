import sys

prompt = "lisp-in-python>"

def read():
    line = sys.stdin.readline()
    return line

def eval(str):
    return str

def print(str):
    sys.stdout.write(str)
    if len(str) > 0:
        sys.stdout.write("\n")
    sys.stdout.write(f"{prompt} ")

def loop():
    sys.stdout.write(f"{prompt} ")
    sys.stdout.flush()
    while True:
        print(eval(read()))
        sys.stdout.flush()

loop()

