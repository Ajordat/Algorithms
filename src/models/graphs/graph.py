from src.models.graphs.base_graph import BaseGraph


class Graph(BaseGraph):

    def add_edge(self, node1, node2):
        self._assert_node_is_in_graph(node1)
        self._assert_node_is_in_graph(node2)

        if node2 not in self._g[node1]:
            self._g[node1].append(node2)
        if node1 not in self._g[node2]:
            self._g[node2].append(node1)

    def __dfs(self, current_node, checked):
        print(current_node)
        checked.append(current_node)

        for vertex in self._g[current_node]:
            if vertex not in checked:
                self.__dfs(vertex, checked)

    def dfs(self, start):
        self._assert_node_is_in_graph(start)
        self.__dfs(start, [])

    def __bfs(self, current_node, following, checked):
        print(current_node)
        checked.append(current_node)

        for vertex in self._g[current_node]:
            if vertex not in checked:
                following.append(vertex)
        if following:
            self.__bfs(following.pop(0), following, checked)

    def bfs(self, start):
        self._assert_node_is_in_graph(start)
        self.__bfs(start, [], [])

    def __find_path(self, node1, node2, path, checked):
        path.append(node1)
        checked.append(node1)
        if node1 == node2:
            return path
        for vertex in self._g[node1]:
            if vertex not in checked:
                result = self.__find_path(vertex, node2, path, checked)
                if result:
                    return result
        path.remove(node1)

    def find_path(self, node1, node2):
        self._assert_node_is_in_graph(node1)
        self._assert_node_is_in_graph(node2)
        return self.__find_path(node1, node2, [], [])
