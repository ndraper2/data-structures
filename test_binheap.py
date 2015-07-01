# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from binheap import BinHeap
import pytest


@pytest.fixture()
def full_heap():
    heap = BinHeap()
    heap.push(5)
    heap.push(4)
    heap.push(10)
    heap.push(7)
    heap.push(2)
    return heap


def test_init_empty():
    heap = BinHeap()
    assert heap.list == []


def test_push():
    heap = BinHeap()
    heap.push(5)
    assert heap.list[0] == 5


def test_push_more():
    heap = BinHeap()
    heap.push(5)
    heap.push(4)
    assert heap.list[0] == 4
    assert heap.list[1] == 5


def test_init_iterator():
    heap = BinHeap([5, 4, 10, 7, 2])
    assert heap.list == [2, 4, 10, 7, 5]


def test_pop_first(full_heap):
    assert full_heap.pop() == 2


def test_pop_check_bubble_down(full_heap):
    full_heap.pop()
    assert full_heap.pop() == 4


def test_pop_one_child():
    heap = BinHeap()
    heap.push(5)
    heap.push(10)
    assert heap.pop() == 5


def test_pop_last():
    heap = BinHeap()
    heap.push(5)
    assert heap.pop() == 5
    assert heap.list == []


def pop_empty():
    heap = BinHeap()
    with pytest.raises(IndexError):
        heap.pop()


def test_burn_the_whole_thing(full_heap):
    assert full_heap.pop() == 2
    assert full_heap.pop() == 4
    assert full_heap.pop() == 5
    assert full_heap.pop() == 7
    assert full_heap.pop() == 10
