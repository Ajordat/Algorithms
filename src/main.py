from src.algorithms.graph_algorithms import GraphAlgorithms
from src.models.graphs.weighted_graph import WeightedGraph
from src.models.trees.binary_tree import BinaryTree

graph = WeightedGraph()

graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D')
graph.add_node('E')
graph.add_node('F')

graph.add_edge('A', 'B', weight=7)
graph.add_edge('A', 'C', weight=9)
graph.add_edge('A', 'F', weight=14)
graph.add_edge('B', 'C', weight=10)
graph.add_edge('B', 'D', weight=15)
graph.add_edge('C', 'D', weight=11)
graph.add_edge('C', 'F', weight=2)
graph.add_edge('D', 'E', weight=6)
graph.add_edge('E', 'F', weight=9)

print(graph)

solver = GraphAlgorithms()

res = solver.dijkstra(graph, 'A')
print(f"Dijkstra: {res}")

tree = BinaryTree()

tree.add_value(1)
tree.add_value(2)
tree.add_value(3)
tree.add_value(4)
tree.add_value(2)

print(tree)
print(tree.search(3))
