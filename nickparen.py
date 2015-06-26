# -*- coding: utf-8 -*-
from __future__ import unicode_literals


def paren_check(string_to_check):
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
