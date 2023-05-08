import concurrent.futures
import heapq
import threading
import time
from WeightedGraph import WeightedGraph

import queue
import subprocess
import sys

start_time = time.monotonic()

graph = WeightedGraph()


def main():
    # Add some nodes
    graph.add_node("A", 0.15)
    graph.add_node("B", 0.2)
    graph.add_node("C", 0.05)
    graph.add_node("D", 0.0875)
    graph.add_node("E", 0.1)

    # Add some edges
    graph.add_edge("A", "B", 5, 0.1)
    graph.add_edge("A", "C", 3, 0.2)
    graph.add_edge("B", "C", 1, 0.05)
    graph.add_edge("B", "D", 2, 0.1)
    graph.add_edge("C", "D", 4, 0.3)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(run_timer(1))


def print_elapsed_time():
    elapsed_time = time.monotonic() - start_time
    print(f"Elapsed time: {elapsed_time:.1f} seconds")


def run_timer(interval):
    while True:
        graph.simulate_node_failure(time.monotonic() - start_time)
        time.sleep(interval)


if __name__ == '__main__':
    with open('file.txt', 'w') as f:
        f.truncate(0)

    main()
