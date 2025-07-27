# /*
#  * Implement the methods below according to the specification in the assignment description.
#  * Please be sure not to change the signature of any of the methods!
#  */
from GraphBuilder import GraphBuilder
from BreadthFirstSearch import BreadthFirstSearch
from DepthFirstSearch import DepthFirstSearch

class GraphUtils:
    @staticmethod
    def min_distance(graph, src, dest):
        if graph is None or src is None or dest is None:
            return -1
        if not graph.contains_element(src) or not graph.contains_element(dest):
            return -1
        start=graph.get_node(src)
        visited=set()
        queue=GraphBuilder.deque()
        queue.append((start, 0))
        visited.add(start)
        while queue:
            temp=queue.popleft()
            current=temp[0]
            dist=temp[1]
            if current.get_element()==dest:
                return dist
            neighbors=graph.get_node_neighbors(current)
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor,dist+1))
        return -1

    @staticmethod
    def nodes_within_distance(graph, src, distance):
        if graph is None or src is None or distance<1:
            return None
        if not graph.contains_element(src):
            return None
        start=graph.get_node(src)
        visited=set()
        result=set()
        queue=GraphBuilder.deque()
        queue.append((start, 0))
        visited.add(start)
        while queue:
            temp=queue.popleft()
            current=temp[0]
            dist=temp[1]
            if dist<distance:
                neighbors=graph.get_node_neighbors(current)
                for neighbor in neighbors:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor,dist+1))
                        result.add(neighbor.get_element())
        return result

    @staticmethod
    def is_hamiltonian_path(graph, values):
        if graph is None or values is None:
            return False
        all_nodes=graph.get_all_nodes()
        if len(values)!=len(all_nodes):
            return False
        visited=set()
        for i in range(len(values)):
            value=values[i]
            if not graph.contains_element(value) or value in visited:
                return False
            visited.add(value)
            if i>0:
                prev_node=graph.get_node(values[i - 1])
                current_node=graph.get_node(value)
                neighbors=graph.get_node_neighbors(prev_node)
                if current_node not in neighbors:
                    return False
        return True

    # Testing method
    @staticmethod
    def main():
        filename = "graph_builder_test.txt"

        # Build Directed and Undirected Graphs
        print("Building Directed Graph:")
        directed_graph = GraphBuilder.build_directed_graph(filename)
        print(f"Directed Graph: {len(directed_graph.get_all_nodes())} nodes, {directed_graph.get_num_edges()} edges")

        print("\nBuilding Undirected Graph:")
        undirected_graph = GraphBuilder.build_undirected_graph(filename)
        print(f"Undirected Graph: {len(undirected_graph.get_all_nodes())} nodes, {undirected_graph.get_num_edges()} edges")

        # Pick some nodes for testing
        start = undirected_graph.get_node("0")
        target = "6"
        not_in_graph = "10"

        print("\nRunning Breadth First Search (BFS):")
        bfs = BreadthFirstSearch(undirected_graph)
        result = bfs.bfs(start, target)
        print(f"BFS result from 0 to {target}: {result}")

        print("\nRunning Depth First Search (DFS):")
        dfs = DepthFirstSearch(undirected_graph)
        result = dfs.dfs(start, target)
        print(f"DFS result from 0 to {target}: {result}")

        print("\nTesting isHamiltonianPath:")
        path = ["0", "1", "2", "4", "6"]
        result = GraphUtils.is_hamiltonian_path(undirected_graph, path)
        print(f"Is Hamiltonian Path {path}? {result}")

        print("\nTesting edge case with missing node:")
        result = bfs.bfs(start, not_in_graph)
        print(f"BFS to non-existing node {not_in_graph}: {result}")

# If this file is run directly, call main
if __name__ == "__main__":
    GraphUtils.main()
