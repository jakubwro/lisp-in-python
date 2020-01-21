from sys import stdin, stdout, stderr
import sys
import re
import reader, printer

prompt = "lisp-in-python>"
def displayprompt():
    stdout.write(f"{prompt} ")
    stdout.flush()

def read():
    line = stdin.readline()
    ast = reader.read(line)
    return ast

def eval(ast):
    return str(ast)

def print(str):
    stdout.write(str)
    if len(str) > 0:
        stdout.write("\n")

def loop():
    displayprompt()
    while True:
        print(eval(read()))
        displayprompt()

loop()
