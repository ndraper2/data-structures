# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class BinHeap(object):

    def __init__(self, iterable=None):
        """Create a new binary min-heap.
           Insert values from an optional iterable.
        """
        self.list = []
        if iterable:
            for item in iterable:
                self.push(item)

    def push(self, value):
        """Push a new value onto the heap, maintaining the heap property."""
        self.list.append(value)
        self._bubble_up()

    def _bubble_up(self):
        i = len(self.list) - 1
        while (i - 1) // 2 >= 0:
            if self.list[i] < self.list[(i - 1) // 2]:
                self.list[i], self.list[(i - 1) // 2] = (
                    self.list[(i - 1) // 2], self.list[i])
            i = (i - 1) // 2

    def pop(self):
        """Pop the top value off the heap, maintaining the heap property."""
        if len(self.list) == 1:
            return self.list.pop()
        try:
            return_val = self.list[0]
        except IndexError:
            raise IndexError('Heap is empty!')
        self.list[0] = self.list.pop()
        self._bubble_down()
        return return_val

    def _bubble_down(self):
        i = 0
        while i * 2 + 1 <= len(self.list) - 1:
            child = self._min_child(i)
            if self.list[i] > self.list[child]:
                self.list[i], self.list[child] = (
                    self.list[child], self.list[i])
            i = child

    def _min_child(self, index):
        if index * 2 + 2 > len(self.list) - 1:
            return index * 2 + 1
        if self.list[2 * index + 1] > self.list[2 * index + 2]:
            return 2 * index + 2
        else:
            return 2 * index + 1
