from src.models.graphs.weighted_graph import WeightedGraph

graph = WeightedGraph()

graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D')
graph.add_node('E')
graph.add_node('F')

graph.add_edge('A', 'B', weight=2)
graph.add_edge('A', 'C', weight=9)
graph.add_edge('A', 'F', weight=5)
graph.add_edge('B', 'C', weight=7)
graph.add_edge('B', 'D', weight=1)
graph.add_edge('C', 'D', weight=2)
graph.add_edge('C', 'F', weight=3)
graph.add_edge('D', 'E', weight=4)
graph.add_edge('E', 'F', weight=5)

print(graph)
