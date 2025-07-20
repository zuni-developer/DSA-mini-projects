# /*
#  * This is an implementation of Depth First Search (DFS) on a graph.
#  * You may modify and submit this code if you'd like.
#  */

class DepthFirstSearch:
    def __init__(self, graph_to_search):
        self.marked = set()
        self.graph = graph_to_search

    def dfs(self, start, element_to_find):
        if not self.graph.contains_node(start):
            return False

        if start.get_element() == element_to_find:
            return True
        else:
            self.marked.add(start)
            for neighbor in self.graph.get_node_neighbors(start):
                if neighbor not in self.marked and self.dfs(neighbor, element_to_find):
                    return True
            return False
