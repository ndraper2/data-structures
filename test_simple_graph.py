# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from simple_graph import Graph
import pytest


@pytest.fixture
def full_graph():
    g = Graph()
    g.add_node(3)
    g.add_node(10)
    g.add_node(15)
    g.add_node(7)
    g.add_node(14)
    g.add_edge(3, 7)
    g.add_edge(15, 10)
    g.add_edge(14, 3)
    g.add_edge(3, 10)
    g.add_edge(7, 15)
    return g


@pytest.fixture
def cyclic_graph():
    g = Graph()
    g.add_node(3)
    g.add_node(10)
    g.add_node(5)
    g.add_node(2)
    g.add_node(7)
    g.add_edge(3, 10)
    g.add_edge(3, 5)
    g.add_edge(10, 5)
    g.add_edge(5, 2)
    g.add_edge(2, 7)
    return g


def test_init():
    g = Graph()
    assert g.gdict == {}


def test_add_node():
    g = Graph()
    g.add_node(5)
    assert g.gdict == {5: []}


def test_add_edge():
    g = Graph()
    g.add_node(5)
    g.add_node(10)
    g.add_edge(5, 10)
    assert g.gdict[5] == [10]


def test_add_edge_new_nodes(full_graph):
    full_graph.add_edge(18, 4)
    assert 18 in full_graph.gdict
    assert 4 in full_graph.gdict
    assert 4 in full_graph.gdict[18]


def test_nodes(full_graph):
    nodes = full_graph.nodes()
    assert 15 in nodes
    assert 3 in nodes
    assert 15 in nodes


def test_edges(full_graph):
    edges = full_graph.edges()
    assert (3, 7) in edges
    assert (14, 3) in edges
    assert (7, 15) in edges


def test_del_node(full_graph):
    full_graph.del_node(3)
    assert 3 not in full_graph.gdict
    for edgelist in full_graph.gdict.values():
        assert 3 not in edgelist


def test_del_node_nonexistent(full_graph):
    with pytest.raises(KeyError):
        full_graph.del_node(18)


def test_del_edge(full_graph):
    full_graph.del_edge(3, 7)
    assert 7 not in full_graph.gdict[3]


def test_del_edge_nonexistent(full_graph):
    with pytest.raises(ValueError):
        full_graph.del_edge(18, 4)
    with pytest.raises(ValueError):
        full_graph.del_edge(15, 25)


def test_has_node(full_graph):
    assert full_graph.has_node(15)
    assert not full_graph.has_node(25)


def test_neighbors(full_graph):
    neighbors = full_graph.neighbors(3)
    assert 10 in neighbors
    assert 7 in neighbors


def test_adjacent(full_graph):
    assert full_graph.adjacent(15, 10)
    assert not full_graph.adjacent(3, 14)


def test_adjacent_nonexistent(full_graph):
    with pytest.raises(KeyError):
        full_graph.adjacent(15, 19)
    with pytest.raises(KeyError):
        full_graph.adjacent(19, 15)


def test_depth_first_traversal(full_graph):
    full_graph.add_edge(10, 9)
    assert full_graph.depth_first_traversal(14) == [14, 3, 10, 9, 7, 15]


def test_depth_first_traversal_partial(full_graph):
    full_graph.add_edge(10, 9)
    assert full_graph.depth_first_traversal(7) == [7, 15, 10, 9]


def test_depth_first_traversal_cyclic(cyclic_graph):
    assert cyclic_graph.depth_first_traversal(3) == [3, 5, 2, 7, 10]


def test_breadth_first_traversal(full_graph):
    full_graph.add_edge(10, 9)
    assert full_graph.breadth_first_traversal(14) == [14, 3, 7, 10, 15, 9]


def test_breadth_first_traversal_partial(full_graph):
    full_graph.add_edge(10, 9)
    assert full_graph.breadth_first_traversal(7) == [7, 15, 10, 9]


def test_breadth_first_traversal_cyclic(cyclic_graph):
    assert cyclic_graph.breadth_first_traversal(3) == [3, 10, 5, 2, 7]




