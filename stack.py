# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from linked_list import LinkedList


class Stack(object):
    def __init__(self, iterable=None):
        """Create a new Stack with optional given iterable of values."""
        if iterable:
            self.list = LinkedList(iterable)
        else:
            self.list = LinkedList()

    def push(self, value):
        """Push a new value onto the stack."""
        self.list.insert(value)

    def pop(self):
        """Return the top value from the stack and remove the node."""
        return self.list.pop()
