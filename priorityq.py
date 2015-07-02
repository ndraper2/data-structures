# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from functools import total_ordering
from binheap import BinHeap


@total_ordering
class Node(object):
    """Create a new node with value, priority and id."""
    def __init__(self, value, priority, id):
        self.value = value
        self.priority = priority
        self.id = id

    def __lt__(self, other):
        if self.priority == other.priority:
            return self.id < other.id
        else:
            return self.priority < other.priority

    def __eq__(self, other):
        if self.priority == other.priority:
            return self.id == other.id
        else:
            return self.priority == other.priority


class PriorityQ(BinHeap):
    """Create a new empty priority queue."""
    def __init__(self):
        self.id_count = 0
        super(PriorityQ, self).__init__()

    """Insert a node with given value and priority"""
    def insert(self, value, priority):
        self.list.append(Node(value, priority, self.id_count))
        self.id_count += 1
        self._bubble_up()

    """Pop the top node and return the value of the node."""
    def pop(self):
        return super(PriorityQ, self).pop().value

    """Look at the top node's value and return it."""
    def peek(self):
        return self.list[0].value
