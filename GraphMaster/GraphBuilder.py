from DirectedGraph import DirectedGraph
from UndirectedGraph import UndirectedGraph


class GraphBuilder:
    @staticmethod
    def build_directed_graph(filename):
        dg = DirectedGraph()
        try:
            GraphBuilder.build_graph(dg, filename)
        except Exception as e:
            print(f"An exception occurred while trying to read {filename}: {e}")
            return None
        return dg

    @staticmethod
    def build_undirected_graph(filename):
        ug = UndirectedGraph()
        try:
            GraphBuilder.build_graph(ug, filename)
        except Exception as e:
            print(f"An exception occurred while trying to read {filename}: {e}")
            return None
        return ug

    @staticmethod
    def build_graph(graph, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    edge = line.strip().split()
                    if len(edge) < 2:
                        continue
                    source, destination = edge[0], edge[1]
                    source_node = graph.get_node(source)
                    destination_node = graph.get_node(destination)
                    graph.add_edge(source_node, destination_node)
        except FileNotFoundError:
            raise FileNotFoundError(f"The file '{filename}' was not found.")
        except IOError:
            raise IOError(f"Error occurred while reading the file '{filename}'.")
