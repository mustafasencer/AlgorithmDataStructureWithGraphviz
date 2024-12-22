from collections import defaultdict


class GraphNode:
	def __init__(self, data, neighbors=None):
		self.vertex = data
		self.neighbors = neighbors if neighbors is not None else []


class WeightedGraph:
	def __init__(self, vertices):
		self.V = vertices
		self.graph = []

	def add_edge(self, v, w, c):
		self.graph.append((v, w, c))

	def print_graph(self):
		for i in range(self.V):
			print("Adjacency list of vertex {}\n head".format(i), end="")
			temp = self.graph[i]
			while temp:
				print(" -> {}".format(temp.pop(0)), end="")
			print(" \n")


class DirectedGraph:
	def __init__(self, vertices):
		self.V = vertices
		self.graph = defaultdict(list)

	def add_edge(self, v, w):
		self.graph[v].append(w)

	def print_graph(self):
		for i in range(self.V):
			print("Adjacency list of vertex {}\n head".format(i), end="")
			temp = self.graph[i]
			while temp:
				print(" -> {}".format(temp.pop(0)), end="")
			print(" \n")


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
