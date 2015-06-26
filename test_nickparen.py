# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest
from nickparen import paren_check


@pytest.fixture
def open_string():
    return '()(()(())'


@pytest.fixture
def balanced_string():
    return '()(())()'


@pytest.fixture
def broken_string():
    # makes sure a broken string bails immediately -
    # total count on this is open
    return '())()()(('


def test_open(open_string):
    assert paren_check(open_string) == 1


def test_balanced(balanced_string):
    assert paren_check(balanced_string) == 0


def test_broken(broken_string):
    assert paren_check(broken_string) == -1
