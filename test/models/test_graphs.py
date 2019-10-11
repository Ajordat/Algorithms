import unittest

from src.models.graphs.directed_graph import DirectedGraph
from src.models.graphs.graph import Graph
from src.models.graphs.weighted_graph import WeightedGraph


class TestBaseGraph(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.graph_class = None

    def add_node(self):
        g = self.graph_class()
        g.add_node('A')

        self.assertIn('A', g)
        self.assertEqual(len(g), 1)
        self.assertIsNotNone(g.get_node('A'))
        self.assertIsNotNone(g['A'])

    def node_is_in_graph(self):
        g = self.graph_class()
        g.add_node('A')

        g._assert_node_is_in_graph('A')
        self.assertRaises(KeyError, g._assert_node_is_in_graph, 'X')

    def add_edge(self):
        g = self.graph_class()
        g.add_node('A')
        g.add_node('B')
        g.add_edge('A', 'B')

        self.assertEqual(len(g), 2)
        self.assertRaises(KeyError, g.add_edge, 'A', 'X')
        self.assertRaises(KeyError, g.add_edge, 'X', 'B')
        return g


class TestGraph(TestBaseGraph):

    def __init__(self, *args):
        super().__init__(*args)
        self.graph_class = Graph

    def test_add_node(self):
        self.add_node()

    def test_node_is_in_graph(self):
        super().node_is_in_graph()

    def test_add_edge(self):
        g = super().add_edge()

        self.assertIn('B', g.get_edges('A'))
        self.assertIn('A', g.get_edges('B'))


class TestDirectedGraph(TestGraph):

    def __init__(self, *args):
        super().__init__(*args)
        self.graph_class = DirectedGraph

    def test_add_edge(self):
        g = super().add_edge()

        self.assertIn('B', g.get_edges('A'))
        self.assertNotIn('A', g.get_edges('B'))


class TestWeightedGraph(TestGraph):

    def __init__(self, *args):
        super().__init__(*args)
        self.graph_class = WeightedGraph
