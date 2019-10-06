from abc import abstractmethod, ABC


class BaseGraph(ABC):

    def __init__(self, g=None):
        self.g = {} if g is None else g

    def _assert_node_is_in_graph(self, node):
        if node not in self.g:
            raise KeyError(node)

    def add_node(self, node):
        if node not in self.g.keys():
            self.g[node] = []

    @abstractmethod
    def add_edge(self, node1, node2):
        pass

    def __str__(self):
        return str(self.g)
