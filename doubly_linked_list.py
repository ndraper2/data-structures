# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Node(object):
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class DoubleList(object):
    def __init__(self):
        self.size = 0
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
        self.tail = Node(value, None, self.tail)
        if not self.head:
            self.head = self.tail
        else:
            self.tail.prev.next = self.tail

    def pop(self):
        if not self.head:
            raise IndexError("List is empty!")
        return_val = self.head.value
        self.head = self.head.next
        try:
            self.head.prev = None
        except AttributeError:
            self.tail = None
        self.size -= 1
        return return_val

    def shift(self):
        if not self.tail:
            raise IndexError("List is empty!")
        return_val = self.tail.value
        self.tail = self.tail.prev
        try:
            self.tail.next = None
        except AttributeError:
            self.head = None
        self.size -= 1
        return return_val

    def search(self, value):
        iter_node = self.head
        while iter_node:
            if iter_node.value == value:
                return iter_node
            iter_node = iter_node.next
        return None

    def remove(self, value):
        iter_node = self.head
        while iter_node:
            if iter_node.value == value:
                try:
                    iter_node.prev.next = iter_node.next
                except AttributeError:
                    self.head = iter_node.next
                try:
                    iter_node.next.prev = iter_node.prev
                except AttributeError:
                    self.tail = iter_node.prev
                self.size -= 1
                return
            iter_node = iter_node.next
        raise ValueError('Value not in list')
