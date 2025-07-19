# /*
#  * This is an implementation of Breadth First Search (BFS) on a graph.
#  * You may modify and submit this code if you'd like.
#  */

from collections import deque

class BreadthFirstSearch:
    def __init__(self, graph_to_search):
        self.marked = set()
        self.graph = graph_to_search

    def bfs(self, start, element_to_find):
        if not self.graph.contains_node(start):
            return False
        if start.get_element() == element_to_find:
            return True

        to_explore = deque()
        self.marked.add(start)
        to_explore.append(start)

        while to_explore:
            current = to_explore.popleft()
            for neighbor in self.graph.get_node_neighbors(current):
                if neighbor not in self.marked:
                    if neighbor.get_element() == element_to_find:
                        return True
                    self.marked.add(neighbor)
                    to_explore.append(neighbor)
        return False
