from src.models.graphs.base_graph import BaseGraph


class DirectedGraph(BaseGraph):

    def add_edge(self, node1, node2):
        self._assert_node_is_in_graph(node1)
        self._assert_node_is_in_graph(node2)

        if node2 not in self._g[node1]:
            self._g[node1].append(node2)
