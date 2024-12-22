from collections import defaultdict


class GraphNode:
    def __init__(self, data, neighbors=None) -> None:
        self.vertex = data
        self.neighbors = neighbors if neighbors is not None else []


class WeightedGraph:
    def __init__(self, vertices) -> None:
        self.V = vertices
        self.graph = []

    def add_edge(self, v, w, c) -> None:
        self.graph.append((v, w, c))

    def print_graph(self) -> None:
        for i in range(self.V):
            temp = self.graph[i]
            while temp:
                pass


class DirectedGraph:
    def __init__(self, vertices) -> None:
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, v, w) -> None:
        self.graph[v].append(w)

    def print_graph(self) -> None:
        for i in range(self.V):
            temp = self.graph[i]
            while temp:
                pass


if __name__ == "__main__":
    V = 5
    graph = DirectedGraph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    graph.print_graph()
