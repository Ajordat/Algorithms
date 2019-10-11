from src.models.graphs.base_graph import BaseGraph


class WeightedGraph(BaseGraph):

    def add_node(self, node):
        if node not in self._g:
            self._g[node] = {}

    def add_edge(self, node1, node2, weight=1.0):
        self._assert_node_is_in_graph(node1)
        self._assert_node_is_in_graph(node2)

        self._g[node1][node2] = weight
        self._g[node2][node1] = weight
