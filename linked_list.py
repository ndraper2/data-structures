# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Node(object):
    """Create a new Node with the given value and optional next pointer."""
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList(object):
    """Create a new LinkedList with optional given iterable of values."""
    def __init__(self, iterable=None):
        self._size = 0
        self.head = None
        if iterable:
            for item in iterable:
                self.insert(item)

    def insert(self, value):
        """Create a new node and insert it a the head of the list."""
        self.head = Node(value, self.head)
        self._size += 1

    def pop(self):
        """Remove the head node from the list and return its value."""
        if not self.head:
            raise IndexError("List is empty!")
        return_val = self.head.value
        self.head = self.head.next
        self._size -= 1
        return return_val

    def size(self):
        """Return the size of the list."""
        return self._size

    def search(self, value):
        """Return the node containing the provided value."""
        iter_node = self.head
        while iter_node:
            if iter_node.value == value:
                return iter_node
            iter_node = iter_node.next
        return None

    def remove(self, node):
        """Remove the given node."""
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
