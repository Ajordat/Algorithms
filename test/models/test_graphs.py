import unittest

from src.models.graphs.directed_graph import DirectedGraph
from src.models.graphs.graph import Graph


class TestGraph(unittest.TestCase):

    def test_insert_node(self):
        g = Graph()
        g.add_node('A')

        self.assertIn('A', g)
        self.assertIsNotNone(g.get_node('A'))
        self.assertIsNotNone(g['A'])

    def test_node_is_in_graph(self):
        g = Graph()
        g.add_node('A')

        g._assert_node_is_in_graph('A')
        self.assertRaises(KeyError, g._assert_node_is_in_graph, 'X')

    def test_add_edge(self):
        g = Graph()
        g.add_node('A')
        g.add_node('B')
        g.add_edge('A', 'B')

        self.assertRaises(KeyError, g.add_edge, 'A', 'X')
        self.assertRaises(KeyError, g.add_edge, 'X', 'B')
        self.assertRaises(KeyError, g.add_edge, 'X', 'Y')
        self.assertIn('B', g.get_edges('A'))
        self.assertIn('A', g.get_edges('B'))
        self.assertRaises(KeyError, g.get_edges, 'X')


class TestDirectedGraph(unittest.TestCase):

    def test_add_edge(self):
        g = DirectedGraph()
        g.add_node('A')
        g.add_node('B')
        g.add_edge('A', 'B')

        self.assertRaises(KeyError, g.add_edge, 'A', 'X')
        self.assertRaises(KeyError, g.add_edge, 'X', 'B')
        self.assertRaises(KeyError, g.add_edge, 'X', 'Y')
        self.assertIn('B', g.get_edges('A'))
        self.assertNotIn('A', g.get_edges('B'))
        self.assertRaises(KeyError, g.get_edges, 'X')
