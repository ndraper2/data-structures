# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Node(object):
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class DoubleList(object):
    def __init__(self):
        self._size = 0
        self.head = None
        self.tail = None

    def insert(self, value):
        self.size += 1
        self.head = Node(value, self.head)
        if not self.tail:
            self.tail = self.head
        else:
            self.head.next.prev = self.head

    def append(self, value):
        self.size += 1
        self.tail = Node(value, self.tail)
        if not self.head:
            self.head = self.tail
        else:
            self.tail.prev.next = self.tail

    def pop(self):
        if not self.head:
            raise IndexError("List is empty!")
        return_val = self.head.value
        self.head = self.head.next
        self._size -= 1
        return return_val

        def shift(self):


    def size(self):
        return self._size

    def search(self, value):
        iter_node = self.head
        while iter_node:
            if iter_node.value == value:
                return iter_node
            iter_node = iter_node.next
        return None

    def remove(self, node):
        if self.head is node:
            self.head = self.head.next
        else:
            iter_node = self.head
            while iter_node.next:
                if iter_node.next is node:
                    iter_node.next = iter_node.next.next
                    self._size -= 1
                    return None
                iter_node = iter_node.next
            raise ValueError('node not in list')

    def display(self):
        """Return a tuple-like string containing all the elements of the list."""
        display_string = ''
        iter_node = self.head
        while iter_node:
            display_string += "{},".format(iter_node.value)
            iter_node = iter_node.next
        display_string = "({})".format(display_string.rstrip(','))
        return display_string

    def __str__(self):
        return self.display()

    def __repr__(self):
        return self.display()