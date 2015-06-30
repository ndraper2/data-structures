# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from doubly_linked_list import DoubleList, Node
import pytest


@pytest.fixture
def full_list():
    list = DoubleList()
    list.insert(True)
    list.insert('a string')
    list.insert(5)
    list.insert(10)
    return list


def test_node_init():
    node = Node(5)
    assert node.value == 5
    assert node.next is None
    assert node.prev is None


def test_node_bad_init():
    with pytest.raises(TypeError):
        Node(24, 'arg', 'arg2', 'arg3')


def test_empty_list():
    list = DoubleList()
    assert list.head is None
    assert list.tail is None


def test_insert():
    list = DoubleList()
    list.insert(5)
    assert list.head.value == 5
    assert list.tail.value == 5
    list.insert(10)
    assert list.head.value == 10
    assert list.tail.value == 5
    assert list.head.next.value == 5
    assert list.tail.prev.value == 10


def test_append():
    list = DoubleList()
    list.append(5)
    assert list.tail.value == 5
    assert list.head.value == 5
    list.append(10)
    assert list.tail.value == 10
    assert list.head.value == 5
    assert list.tail.prev.value == 5
    assert list.head.next.value == 10


def test_pop(full_list):
    assert full_list.pop() == 10
    assert full_list.size == 3
    assert full_list.pop() == 5
    assert full_list.pop() == 'a string'
    assert full_list.pop() is True
    assert full_list.size == 0
    with pytest.raises(IndexError):
        full_list.pop()


def test_shift(full_list):
    assert full_list.shift() is True
    assert full_list.size == 3
    assert full_list.shift() == 'a string'
    assert full_list.shift() == 5
    assert full_list.shift() == 10
    assert full_list.size == 0
    with pytest.raises(IndexError):
        full_list.shift()


def test_remove(full_list):
    full_list.remove('a string')
    assert full_list.size == 3
    with pytest.raises(ValueError):
        full_list.remove('a string')
    full_list.remove(5)
    full_list.remove(10)
    full_list.remove(True)
    assert full_list.size == 0
    assert full_list.head is None
    assert full_list.tail is None
