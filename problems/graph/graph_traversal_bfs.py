from collections import defaultdict


class Graph:
    def __init__(self, V) -> None:
        self.V = V
        self.graph = defaultdict(list)

    def add_edge(self, u, v) -> None:
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

    def bfs_queue_1(self, s):
        visited = [False] * self.V

        result = []
        queue = []

        queue.append(s)
        visited[s] = True

        while queue:
            vertex = queue.pop(0)
            result.append(vertex)

            for v in self.graph[vertex]:
                if v not in visited[v]:
                    queue.append(v)
                    visited[v] = True

        return result


if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    assert g.test_bfs_queue(2) == g.bfs_queue(2)
