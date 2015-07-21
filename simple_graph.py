# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import heapq


class Graph(object):

    def __init__(self):
        """Create a new empty graph."""
        self.gdict = {}

    def nodes(self):
        """Return a list of nodes in the graph."""
        return self.gdict.keys()

    def edges(self):
        """Return a list of edges in the graph."""
        self._edges = []
        for node in self.gdict:
            for end in self.gdict[node]:
                self._edges.append((node, end, self.gdict[node][end]))
        return self._edges

    def add_node(self, n):
        """Add a node n into the graph.
        Nodes must be hashable."""
        self.gdict.setdefault(n, {})

    def add_edge(self, n1, n2, weight):
        """Add an edge connecting n1 and n2 to the graph with specified weight."""
        self.gdict.setdefault(n2, {})
        try:
            self.gdict[n1][n2] = weight
        except KeyError:
            self.gdict[n1] = {n2: weight}

    def del_node(self, n):
        """Delete node n from the graph."""
        try:
            del self.gdict[n]
        except KeyError:
            raise KeyError('{} not in the graph.'.format(n))
        for nodedict in self.gdict.values():
            try:
                del nodedict[n]
            except KeyError:
                continue

    def del_edge(self, n1, n2):
        """Delete the edge connecting n1 and n2 from the graph."""
        try:
            del self.gdict[n1][n2]
        except (KeyError, ValueError):
            raise ValueError('Edge {}, {} not in the graph.'.format(n1, n2))

    def has_node(self, n):
        """Return True if n is in the graph, else False."""
        return n in self.gdict

    def neighbors(self, n):
        """Return the list of nodes n is pointing to."""
        try:
            return self.gdict[n].keys()
        except KeyError:
            raise KeyError('{} not in the graph.'.format(n))

    def adjacent(self, n1, n2):
        """Return True if there is an edge connecting n1 and n2, else False."""
        if n1 not in self.gdict or n2 not in self.gdict:
            raise KeyError('One of these nodes is not in the graph.')
        return n2 in self.gdict[n1]

    def depth_first_traversal(self, start):
        """Perform a depth first traversal on a graph starting at the given node"""
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
                for neighbor in self.neighbors(current):
                    s.push(neighbor)

    def breadth_first_traversal(self, start):
        """Perform a breadth first traversal on a graph starting at the given node"""
        from queue import Queue
        q = Queue()
        q.enqueue(start)
        visited = [start]
        while q.size() > 0:
            current = q.dequeue()
            for neighbor in self.neighbors(current):
                if neighbor not in visited:
                    q.enqueue(neighbor)
                    visited.append(neighbor)
        return visited

    def dijkstras_algorithm(self, source):
        dist = {}
        prev = {}
        pq = []

        for node in self.nodes():
            dist[node] = float('inf')
            prev[node] = None

        dist[source] = 0
        heapq.heappush(pq, (0, source))

        while pq:
            distance, node = heapq.heappop(pq)
            for neighbor in self.neighbors(node):
                alt_dist = distance + self.gdict[node][neighbor]
                if alt_dist < dist[neighbor]:
                    dist[neighbor] = alt_dist
                    prev[neighbor] = node
                    heapq.heappush(pq, (alt_dist, neighbor))

        return dist, prev

    def bellman_ford(self, source):
        dist = {}
        prev = {}

        for node in self.nodes():
            dist[node] = float('inf')
            prev[node] = None
        dist[source] = 0

        for node in self.nodes():
            for n1, n2, weight in self.edges():
                if dist[n1] + weight < dist[n2]:
                    dist[n2] = dist[n1] + weight
                    prev[n2] = n1

        for n1, n2, weight in self.edges():
            if dist[n1] + weight < dist[n2]:
                raise ValueError('Graph contains a negative-weight cycle')
        return dist, prev


if __name__ == '__main__':
    from random import randint
    from timeit import Timer
    graph1 = Graph()
    for i in range(500):
        graph1.add_node(i)
    for i in range(750):
        graph1.add_edge(randint(1, 499), randint(1, 499), randint(1, 50))
    print ('Depth First Traversal of random graph with 500 elements and '
           '750 edges, run 1000 times.')
    print Timer('graph1.depth_first_traversal(50)',
                'from __main__ import graph1').timeit(1000)
    print ('Breadth First Traversal of the same graph, performed 1000 times.')
    print Timer('graph1.breadth_first_traversal(50)',
                'from __main__ import graph1').timeit(1000)
