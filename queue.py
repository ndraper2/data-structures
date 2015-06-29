#-*- coding:UTF-8 -*-
from __future__ import unicode_literals
from linked_list import Node


class Queue(object):
    def __init__(self, iterable=None):
        self._size = 0
        self.head = None
        if iterable:
            for item in iterable:
                self.enqueue(item)

    def enqueue(self, value):  #adds value to the queue
        self.head.next = Node(val)
        self.head = self.head.next
        self._size += 1

    def dequeue(self):  #removes the correct item from the queue and returns its value
        value = self.tail.value
        self.tail = self.tail.next
        self._size -= 1
        return value

    def size(self):
        return self._size




