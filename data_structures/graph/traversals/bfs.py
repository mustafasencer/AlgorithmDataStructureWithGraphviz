""" Not implemented yet. """
from collections import defaultdict


class Graph:

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs_queue(self, s):

        visited = [False] * self.V

        queue = []
        result = []

        queue.append(s)
        visited[s] = True

        while queue:

            s = queue.pop(0)
            result.append(s)

            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
        return result

    def test_bfs_queue(self, start):
        visited = [False] * self.V
        queue = []
        result = []

        queue.append(start)

        while queue:
            s = queue.pop(0)

            if not visited[s]:
                result.append(s)
                visited[s] = True
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
        return result


if __name__ == '__main__':
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    assert g.test_bfs_queue(2) == g.bfs_queue(2)
    print(g.test_bfs_queue(2))
