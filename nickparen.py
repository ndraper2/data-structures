# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from stack import Stack


def paren_check(string_to_check):
    """Return a value indicating whether parentheses in a string match."""
    count = 0
    for char in string_to_check:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count < 0:
            return -1
    if count > 0:
        return 1
    return 0


def pair_check(string_to_check):
    """Return a value indicating whether parentheses or brackets in a string match."""
    open_set = {'(', '[', '{'}
    closed_dict = {')': '(', ']': '[', '}': '{'}
    stack = Stack()
    for char in string_to_check:
        if char in open_set:
            stack.push(char)
        elif char in closed_dict:
            try:
                if stack.pop() == closed_dict[char]:
                    continue
                else:
                    return -1
            except IndexError:
                return -1
    try:
        stack.pop()
        return 1
    except IndexError:
        return 0
