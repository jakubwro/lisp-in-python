from re import compile, findall

tokenize_regex = compile(r"""[\s,]*(~@|[()'`~^@]|"(?:[\\].|[^\\"])*"?|;.*|[^\s()'"`@,;]+)""")

def tokenize(str):
    tokens = findall(tokenize_regex, str)
    return [t for t in tokens if t[0] != ';']

class Lexer():
    def __init__(self, str):
        self.tokens = tokenize(str)
        self.pos = 0
        # print(self.tokens)

    def next(self):
        token = self.tokens[self.pos]
        self.pos += 1
        return token

    def peek(self):
        if len(self.tokens) <= self.pos:
            return None
        return self.tokens[self.pos]