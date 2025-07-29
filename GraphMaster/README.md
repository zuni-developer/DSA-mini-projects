# 📊 GraphMaster: Graph Traversal & Utilities in Python

GraphMaster is a modular Python-based project to explore and manipulate graphs using classic algorithms like Breadth-First Search (BFS) and Depth-First Search (DFS). It includes directed/undirected graph support, node and edge definitions, graph building from file, and various utilities.

---

## 🗂️ Project Structure

| File Name              | Description |
|------------------------|-------------|
| `Node.py`              | Defines the `Node` class used in graphs. |
| `Edge.py`              | Defines the `Edge` class for connections between nodes. |
| `Graph.py`             | Base class containing common graph logic. |
| `DirectedGraph.py`     | Inherits from `Graph.py` to implement a directed graph. |
| `UndirectedGraph.py`   | Inherits from `Graph.py` to implement an undirected graph. |
| `BreadthFirstSearch.py`| Contains BFS traversal logic. |
| `DepthFirstSearch.py`  | Contains DFS traversal logic. |
| `GraphBuilder.py`      | Builds graph from external input (e.g., text file). |
| `graph_builder_test.txt`| Sample input file used by `GraphBuilder.py`. |
| `GraphUtils.py`        | Utility functions to support graph operations (e.g., printing, validating). |

---

## 🚀 How to Use

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-repo/graphmaster.git
   cd graphmaster
   ```

2. **Build a Graph from File**
   ```python
   from GraphBuilder import GraphBuilder
   graph = GraphBuilder.build_from_file('graph_builder_test.txt')
   ```

3. **Run BFS or DFS**
   ```python
   from BreadthFirstSearch import bfs
   bfs(graph, start_node)

   from DepthFirstSearch import dfs
   dfs(graph, start_node)
   ```

---

## 🧪 Sample Test File Format (`graph_builder_test.txt`)
```
A B
A C
B D
C E
```

Each line represents an edge (e.g., A → B).

---

## ✅ Features

- Directed and Undirected Graph support
- Node and Edge abstraction
- File-based graph construction
- Breadth-First and Depth-First Traversals
- Modular and extensible design

---

## 🛠️ Requirements

- Python 3.6+
- No external libraries required (only standard library)

---

## 📌 Notes

- The program is built using object-oriented principles.
- You can extend the traversal files to include path tracking, weights, or visited node recording.
- This is ideal for academic learning, visualization tools, or algorithm practice.
