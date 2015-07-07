# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Graph(object):

    def __init__(self):
        self.gdict = {}

    def nodes(self):
        return self.gdict.keys()

    def edges(self):
        self.edges = []
        for node in self.gdict:
            for end in self.gdict[node]:
                self.edges.append((node, end))
        return self.edges

    def add_node(self, n):
        self.gdict.setdefault(n, [])

    def add_edge(self, n1, n2):
        self.gdict[n1].setdefault(n2, [])
        try:
            self.gdict[n1].append(n2)
        except KeyError:
            self.gdict[n1] = [n2]

    def del_node(self, n):
        try:
            del self.gdict[n1]
        except KeyError:
            raise KeyError('{} not in the graph.'.format(n1))
        for nodelist in self.gdit.values():
            try:
                nodelist.remove(n)
            except ValueError:
                continue

    def del_edge(self, n1, n2):
        try:
            self.gdict[n1].remove[n2]
        except KeyError, ValueError:
            raise ValueError('Edge {}, {} not in the graph.'.format(n1, n2))

    def has_node(self, n):
        return n in self.gdict

    def neighbors(self, n):
        try:
            return self.gdict[n]
        except KeyError:
            raise KeyError('{} not in the graph.'.format(n1))

    def adjacent(self, n1, n2):
        if n1 not in self.dict or n2 not in self.gdict:
            raise KeyError('One of these nodes is not in the graph.')
        return n2 in self.gdict[n1]
