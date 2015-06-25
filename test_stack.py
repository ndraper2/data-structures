# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
from stack import Stack


def test_initialization():
    stack = Stack()
    assert isinstance(stack, Stack)
    assert stack.list.head is None


def test_push():
    stack = Stack()
    stack.push(5)
    assert stack.list.head.value == 5


def test_pop():
    stack = Stack()
    stack.push(5)
    assert stack.pop() == 5


def test_initialization_list():
    stack = Stack([5, 10, 'string'])
    assert stack.pop() == 'string'
    assert stack.pop() == 10
    assert stack.pop() == 5


def test_pop_empty():
    stack = Stack()
    with pytest.raises(IndexError):
        stack.pop()
