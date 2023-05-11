import concurrent.futures
import time

from dijkstra import dijkstra
from Node import Node
from WeightedGraph import WeightedGraph

import matplotlib.pyplot as plt
import networkx as nx

start_time = time.monotonic()
graph = WeightedGraph()


def main():
    # Create nodes
    node_1 = Node("1", 0.0)
    node_2 = Node("2", 0.02)
    node_3 = Node("3", 0.02)
    node_4 = Node("4", 0.02)
    node_5 = Node("5", 0.02)
    node_6 = Node("6", 0.02)
    node_7 = Node("7", 0.02)
    node_8 = Node("8", 0.02)
    node_9 = Node("9", 0.02)
    node_10 = Node("10", 0.02)

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
    graph.add_edge(node_1, node_3, 1, 0.01)
    graph.add_edge(node_2, node_3, 3, 0.01)
    graph.add_edge(node_2, node_4, 2, 0.01)
    graph.add_edge(node_2, node_5, 8, 0.01)
    graph.add_edge(node_3, node_5, 1, 0.01)
    graph.add_edge(node_3, node_7, 4, 0.01)
    graph.add_edge(node_4, node_6, 1, 0.01)
    graph.add_edge(node_4, node_8, 4, 0.01)
    graph.add_edge(node_5, node_7, 2, 0.01)
    graph.add_edge(node_6, node_7, 4, 0.01)
    graph.add_edge(node_6, node_8, 7, 0.01)
    graph.add_edge(node_7, node_9, 3, 0.01)
    graph.add_edge(node_7, node_10, 5, 0.01)
    graph.add_edge(node_8, node_10, 2, 0.01)
    graph.add_edge(node_9, node_10, 1, 0.01)

    G = nx.Graph()
    G.add_edge(node_1, node_2, weight=5)
    G.add_edge(node_1, node_3, weight=1)
    G.add_edge(node_2, node_3, weight=3)
    G.add_edge(node_2, node_4, weight=2)
    G.add_edge(node_2, node_5, weight=8)
    G.add_edge(node_3, node_5, weight=1)
    G.add_edge(node_3, node_7, weight=4)
    G.add_edge(node_4, node_6, weight=1)
    G.add_edge(node_4, node_8, weight=4)
    G.add_edge(node_5, node_7, weight=2)
    G.add_edge(node_6, node_7, weight=4)
    G.add_edge(node_6, node_8, weight=7)
    G.add_edge(node_7, node_9, weight=3)
    G.add_edge(node_7, node_10, weight=5)
    G.add_edge(node_8, node_10, weight=2)
    G.add_edge(node_9, node_10, weight=1)

    # Map node id to new node names
    mapping = {node_1: '1', node_2: '2', node_3: '3', node_4: '4', node_5: '5', node_6: '6', node_7: '7', node_8: '8', node_9: '9', node_10: '10'}
    G = nx.relabel_nodes(G, mapping)

    # Add coordinates to the nodes
    pos = {'1': (0, 5), '2': (4, 8), '3': (4, 2), '4': (9, 8), '5': (9, 4), '6': (14, 8), '7': (14, 2), '8': (17, 10), '9': (19, 2), '10': (21, 6)}
    nx.set_node_attributes(G, pos, 'coord')

    elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
    esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 0.5]
    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=600)

    # edges
    nx.draw_networkx_edges(G, pos, edgelist=elarge, width=3)
    nx.draw_networkx_edges(
        G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed"
    )

    # node labels
    nx.draw_networkx_labels(G, pos, font_size=18, font_family="sans-serif")
    # edge weight labels
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=18)

    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.show()

    with open('log_file.txt', 'w') as f:
        f.truncate(0)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(run_timer, 1, node_1)


def get_elapsed_time():
    return time.monotonic() - start_time


def run_timer(interval, selected_node):
    with open('log_file.txt', 'w') as log_file:
        pass
    if graph.counter == 0:
        distances, shortest_paths = dijkstra(graph, selected_node)
        for destination_node_id, path in shortest_paths.items():
            path_str = ' -> '.join([str(node) for node in path])
            print(f"Path: {path_str:38s} Cost: {distances[destination_node_id]:3.2f}")

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
                print(f"Path: {path_str:38s} Cost: {distances[destination_node_id]:3.2f}")
        else:
            print(f'{get_elapsed_time(): 0.1f}s - No change')

        time.sleep(.5)


if __name__ == '__main__':
    main()
    # G = nx.Graph()
    #
    # G.add_edge('1', '2', weight=5)
    # G.add_edge('1', '3', weight=1)
    # G.add_edge('2', '3', weight=3)
    # G.add_edge('2', '4', weight=2)
    # G.add_edge('2', '5', weight=8)
    # G.add_edge('3', '5', weight=1)
    # G.add_edge('3', '7', weight=4)
    # G.add_edge('4', '6', weight=1)
    # G.add_edge('4', '8', weight=4)
    # G.add_edge('5', '7', weight=2)
    # G.add_edge('6', '7', weight=4)
    # G.add_edge('6', '8', weight=7)
    # G.add_edge('7', '9', weight=3)
    # G.add_edge('7', '10', weight=5)
    # G.add_edge('8', '10', weight=2)
    # G.add_edge('9', '10', weight=1)
    #
    # # Add coordinates to the nodes
    # pos = {'1': (0, 5), '2': (4, 8), '3': (4, 2), '4': (9, 8), '5': (9, 4), '6': (14, 8), '7': (14, 2), '8': (17, 10), '9': (19, 2), '10': (21, 6)}
    # nx.set_node_attributes(G, pos, 'coord')
    #
    # elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
    # esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 0.5]
    # # nodes
    # nx.draw_networkx_nodes(G, pos, node_size=600)
    #
    # # edges
    # nx.draw_networkx_edges(G, pos, edgelist=elarge, width=3)
    # nx.draw_networkx_edges(
    #     G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed"
    # )
    #
    # # node labels
    # nx.draw_networkx_labels(G, pos, font_size=18, font_family="sans-serif")
    # # edge weight labels
    # edge_labels = nx.get_edge_attributes(G, "weight")
    # nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=18)
    #
    # ax = plt.gca()
    # ax.margins(0.08)
    # plt.axis("off")
    # plt.tight_layout()
    # plt.show()
