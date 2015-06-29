# -*- coding:UTF-8 -*-
from __future__ import unicode_literals
import pytest
from queue import Queue


@pytest.fixture
def full_queue():
    queue = Queue()
    queue.enqueue(True)
    queue.enqueue('a string')
    queue.enqueue(5)
    queue.enqueue(10)
    return queue


def test_constructor():
    queue = Queue()
    assert queue.head is None
    assert queue.tail is None
    assert queue._size == 0


def test_enque():
    queue = Queue()
    queue.enqueue(5)
    assert queue.head.value == 5


def test_deque(full_queue):
    assert full_queue.dequeue() is True
    assert full_queue.dequeue() == 'a string'
    assert full_queue.size() == 2


def test_size(full_queue):
    assert full_queue.size() == 4
    full_queue.enqueue('1')
    assert full_queue.size() == 5
    full_queue.dequeue()
    assert full_queue.size() == 4


def test_dequeue_empty():
    queue = Queue()
    with pytest.raises(IndexError):
        queue.dequeue()
