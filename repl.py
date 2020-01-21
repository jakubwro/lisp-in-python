from sys import stdin, stdout, stderr

prompt = "lisp-in-python>"

def read():
    line = stdin.readline()
    return line

def eval(str):
    return str

def print(str):
    stdout.write(str)
    if len(str) > 0:
        stdout.write("\n")
    stdout.write(f"{prompt} ")

def loop():
    stdout.write(f"{prompt} ")
    stdout.flush()
    while True:
        print(eval(read()))
        stdout.flush()

loop()

