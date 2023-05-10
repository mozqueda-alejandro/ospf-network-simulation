import random
from Node import *
from queue import Queue


class WeightedGraph:
    counter = 0

    def __init__(self):
        self.nodes = {}  # key: node_id, value: Node object

        self.faulty_nodes = {}  # key: node_id, value: time spent in faulty state
        self.faulty_links = {}  # key: (node1_id, node2_id), value: time spent in faulty state

    def add_node(self, node: Node) -> None:
        self.nodes[node.get_id()] = node

    def remove_node(self, node_id: str) -> None:
        node = self.nodes[node_id]
        for neighbor in node.get_neighbors().keys():
            neighbor_id = neighbor.get_id()
            self.nodes[neighbor_id].remove_neighbor(node)
        del self.nodes[node_id]

    def add_edge(self, node1, node2, weight, link_failure_probability):
        node1 = self.nodes[node1.get_id()]
        node2 = self.nodes[node2.get_id()]
        link = Link(weight, link_failure_probability)
        node1.add_neighbor(node2, link)
        node2.add_neighbor(node1, link)

    def remove_edge(self, node1_id, node2_id):
        # node1 = self.nodes[node1_id]
        # node2 = self.nodes[node2_id]
        # node1.remove_neighbor(node2)
        # node2.remove_neighbor(node1)
        # Set the link status of the link between node1 and node2 to False
        node1 = self.nodes[node1_id]
        node2 = self.nodes[node2_id]
        node1.neighbors[node2].link_status = False
        node2.neighbors[node1].link_status = False

    def get_nodes(self) -> dict:
        return self.nodes

    def get_active_nodes(self) -> dict:
        active_nodes = {}
        for node_id, node in self.nodes.items():
            if node.node_status:
                active_nodes[node_id] = node
        return active_nodes

    def get_node(self, node_id):
        return self.nodes[node_id]

    def restore_nodes(self):
        for node_id, time in self.faulty_nodes.items():
            if time == Node.node_restore_time:
                self.nodes[node_id].node_status = True
                del self.faulty_nodes[node_id]
                print(f"\tNODE {node_id} RESTORED")
            else:
                self.faulty_nodes[node_id] += 1

    def restore_links(self):
        for link_ids, time in self.faulty_links.items():
            if time == Link.link_restore_time:
                node1_id, node2_id = link_ids
                self.nodes[node1_id].neighbors[self.nodes[node2_id]].link_status = True
                self.nodes[node2_id].neighbors[self.nodes[node1_id]].link_status = True
                del self.faulty_links[link_ids]
                print(f"\tLINK {node1_id} - {node2_id} RESTORED")
            else:
                self.faulty_links[link_ids] += 1

    def simulate_node_failure(self, time) -> int:
        # Restore nodes that have been in a faulty state for Node.node_restore_time
        # self.restore_nodes()

        nodes = self.get_active_nodes()
        node_removed = 0  # int representing if a node was removed, not removed, or no nodes in graph
        if len(nodes) == 0:
            node_removed = -1
            return node_removed

        # print(f'{time:.0f}s : Node failure sim{"." * (WeightedGraph.counter % 4 + 1)}')

        to_remove = []
        for node_id, node in nodes.items():
            failure_threshold = random.random()
            if failure_threshold <= node.node_failure_probability:
                print(f'\tNODE {node_id} FAILED - fProb= {node.node_failure_probability:.2f} >= fThresh= {failure_threshold:.2f}')
                to_remove.append(node_id)
                node_removed = 1
        for node_id in to_remove:
            self.nodes[node_id].node_status = False
            if node_id not in self.faulty_nodes:
                self.faulty_nodes[node_id] = 0

        return node_removed

    def simulate_link_failure(self, time):
        # Restore links that have been in a faulty state for Link.link_restore_time
        # self.restore_links()

        # print(f'{time:.1f}s : Link failure sim{"." * (WeightedGraph.counter % 4 + 1)}')

        links_exist = False
        to_remove = []
        for node in self.get_active_nodes().values():
            for neighbor, link in node.get_neighbors().items():
                # Check if link is active
                if not link.get_status():
                    continue

                # Check if neighbor is active
                if not neighbor.get_status():
                    continue

                links_exist = True
                if neighbor > node:  # to avoid processing duplicate links
                    failure_threshold = random.random()
                    if failure_threshold <= link.link_failure_probability:
                        print(f'\tLINK {node.get_id()} - {neighbor.get_id()} FAILED - Failure Probability= {link.link_failure_probability:.2f} >= Failure Threshold= {failure_threshold:.2f}')
                        to_remove.append((node.get_id(), neighbor.get_id()))

        for node_id, neighbor_id in to_remove:
            self.remove_edge(node_id, neighbor_id)
            if (node_id, neighbor_id) not in self.faulty_links and (neighbor_id, node_id) not in self.faulty_links:
                self.faulty_links[(node_id, neighbor_id)] = 0

        return -1 if not links_exist else len(to_remove)

    def __str__(self):
        for node in self.nodes.values():
            print(node)
            for neighbor in node.neighbors:
                print(f'    {neighbor} - {node.neighbors[neighbor]}')
