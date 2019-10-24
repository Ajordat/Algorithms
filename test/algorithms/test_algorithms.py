import unittest

from src.algorithms.graph_algorithms import GraphAlgorithms
from src.models.graphs.weighted_graph import WeightedGraph


class TestGraphAlgorithms(unittest.TestCase):

    default_graph = {'A': {'B': 7, 'C': 9, 'F': 14}, 'B': {'A': 7, 'C': 10, 'D': 15}, 'C': {'A': 9, 'B': 10, 'D': 11, 'F': 2}, 'D': {'B': 15, 'C': 11, 'E': 6}, 'E': {'D': 6, 'F': 9}, 'F': {'A': 14, 'C': 2, 'E': 9}}

    def test_dijkstra(self):
        solver = GraphAlgorithms()
        g = WeightedGraph(self.default_graph)

        result_a = solver.dijkstra(g, 'A')
        result_b = solver.dijkstra(g, 'B')
        result_c = solver.dijkstra(g, 'C')
        result_d = solver.dijkstra(g, 'D')
        result_e = solver.dijkstra(g, 'E')
        result_f = solver.dijkstra(g, 'F')

        self.assertEqual(result_a, {'A': 0, 'B': 7, 'C': 9, 'D': 20, 'E': 20, 'F': 11})
        self.assertEqual(result_b, {'A': 7, 'B': 0, 'C': 10, 'D': 15, 'E': 21, 'F': 12})
        self.assertEqual(result_c, {'A': 9, 'B': 10, 'C': 0, 'D': 11, 'E': 11, 'F': 2})
        self.assertEqual(result_d, {'A': 20, 'B': 15, 'C': 11, 'D': 0, 'E': 6, 'F': 13})
        self.assertEqual(result_e, {'A': 20, 'B': 21, 'C': 11, 'D': 6, 'E': 0, 'F': 9})
        self.assertEqual(result_f, {'A': 11, 'B': 12, 'C': 2, 'D': 13, 'E': 9, 'F': 0})

        self.assertRaises(KeyError, solver.dijkstra, g, 'X')
