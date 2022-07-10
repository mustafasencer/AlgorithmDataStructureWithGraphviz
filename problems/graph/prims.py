"""
    Created by Mustafa Sencer Özcan on 01.06.2020.
"""
from heapq import heappop, heappush
from itertools import count

from data_structures.graph import DirectedGraph


def minimum_spanning_tree_cost(graph):
    """
    Return the sum of the costs of the edges in the minimum spanning
    tree for the given graph, which must be a mapping from nodes to an
    iterable of (neighbor, edge-cost) pairs.

    """
    tiebreak = count().__next__  # Factory for tie-breaking values
    total = 0  # Total cost of edges in tree
    explored = set()  # Set of vertices in tree
    start = next(iter(graph))  # Arbitrary starting vertex
    unexplored = [(0, tiebreak(), start)]  # Unexplored edges ordered by cost
    while unexplored:
        cost, _, winner = heappop(unexplored)
        if winner not in explored:
            explored.add(winner)
            total += cost
            for neighbor, cost in graph[winner]:
                if neighbor not in explored:
                    heappush(unexplored, (cost, tiebreak(), neighbor))
    return total


if __name__ == "__main__":
    V = 5
    graph = DirectedGraph(5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    minimum_spanning_tree_cost(graph)
