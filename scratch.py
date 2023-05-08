import heapq
from queue import Queue


def dijkstra(graph, start):
    # Initialize distances to all nodes as infinity, except for start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Create a priority queue to store the next nodes to be visited
    pq = [(0, start)]

    # While there are still nodes to visit
    while pq:
        # Get the node with the smallest distance from start
        curr_dist, curr_node = heapq.heappop(pq)

        # If we have already visited this node, continue to the next one
        if curr_dist > distances[curr_node]:
            continue

        # For each neighbor of the current node
        for neighbor, weight in graph[curr_node].items():
            # Calculate the distance to the neighbor through the current node
            dist = curr_dist + weight

            # If the distance to the neighbor is less than the current known distance,
            # update the distance and add the neighbor to the priority queue
            if dist < distances[neighbor]:
                distances[neighbor] = dist
                heapq.heappush(pq, (dist, neighbor))

    return distances


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
