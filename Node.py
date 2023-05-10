from __future__ import annotations
from Link import *


class Node:
    static_counter = 0
    node_repair_

    def __init__(self, node_id: str, node_failure_probability: float) -> None:
        self.id = node_id
        self.neighbors = {}  # {Node object: Link object}
        self.node_failure_probability = node_failure_probability
        self.local_counter = Node.static_counter
        Node.static_counter += 1

    def add_neighbor(self, neighbor: Node, link: Link) -> None:
        self.neighbors[neighbor] = link

    def remove_neighbor(self, neighbor: Node) -> None:
        del self.neighbors[neighbor]

    def get_id(self) -> str:
        return self.id

    def get_neighbors(self) -> dict:
        return self.neighbors

    def __repr__(self):
        return f'Node {self.id}'

    def __str__(self)  -> str:
        return f'Node {self.id}'

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return isinstance(other, Node) and self.id == other.id

    def __gt__(self, other):
        return self.id > other.id
