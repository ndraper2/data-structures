#-*- coding:UTF-8 -*-
from __future__ import unicode_literals
from linked_list import LinkedList


class Stack(object):
    def __init__(self, iterable=None):
        if iterable:
            self.list = LinkedList(iterable)
        else:
            self.list = LinkedList()

    def push(self, value):
        self.list.insert(value)

    def pop(self):
        return self.list.pop()

