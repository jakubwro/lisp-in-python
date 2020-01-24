from sys import stdin, stdout, stderr

def presentlist(content, buffer):
    buffer.append("(")
    i = 1
    for item in content:
        presentresult(item, buffer)
        if i < len(content):
            buffer.append(", ")
        i = i + 1
    buffer.append(")")

def presentresult(content, buffer):
    if (content == None):
        buffer.append("nil")
    elif (isinstance(content, list)):
        presentlist(content, buffer)
    else:
        buffer.append(str(content))

def present(content):
    buffer = []
    presentresult(content, buffer)
    return "".join(buffer)
        
