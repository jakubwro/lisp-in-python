from lisptypes import Symbol, LispException, Fn,  Environment

# def expandquotes(ast):
#     expanded = []
#     quotemode = False
#     for node in ast:
#         if node == "'":
#             quotemode = True
#             continue
#         if not quotemode:
#             expanded.append(node)
#         else:
#             expanded.append(['quote', node])
#         quotemode = False
#     if quotemode == True:
#         raise LispException("Unexpected closed paren!")
#     return expanded

def evaluateast(ast, env):
    if isinstance(ast, Symbol):
        return env.get(ast)
    if isinstance(ast, list):
        return list(map(lambda x: evaluate(x, env), ast))
    return ast

def evaluate(ast, env):
    while True:
        if not isinstance(ast, list):
            return evaluateast(ast, env)
        if not ast: # empty list
            return []
        
        form = ast[0]
        if form == 'def!':
            if len(ast) != 3:
                raise(LispException("'def!' requires 2 arguments"))
            return env.set(ast[1], evaluate(ast[2], env))

        if form == "let*":
            if len(ast) != 3:
                raise(LispException("'let*' requires 2 arguments"))
            letenv = Environment(env)
            t = ast[1]
            for i in range(0, len(ast[1]), 2):
                letenv.set(t[i], evaluate(t[i+1], letenv))
            env = letenv
            ast = ast[2]
            continue

        if form == "if":
            if len(ast) < 3:
                raise(LispException("'if' requires at least 2 arguments"))
            cond = evaluate(ast[1], env)
            if cond is None or cond is False:
                if len(ast) > 3:
                    ast = ast[3]
                else:
                    ast = None
            else:
                ast = ast[2]
            continue

        if form == "fn*":
            if len(ast) != 3:
                raise(LispException("'fn*' requires 2 arguments"))
            binds = ast[1]
            body = ast[2]
            return Fn(body, binds, env, evaluate)

        if form == "do":
            for expr in ast[1:-1]:
                evaluate(expr, env)
            ast = ast[-1]
            continue

        if form == "quote":
            return ast[1]

        if form == "quasiquote":
            ast = quasiquote(ast[1])
            continue

        evaluated = evaluateast(ast, env)
        func, args = evaluated[0], evaluated[1:]
        if isinstance(func, Fn):
            ast = func.body
            env = func.newenv(args)
            continue
        if not callable(func):
            raise(LispException(f"{func} is not callable. Are you missing a quotation?"))
        return func(*args)

def ispair(l):
    return isinstance(l, list) and len(l) > 0

def quasiquote(ast):
    if not ispair(ast):
        return [Symbol('quote'), ast]
    elif ast[0] == 'unquote':
        return ast[1]
    elif ispair(ast[0]) and ast[0][0] == 'splice-unquote':
        return [Symbol('concat'), ast[0][1], quasiquote(ast[1:])]
    else:
        return [Symbol('cons'), quasiquote(ast[0]), quasiquote(ast[1:])]
