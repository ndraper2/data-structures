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
        self._bubble_up(len(self.list) - 1)

    def _bubble_up(self, index):
        if index == 0:
            return
        if self.list[index] < self.list[(index - 1) // 2]:
            self.list[index], self.list[(index - 1) // 2] = (
                self.list[(index - 1) // 2], self.list[index])
            self._bubble_up((index - 1) // 2)

    def pop(self):
        """Pop the top value off the heap, maintaining the heap property."""
        if len(self.list) == 1:
            return self.list.pop()
        try:
            return_val = self.list[0]
        except IndexError:
            raise IndexError('Heap is empty!')
        self.list[0] = self.list.pop()
        self._bubble_down(0)
        return return_val

    def _bubble_down(self, index):
        if index * 2 >= len(self.list) - 1:
            return
        child = self._min_child(index)
        if self.list[index] > self.list[child]:
            self.list[index], self.list[child] = (
                self.list[child], self.list[index])
            self._bubble_down(child)

    def _min_child(self, index):
        if index * 2 + 2 > len(self.list) - 1:
            return index * 2 + 1
        if self.list[2 * index + 1] > self.list[2 * index + 2]:
            return 2 * index + 2
        else:
            return 2 * index + 1
