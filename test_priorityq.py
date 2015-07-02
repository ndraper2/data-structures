#-*- coding:UTF-8 -*-
from __future__ import unicode_literals
from priorityq import PriorityQ
import pytest


@pytest.fixture
def full_priorityq():
    priorityq = PriorityQ()
    priorityq.insert(3, 8)
    priorityq.insert(5, 2)
    priorityq.insert(6, 3)
    priorityq.insert(4, 10)
    priorityq.insert(7, 3)
    return priorityq


def test_init_empty():
    priorityq = PriorityQ()
    assert priorityq.list == []


def test_insert():
    priorityq = PriorityQ()
    priorityq.insert(3, 8)
    assert priorityq.list[0].value == 3


def test_insert_more():
    priorityq = PriorityQ()
    priorityq.insert(3, 8)
    priorityq.insert(5, 2)
    assert priorityq.list[0].value == 5
    assert priorityq.list[1].value == 3


def test_pop_first(full_priorityq):
    assert full_priorityq.pop() == 5


def test_pop_more(full_priorityq):
    assert full_priorityq.pop() == 5
    assert full_priorityq.pop() == 6
    assert full_priorityq.pop() == 7


def test_pop_last():
    priorityq = PriorityQ()
    priorityq.insert(5, 2)
    assert priorityq.pop() == 5
    assert priorityq.list == []


def pop_empty():
    priorityq = PriorityQ()
    with pytest.raises(IndexError):
        priorityq.pop()


def test_burn_the_whole_thing(full_priorityq):
    assert full_priorityq.pop() == 5
    assert full_priorityq.pop() == 6
    assert full_priorityq.pop() == 7
    assert full_priorityq.pop() == 3
    assert full_priorityq.pop() == 4
