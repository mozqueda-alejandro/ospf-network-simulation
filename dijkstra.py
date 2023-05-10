import heapq

from Node import Node
from WeightedGraph import WeightedGraph


def dijkstra(graph: WeightedGraph, source: Node):
    nodes = graph.get_active_nodes()
    distances = {}  # key: node_id, value: distance from source
    paths = {source.get_id(): [source.get_id()]}

    # Initialize distances from the source to all other nodes to infinity
    for node_id in nodes.keys():
        distances[node_id] = float('inf')

    # Initialize the distance from the source to itself to 0
    source_id = source.get_id()
    distances[source_id] = 0
    heap = [(distances[source_id], source)]
    heapq.heapify(heap)

    # While the priority queue is not empty
    while len(heap) > 0:
        curr_dist, curr_node = heapq.heappop(heap)

        # If the distance to the current node is greater than the current known distance,
        # skip the current node
        if curr_dist > distances[curr_node.get_id()]:
            continue

        for neighbor, link in (curr_node.get_neighbors()).items():
            # Check if link is active
            if not link.get_status():
                continue

            # Check if neighbor is active
            if not neighbor.get_status():
                continue

            # Calculate the distance to the neighbor through the current node
            dist = curr_dist + link.get_cost()

            # If the distance to the neighbor is less than the current known distance,
            # update the distance and add the neighbor to the priority queue
            if dist < distances[neighbor.get_id()]:
                distances[neighbor.get_id()] = dist
                heapq.heappush(heap, (dist, neighbor))

                # Update the path to the neighbor
                paths[neighbor.get_id()] = paths[curr_node.get_id()] + [neighbor.get_id()]
    return distances, paths
