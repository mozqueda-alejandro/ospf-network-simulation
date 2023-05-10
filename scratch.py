import heapq
from queue import Queue

# 1. Set the distance to the start node to 0 and all other distances to infinity.
# 2. Create a priority queue and add the start node with distance 0 to the queue.
# 3. While the priority queue is not empty:
#       a. Pop the node with the smallest distance from the priority queue. This will be the current node.
#       b. For each neighbor of the current node:
#             i. Calculate the distance from the start node to the neighbor through the current node.
#             ii. If the calculated distance is less than the
#             current known distance to the neighbor, update the distance.
#             iii. Add the neighbor to the priority queue with its updated distance.
# 4. When all nodes have been visited, the distances dictionary
# contains the shortest distance to each node from the start node.



def bfs(graph, start_node):
    visited = set()
    q = Queue()

    q.put(start_node)
    visited.add(start_node)

    while not q.empty():
        current_node = q.get()
        print(current_node.id)

        for neighbor_id, weight in current_node.neighbors.items():
            neighbor_node = graph[neighbor_id]
            if neighbor_node not in visited:
                visited.add(neighbor_node)
                q.put(neighbor_node)

# WORKING BREADTH FIRST SEARCH
# links = []
#         visited = set()
#         q = Queue()
#
#         q.put(start_node)
#         visited.add(start_node)
#
#         while not q.empty():
#             current_node = q.get()
#             print(current_node.id)
#
#             for neighbor, link in current_node.get_neighbors().items():
#                 if neighbor not in visited:
#                     visited.add(neighbor)
#                     q.put(neighbor)

# WORKING CODE
# def dijkstra(graph: WeightedGraph, source: Node):
#     nodes = graph.get_nodes()
#     distances = {}  # key: node_id, value: distance from source
#     for node_id in nodes.keys():
#         distances[node_id] = float('inf')
#     distances[source.get_id()] = 0
#     heap = [(distances[source.get_id()], source)]
#     heapq.heapify(heap)
#
#     while len(heap) > 0:
#         curr_dist, curr_node = heapq.heappop(heap)
#         if curr_dist > distances[curr_node.get_id()]:
#             continue
#         # For each neighbor of the current node
#         for neighbor, link in (graph.get_neighbors(curr_node.get_id())).items():
#             # Calculate the distance to the neighbor through the current node
#             dist = curr_dist + link.cost
#
#             # If the distance to the neighbor is less than the current known distance,
#             # update the distance and add the neighbor to the priority queue
#             if dist < distances[neighbor.get_id()]:
#                 distances[neighbor.get_id()] = dist
#                 heapq.heappush(heap, (dist, neighbor))
#     return distances

    # graph = WeightedGraph()
    # node_a = Node("A", 0.0)
    #
    # # Create nodes
    # node_b = Node("B", 0.075)
    # node_c = Node("C", 0.05)
    # node_d = Node("D", 0.0875)
    # node_e = Node("E", 0.1)
    #
    # # Add nodes to graph
    # graph.add_node(node_a)
    # graph.add_node(node_b)
    # graph.add_node(node_c)
    # graph.add_node(node_d)
    # graph.add_node(node_e)
    #
    # # Add edges to graph
    # graph.add_edge(node_a, node_b, 5, 0.0625)
    # graph.add_edge(node_a, node_c, 3, 0.0575)
    # graph.add_edge(node_b, node_c, 1, 0.05)
    # graph.add_edge(node_b, node_d, 2, 0.075)
    # graph.add_edge(node_c, node_d, 4, 0.125)
    # graph.add_edge(node_d, node_e, 6, 0.0425)

        """
        Simulates a link failure for every link in the graph.
        Generates a random failure threshold for each link and compares it to the link's failure probability.
        If the link's failure probability is greater than the failure threshold, the link is removed from the graph.
        """
