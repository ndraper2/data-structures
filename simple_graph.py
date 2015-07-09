# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Graph(object):

    def __init__(self):
        """Create a new empty graph."""
        self.gdict = {}

    def nodes(self):
        """Return a list of nodes in the graph."""
        return self.gdict.keys()

    def edges(self):
        """Return a list of edges in the graph."""
        self.edges = []
        for node in self.gdict:
            for end in self.gdict[node]:
                self.edges.append((node, end))
        return self.edges

    def add_node(self, n):
        """Add a node n into the graph.
        Nodes must be hashable."""
        self.gdict.setdefault(n, [])

    def add_edge(self, n1, n2):
        """Add an edge connecting n1 and n2 to the graph."""
        self.gdict.setdefault(n2, [])
        try:
            self.gdict[n1].append(n2)
        except KeyError:
            self.gdict[n1] = [n2]

    def del_node(self, n):
        """Delete node n from the graph."""
        try:
            del self.gdict[n]
        except KeyError:
            raise KeyError('{} not in the graph.'.format(n))
        for nodelist in self.gdict.values():
            try:
                nodelist.remove(n)
            except ValueError:
                continue

    def del_edge(self, n1, n2):
        """Delete the edge connecting n1 and n2 from the graph."""
        try:
            self.gdict[n1].remove(n2)
        except (KeyError, ValueError):
            raise ValueError('Edge {}, {} not in the graph.'.format(n1, n2))

    def has_node(self, n):
        """Return True if n is in the graph, else False."""
        return n in self.gdict

    def neighbors(self, n):
        """Return the list of nodes n is pointing to."""
        try:
            return self.gdict[n]
        except KeyError:
            raise KeyError('{} not in the graph.'.format(n))

    def adjacent(self, n1, n2):
        """Return True if there is an edge connecting n1 and n2, else False."""
        if n1 not in self.gdict or n2 not in self.gdict:
            raise KeyError('One of these nodes is not in the graph.')
        return n2 in self.gdict[n1]

    def depth_first_traversal(self, start):
        return self._depth_first_traversal(start, [])

    def _depth_first_traversal(self, current, visited):
        visited.append(current)
        for neighbor in self.neighbors(current):
            if neighbor not in visited:
                self._depth_first_traversal(neighbor, visited)
        return visited

    def breadth_first_traversal(self, start):
        from queue import Queue
        q = Queue()
        q.enqueue(start)
        visited = [start]
        while q.size() > 0:
            current = q.dequeue()
            for neighbor in current.neighbors():
                if neighbor not in visited:
                    q.enqueue(neighbor)
                    visited.append(neighbor)
        return visited

    def depth_first_traversal(self, start):
        from stack import Stack
        s = Stack()
        s.push(start)
        visited = []
        while True:
            try:
                current = s.pop()
            except IndexError:
                return visited
            if current not in visited:
                visited.append(current)
                for neighbor in current.neighbors():
                    s.push(neighbor)
