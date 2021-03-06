# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from linked_list import LinkedList, Node
import pytest


@pytest.fixture
def full_list():
    list = LinkedList()
    list.insert(True)
    list.insert('a string')
    list.insert(5)
    list.insert(10)
    return list


def test_node_init():
    node = Node(5)
    assert node.value == 5
    assert node.next is None


def test_node_bad_init():
    with pytest.raises(TypeError):
        node = Node(24, 'blah', 'blah')


def test_empty_list():
    list = LinkedList()
    assert isinstance(list, LinkedList)
    assert list.head is None


def test_insert():
    list = LinkedList()
    list.insert(5)
    assert list.head.value == 5


def test_size(full_list):
    assert full_list.size() == 4


def test_list_init_iterable():
    list = LinkedList([5, True, 'string'])
    assert list.head.value == 'string'
    assert list.size() == 3
    assert list.search(True).value is True


def test_list_init_not_iterable():
    with pytest.raises(TypeError):
        list = LinkedList(534)


def test_pop(full_list):
    assert full_list.pop() == 10
    assert full_list.size() == 3


def test_pop_empty_list():
    list = LinkedList()
    with pytest.raises(IndexError):
        list.pop()


def test_search(full_list):
    assert full_list.search(5).value == 5


def test_search_nonexistent(full_list):
    assert full_list.search(18) is None


def test_remove(full_list):
    node = full_list.search(5)
    full_list.remove(node)
    assert full_list.search(5) is None
    assert full_list.head.next.value == 'a string'
    assert full_list.size() == 3


def test_remove_last(full_list):
    node = full_list.search(True)
    full_list.remove(node)
    assert full_list.search(True) is None
    node2 = full_list.search('a string')
    assert node2.next is None
    assert full_list.size() == 3


def test_remove_nonexistent(full_list):
    with pytest.raises(ValueError):
        full_list.remove(Node(17))


def test_remove_bad_type(full_list):
    with pytest.raises(ValueError):
        full_list.remove(5)


def test_display(full_list):
    assert full_list.display() == "(10,5,a string,True)"


def test_display_empty_list():
    list = LinkedList()
    assert list.display() == '()'


def test_string(full_list):
    assert str(full_list) == "(10,5,a string,True)"


def test_unicode():
    list = LinkedList(['a ɶ character'])
    assert list.display() == "(a ɶ character)"
