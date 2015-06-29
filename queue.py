#-*- coding:UTF-8 -*-
from __future__ import unicode_literals
from linked_list import Node


class Queue(object):
    """Create a new Queue with optional given iterable of values."""
    def __init__(self, iterable=None):
        self._size = 0
        self.head = None
        self.tail = None
        if iterable:
            for item in iterable:
                self.enqueue(item)

    def enqueue(self, value):
        """Create a new node and enqueue it at the head of the queue."""
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
            self._size = 1
        else:
            self.head.next = Node(value)
            self.head = self.head.next
            self._size += 1

    def dequeue(self):
        """Remove the tail node from the queue and return its value."""
        if self._size == 0:
            raise IndexError("Queue is empty!")
        value = self.tail.value
        self.tail = self.tail.next
        self._size -= 1
        return value

    def size(self):
        """Return the size of the queue."""
        return self._size
