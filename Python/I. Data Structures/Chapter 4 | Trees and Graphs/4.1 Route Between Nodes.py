"""
4.1 Route Between Nodes.

Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.
"""
from enum import Enum

State = Enum('State', 'Unvisited Visited Visiting')


class Graph:
    """Class that represents a graph."""

    def __init__(self):
        """Init method."""
        self.nodes = []


class Node:
    """Class that represents a node."""

    def __init__(self, name):
        """Init method."""
        self.name = name
        self.children = []


class Queue(list):
    """Queue class."""

    def __init__(self):
        """Init method."""
        super()

    def enqueue(self, item):
        """Add a item to the end of queue."""
        super().append(item)

    def dequeue(self):
        """Remove item from front of the queue."""
        if self.is_empty():
            return None
        item = self[0]
        del self[0]
        return item

    def is_empty(self):
        """Check if queue is empty."""
        if len(self) == 0:
            return True
        return False


def route_between_nodes(g, start, end):
    """Find route between nodes."""
    if start == end:
        return True

    queue = Queue()

    for u in g.nodes:
        g.state = State.Unvisited

    start.state = State.Visiting
    queue.enqueue(g)
    while not queue.is_empty():
        r = queue.dequeue()
        if r is not None:
            for n in r.children:
                if n.state == State.Unvisited:
                    if n == end:
                        return True
                    else:
                        n.state = State.Visiting
                        queue.enqueue(n)
            r.state = State.Visited
    return False
