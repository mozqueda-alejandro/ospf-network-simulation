from Link import *
from Node import *
import random


class WeightedGraph:
    def __init__(self):
        self.nodes = {}  # key: node_id, value: Node object

    def add_node(self, node_id, node_failure_probability):
        self.nodes[node_id] = Node(node_id, node_failure_probability)

    def remove_node(self, node_id):
        node = self.nodes[node_id]
        for neighbor in node.neighbors:
            self.nodes[neighbor].remove_neighbor(node_id)
        del self.nodes[node_id]

    def add_edge(self, node1_id, node2_id, weight, link_failure_probability):
        node1 = self.nodes[node1_id]
        node2 = self.nodes[node2_id]
        link = Link(weight, link_failure_probability)
        node1.add_neighbor(node2_id, link)
        node2.add_neighbor(node1_id, link)

    def remove_edge(self, node1_id, node2_id):
        node1 = self.nodes[node1_id]
        node2 = self.nodes[node2_id]
        node1.remove_neighbor(node2_id)
        node2.remove_neighbor(node1_id)

    def get_neighbors(self, node_id):
        return self.nodes[node_id].neighbors

    def simulate_node_failure(self, time):
        """
        Simulates a node failure for every node in the graph.
        Generates a random failure threshold for each node and compares it to the node's failure probability.
        If the node's failure probability is greater than the failure threshold, the node is removed from the graph.
        """
        with open('file.txt', 'a') as file:
            file.write(f'{time}s :Simulating node failure...\n')
            to_remove = []
            for node in self.nodes.values():
                failure_threshold = random.random()
                if failure_threshold <= node.node_failure_probability:
                    file.write(f'Node {node.id} failed\n')
                    to_remove.append(node.id)
            for node_id in to_remove:
                self.remove_node(node_id)

        if

    def simulate_link_failure(self):
        """
        Simulates a link failure for every link in the graph.
        Generates a random failure threshold for each link and compares it to the link's failure probability.
        If the link's failure probability is greater than the failure threshold, the link is removed from the graph.
        """
        print("Simulating link failure...")
        temp = self.nodes.copy()

    def __str__(self):
        for node in self.nodes.values():
            print(node)
            for neighbor in node.neighbors:
                print(f'    {neighbor} - {node.neighbors[neighbor]}')
