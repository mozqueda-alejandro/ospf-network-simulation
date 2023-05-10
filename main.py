import concurrent.futures
import time

from dijkstra import dijkstra
from Node import Node
from WeightedGraph import WeightedGraph


start_time = time.monotonic()
graph = WeightedGraph()


def main():
    # Create nodes
    node_1 = Node("1", 0.0)
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
    graph.add_edge(node_1, node_3, 1, 0.025)
    graph.add_edge(node_2, node_3, 3, 0.025)
    graph.add_edge(node_2, node_4, 2, 0.025)
    graph.add_edge(node_2, node_5, 8, 0.025)
    graph.add_edge(node_3, node_5, 1, 0.025)
    graph.add_edge(node_3, node_7, 4, 0.025)
    graph.add_edge(node_4, node_6, 1, 0.025)
    graph.add_edge(node_4, node_8, 4, 0.025)
    graph.add_edge(node_5, node_7, 2, 0.025)
    graph.add_edge(node_6, node_7, 4, 0.025)
    graph.add_edge(node_6, node_8, 7, 0.025)
    graph.add_edge(node_7, node_9, 3, 0.025)
    graph.add_edge(node_7, node_10, 5, 0.025)
    graph.add_edge(node_8, node_10, 2, 0.025)
    graph.add_edge(node_9, node_10, 1, 0.025)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(run_timer, 1, node_1)


def get_elapsed_time():
    return time.monotonic() - start_time


def run_timer(interval, selected_node):
    if graph.counter == 0:
        distances, shortest_paths = dijkstra(graph, selected_node)
        for destination_node_id, path in shortest_paths.items():
            path_str = ' -> '.join([str(node) for node in path])
            print(f"Path: {path_str} Cost: {distances[destination_node_id]:.2f}")

    while True:
        print('-' * 103)
        node_flag = graph.simulate_node_failure(get_elapsed_time())
        link_flag = graph.simulate_link_failure(get_elapsed_time())

        # Not enough nodes or links to continue the simulation
        if node_flag == -1 and link_flag == -1:
            print('Simulation complete.')
            return

        # Either a node or link or both were removed
        if node_flag >= 1 or link_flag >= 1:
            distances, shortest_paths = dijkstra(graph, selected_node)
            for destination_node_id, path in shortest_paths.items():
                path_str = ' -> '.join([str(node) for node in path])
                print(f"Path: {path_str} Cost: {distances[destination_node_id]:.2f}")
        else:
            print(f'{get_elapsed_time(): 0.1f}s - No change')

        time.sleep(interval)


if __name__ == '__main__':
    with open('file.txt', 'w') as f:
        f.truncate(0)
    main()
