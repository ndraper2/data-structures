from __future__ import unicode_literals

def parens(string):
    stack = []
    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            try:
                stack.pop()
            except IndexError:
                return -1

    # if len(stack) == 0:
    #     return 0
    # if len(stack) > 0:
    #     return 1
    try:
        stack.pop()
    except IndexError:
        return 0
    return 1