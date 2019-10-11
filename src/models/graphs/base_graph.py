from abc import abstractmethod, ABC


class BaseGraph(ABC):

    def __init__(self, g=None):
        self._g = {} if g is None else g

    def _assert_node_is_in_graph(self, node):
        if node not in self._g:
            raise KeyError(node)

    def add_node(self, node):
        if node not in self._g.keys():
            self._g[node] = []

    def get_node(self, node):
        return self._g[node]

    def get_edges(self, node):
        return self._g[node]

    @abstractmethod
    def add_edge(self, node1, node2):
        pass

    def __str__(self):
        return str(self._g)

    def __contains__(self, item):
        return item in self._g

    def __getitem__(self, item):
        return self._g[item]
