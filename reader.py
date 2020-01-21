from re import compile,  findall, match

tokenize_regex = compile(r"""[\s,]*(~@|[()'`~^@]|"(?:[\\].|[^\\"])*"?|;.*|[^\s()'"`@,;]+)""")
integer_regex = compile(r"-?[0-9]+$")

class Reader():
    def __init__(self, str):
        self.tokens = tokenize(str)
        self.pos = 0
        print(self.tokens)

    def next(self):
        token = self.tokens[self.pos]
        self.pos += 1
        return token

    def peek(self):
        if len(self.tokens) <= self.pos:
            return None
        return self.tokens[self.pos]

def tokenize(str):
    tokens = findall(tokenize_regex, str)
    return [t for t in tokens if t[0] != ';']
    
def readform(reader):
    if reader.peek() == "(":
        return readlist(reader)
    else:
        return readatom(reader)

def readlist(reader):
    ast = list()
    token = reader.next()
    assert(token == "(")
    token = reader.peek()
    while token != ")":
        assert(token != None) #todo
        ast.append(readform(reader))
        token = reader.peek()
    reader.next()
    return ast

def readatom(reader):
    token = reader.next()
    if match(integer_regex, token):
        return int(token)
    elif token == "nil":
        return None
    elif token == "true":
        return True
    elif token == "false":
        return False
    else:
        return token
    return token

def read(str):
    reader = Reader(str)
    ast = readform(reader)
    return ast
