from Graph import Graph

class DirectedGraph(Graph):
    def __init__(self):
        super().__init__()

    def add_edge(self, source, destination):
        self.add_node(source)      # only adds if not already in graph
        self.add_node(destination)
        add_edge_success = self.add_edge_from_to(source, destination)
        if add_edge_success:
            self.num_edges += 1
        return add_edge_success

    def remove_edge(self, source, destination):
        if not self.contains_node(source) or not self.contains_node(destination):
            return False
        remove_edge_success = self.remove_edge_from_to(source, destination)
        if remove_edge_success:
            self.num_edges -= 1
        return remove_edge_success
