from abc import ABC, abstractmethod
from collections import defaultdict
from Edge import Edge
from Node import Node

class Graph(ABC):
    def __init__(self):
        self.adjacency_sets = defaultdict(set)  # type: dict[Node, set[Edge]]
        self.element_to_node = {}              # type: dict[str, Node]
        self.num_nodes = 0
        self.num_edges = 0

    @abstractmethod
    def add_edge(self, node1, node2):
        pass

    @abstractmethod
    def remove_edge(self, node1, node2):
        pass

    def add_node(self, new_node):
        if new_node is None or self.contains_node(new_node):
            return False
        self.adjacency_sets[new_node] = set()
        self.element_to_node[new_node.get_element()] = new_node
        self.num_nodes += 1
        return True

    def get_node_neighbors(self, node):
        if not self.contains_node(node):
            return None
        return {edge.get_destination() for edge in self.adjacency_sets[node]}

    def add_edge_from_to(self, source, destination):
        new_edge = Edge(source, destination)
        if new_edge not in self.adjacency_sets[source]:
            self.adjacency_sets[source].add(new_edge)
            return True
        return False

    def remove_edge_from_to(self, source, destination):
        to_remove = Edge(source, destination)
        if to_remove in self.adjacency_sets[source]:
            self.adjacency_sets[source].remove(to_remove)
            return True
        return False

    def get_num_nodes(self):
        return self.num_nodes

    def get_num_edges(self):
        return self.num_edges

    def get_starting_node(self):
        return next(iter(self.adjacency_sets), None)

    def get_all_nodes(self):
        return set(self.adjacency_sets.keys())

    def get_node_edges(self, node):
        if not self.contains_node(node):
            return None
        return self.adjacency_sets[node]

    def contains_node(self, node):
        return node in self.adjacency_sets

    def get_node(self, element):
        if element not in self.element_to_node:
            new_node = Node(element)
            self.element_to_node[element] = new_node
        return self.element_to_node[element]

    def contains_element(self, element):
        return element in self.element_to_node
