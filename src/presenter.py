from prompter import displayprompt

def present(content):
    print(content)
    displayprompt(morenewlines = not content)
