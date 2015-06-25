# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList(object):
    def __init__(self, iterable=None):
        self.size = 0
        self.head = None
        if iterable:
            for item in iterable:
                self.insert(item)

    def insert(self, value):
        self.head = Node(value, self.head)
        self.size += 1

    def pop(self):
        if not self.head:
            raise IndexError("List is empty!")
        return_val = self.head.value
        self.head = self.head.next
        self.size -= 1
        return return_val

    def size(self):
        return self.size

    def search(self, value):
        iter_node = self.head
        while iter_node:
            if iter_node.value == value:
                return iter_node
            iter_node = iter_node.next
        return None

    def remove(self, node):
        if self.head == node:
            self.head = self.head.next
        else:
            iter_node = self.head
            while iter_node.next:
                if iter_node.next == node:
                    iter_node.next = iter_node.next.next
                    self.size -= 1
                    return None
                iter_node = iter_node.next
            raise ValueError('node not in list')

    def display(self):
        temp_list = []
        iter_node = self.head
        while iter_node:
            temp_list.append(iter_node.value)
            iter_node = iter_node.next
        return tuple(temp_list)

    def __str__(self):
        return str(self.display())

    def __repr__(self):
        return str(self.display())
