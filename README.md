# data-structures
A repository of basic data structures in partnership with [Saki Fu](https://github.com/SakiFu).

Linked List - a singly linked list where the data is stored in nodes. The list has a pointer to the head, and each node keeps a pointer to the next node in sequence.

Stack - a Last-In, First-Out (LIFO) structure similar to the linked list. Users can push a value onto the stack, and pop the top value off.

Queue - a First-In, First-Out (FIFO) structure with a similar basis as a linked list or a stack. Users can push a value onto one end of the queue, and pop the other end off.

Doubly Linked List - similar to the linked list, but the list contains pointers to both the front and end, and each node has a pointer to its next and previous neighbors.

One would use a singly linked list similarly to a stack; operation at the head of the list is significantly better than operation at the end. A doubly linked list is optimized for operations at either end; this can be used as either a stack or a queue, with the small overhead of a couple extra pointers.

Binary Heap - a tree where each node has two child nodes. It maintains the heap property of always having the smallest (in a min-heap) or the largest (in a max-heap) node on top.

Priority Queue - A queue where each node has a priority, and things should come off the queue sorted by priority. If the priority is the same, the queue property is maintained.  Implemented as a binary heap to reduce insertion from O(n) to O(log(n)).

Simple Graph - a directed graph where each node could be connected to any or none of the other nodes. Implemented as a Python dictionary.

Graph Traversal - added depth-first and breadth-first traversal to the simple graph, along with an ifmain function that demonstrates their performance.

Weighted Edges - added edge weights to the graph to support shortest-path finding.

[![Build Status](https://travis-ci.org/ndraper2/data-structures.svg?branch=master)](https://travis-ci.org/ndraper2/data-structures)