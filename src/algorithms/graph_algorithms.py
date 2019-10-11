import math

from src.models.graphs.weighted_graph import WeightedGraph


class GraphAlgorithms:

    @staticmethod
    def __dijkstra(graph, start):
        distances = {key: math.inf for key in graph._g}
        distances[start] = 0
        to_check = [start]
        checked = []
        for node in to_check:
            for neighbor, weight in graph[node].items():
                if neighbor not in checked and neighbor not in to_check:
                    to_check.append(neighbor)
                if distances[neighbor] > distances[node] + weight:
                    distances[neighbor] = distances[node] + weight

            checked.append(node)

        return distances

    @classmethod
    def dijkstra(cls, graph, start):
        assert type(graph) == WeightedGraph
        graph._assert_node_is_in_graph(start)

        return cls.__dijkstra(graph, start)
