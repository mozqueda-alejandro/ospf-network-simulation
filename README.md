# Dynamic Routing Mechanism Design in Faulty Network

Created by: Rubi Dionisio and Alejandro Mozqueda

CPE 400 Spring 2023 at University of Nevada, Reno

## Project Description

This project is meant to simulate a mesh network in which nodes and links may fail intermittently. Each node and link will have a certain probability to fail, when a fail does occur, the network must re-route to avoid the faulty link/node.

This is the description for the UNR class CPE 400 project labeled as Dynamic Routing Mechanism Design in Faulty Network.

## Default 10-node graph

The following graph was used to run the simulation and was generated in the program with the NetworkX graphical library
## ![default_topology](https://github.com/mozqueda-alejandro/ospf_network_simulation/assets/89401406/a29aaa48-7db7-4a1d-ad8d-09fc2f5cb4d9)

## Resources

``` 
python3
```

## How to run

In the terminal type in:

```
python3 main.py
```

## Functions and Classes

```
class Link:
    Attributes:
        counter – used to give each link a unique ID.
        link_restore_time  – the number of cycles needed before a faulty link is brought back online. 
        link_ID – the ID of a link, specified by the counter.
        cost – the cost of the link.
        link_failure_probability – the probability of that link to fail.
        link_status – true if link is active, false otherwise.
    Description:
        This class is used represent nodes (routers) being linked together.
```

```
class Node:
    Attributes:
        static_counter – used to keep track of nodes.
        node_restore_time – the number of cycles needed before a faulty node is brought back online.
        id – node’s ID.
        neightbors – dictionary storing the node’s neighbors.
        node_failure_probability – probability of the node failing.
        node_status – true if node is active, otherwise false.
        local_counter – determined by the static counter to keep track of nodes.
    Description:
        This class represents routers that are going to be connected using the link class.
```

```
class Weighted Graph:
    Attributes:
        nodes – dictionary that holds the node ID and corresponding node object.
        adjacency_matrix – dictionary that holds node ID and its list of neighbors
    Description:
        This class represents a network of routers (nodes) and links connecting each router together.
```
```
function Dijkstra:
    Runs the Dijkstra algorithm that is called from main.
```
