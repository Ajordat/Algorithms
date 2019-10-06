from src.models.graphs.directed_graph import DirectedGraph

graph = DirectedGraph()

graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D')
graph.add_node('E')
graph.add_node('F')

graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('A', 'F')
graph.add_edge('B', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'D')
graph.add_edge('C', 'F')
graph.add_edge('D', 'E')
graph.add_edge('E', 'F')

print(graph)
