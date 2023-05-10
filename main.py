import concurrent.futures
import heapq
import time

from Node import Node
from WeightedGraph import WeightedGraph


start_time = time.monotonic()

graph = WeightedGraph()
node_1 = Node("1", 0.0)


def main():
    # Create nodes
    node_2 = Node("2", 0.03)
    node_3 = Node("3", 0.03)
    node_4 = Node("4", 0.03)
    node_5 = Node("5", 0.03)
    node_6 = Node("6", 0.03)
    node_7 = Node("7", 0.03)
    node_8 = Node("8", 0.03)
    node_9 = Node("9", 0.03)
    node_10 = Node("10", 0.03)

    # Add nodes to graph
    graph.add_node(node_1)
    graph.add_node(node_2)
    graph.add_node(node_3)
    graph.add_node(node_4)
    graph.add_node(node_5)
    graph.add_node(node_6)
    graph.add_node(node_7)
    graph.add_node(node_8)
    graph.add_node(node_9)
    graph.add_node(node_10)

    # Add edges to graph
    graph.add_edge(node_1, node_2, 5, 0.01)
    graph.add_edge(node_1, node_3, 1, 0.04)
    graph.add_edge(node_2, node_3, 3, 0.04)
    graph.add_edge(node_2, node_4, 2, 0.04)
    graph.add_edge(node_2, node_5, 8, 0.04)
    graph.add_edge(node_3, node_5, 1, 0.04)
    graph.add_edge(node_3, node_7, 4, 0.04)
    graph.add_edge(node_4, node_6, 1, 0.04)
    graph.add_edge(node_4, node_8, 4, 0.04)
    graph.add_edge(node_5, node_7, 2, 0.04)
    graph.add_edge(node_6, node_7, 4, 0.04)
    graph.add_edge(node_6, node_8, 7, 0.04)
    graph.add_edge(node_7, node_9, 3, 0.04)
    graph.add_edge(node_7, node_10, 5, 0.02)
    graph.add_edge(node_8, node_10, 2, 0.02)
    graph.add_edge(node_9, node_10, 1, 0.02)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(run_timer, 1)

    # graph.simulate_link_failure(1)


def print_elapsed_time():
    elapsed_time = time.monotonic() - start_time
    print(f"Elapsed time: {elapsed_time:.1f} seconds")


# def run_timer(interval):
#     while True:
#         flag = graph.simulate_node_failure(time.monotonic() - start_time)
#         if flag == -1:
#             return
#         elif flag == 1:
#             shortest_paths = dijkstra(graph, node_a)
#             for node_id, distance in shortest_paths.items():
#                 print(f'\tNode A -> Node {node_id}: {distance:.2f}')
#         elif flag == 0:
#             pass  # No node failure
#         time.sleep(interval)

def run_timer(interval):
    if graph.counter == 0:
        shortest_paths = dijkstra(graph, node_1)
        for node_id, distance in shortest_paths.items():
            print(f'\tNode 1 -> Node {node_id}: {distance:.2f}')
    while True:
        node_flag = graph.simulate_node_failure(time.monotonic() - start_time)
        link_flag = graph.simulate_link_failure(time.monotonic() - start_time)
        if node_flag == -1 and link_flag == -1:
            print('Simulation complete.')
            return
        if node_flag >= 1 or link_flag >= 1:
            shortest_paths = dijkstra(graph, node_1)
            for node_id, distance in shortest_paths.items():
                print(f'\tNode 1 -> Node {node_id}: {distance:.2f}')
        time.sleep(interval)


def dijkstra(graph: WeightedGraph, source: Node):
    nodes = graph.get_nodes()
    distances = {}  # key: node_id, value: distance from source
    for node_id in nodes.keys():
        distances[node_id] = float('inf')
    distances[source.get_id()] = 0
    heap = [(distances[source.get_id()], source)]
    heapq.heapify(heap)

    while len(heap) > 0:
        curr_dist, curr_node = heapq.heappop(heap)
        if curr_dist > distances[curr_node.get_id()]:
            continue
        # For each neighbor of the current node
        for neighbor, link in (curr_node.get_neighbors()).items():
            # Calculate the distance to the neighbor through the current node
            dist = curr_dist + link.cost

            # If the distance to the neighbor is less than the current known distance,
            # update the distance and add the neighbor to the priority queue
            if dist < distances[neighbor.get_id()]:
                distances[neighbor.get_id()] = dist
                heapq.heappush(heap, (dist, neighbor))
    return distances


if __name__ == '__main__':
    with open('file.txt', 'w') as f:
        f.truncate(0)
    main()
