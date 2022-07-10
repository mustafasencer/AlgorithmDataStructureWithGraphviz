"""
    Created by Mustafa Sencer Özcan on 19.05.2020.
"""
from collections import defaultdict


class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def add_edge(self, v, w):
        self.graph[v].append(w)

    def dfs(self, start):
        visited = [False] * self.V

        stack = []
        result = []

        stack.append(start)

        while stack:
            s = stack.pop()
            if not visited[s]:
                visited[s] = True
                result.append(s)

            for node in self.graph[s]:
                if not visited[node]:
                    stack.append(node)
        return result

    def dfs_(self, start):
        visited = [False] * self.V

        stack = []
        result = []
        stack.append(start)

        while stack:
            s = stack.pop()

            if not visited[s]:
                visited[s] = True
                result.append(s)
            for i in self.graph[s]:
                if not visited[i]:
                    stack.append(i)
        return result


if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(0, 3)
    g.add_edge(1, 4)
    assert g.dfs(1) == g.dfs_(1)
    print(g.dfs(1))
