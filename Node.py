

class Node:
    def __init__(self, node_id, node_failure_probability=0.0):
        self.id = node_id
        self.neighbors = {}  # key: neighbor_id, value: link
        self.node_failure_probability = node_failure_probability

    def add_neighbor(self, neighbor_id, link):
        self.neighbors[neighbor_id] = link

    def remove_neighbor(self, neighbor_id):
        del self.neighbors[neighbor_id]

    def __str__(self):
        return f'Node {self.id}'
