# data-structures
A repository of basic data structures in partnership with [Saki Fu](https://github.com/SakiFu).

Linked List - a singly linked list where the data is stored in nodes. The list has a pointer to the head, and each node keeps a pointer to the next node in sequence.

Stack - a Last-In, First-Out (LIFO) structure similar to the linked list. Users can push a value onto the stack, and pop the top value off.

Queue - a First-In, First-Out (FIFO) structure with a similar basis as a linked list or a stack. Users can push a value onto one end of the queue, and pop the other end off.

Doubly Linked List - similar to the linked list, but the list contains pointers to both the front and end, and each node has a pointer to its next and previous neighbors.

One would use a singly linked list similarly to a stack; operation at the head of the list is significantly better than operation at the end. A doubly linked list is optimized for operations at either end; this can be used as either a stack or a queue, with the small overhead of a couple extra pointers.