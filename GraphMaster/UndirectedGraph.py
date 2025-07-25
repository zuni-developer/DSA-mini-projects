from Graph import Graph

class UndirectedGraph(Graph):
    def __init__(self):
        super().__init__()

    def add_edge(self, node1, node2):
        self.add_node(node1)  # only adds if not already in graph
        self.add_node(node2)
        add_edge_success = (
            self.add_edge_from_to(node1, node2) and
            self.add_edge_from_to(node2, node1)
        )
        if add_edge_success:
            self.num_edges += 1
        return add_edge_success

    def remove_edge(self, node1, node2):
        if not self.contains_node(node1) or not self.contains_node(node2):
            return False
        remove_edge_success = (
            self.remove_edge_from_to(node1, node2) and
            self.remove_edge_from_to(node2, node1)
        )
        if remove_edge_success:
            self.num_edges -= 1
        return remove_edge_success
