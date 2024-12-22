"""
Not completed yet!
Check again.
"""

import collections

from data_structures.graph import GraphNode


class Solution:
	def cloneGraph(self, node: GraphNode) -> GraphNode:
		if not node:
			return
		nodeCopy = GraphNode(node.vertex)
		dic = {node: nodeCopy}
		queue = collections.deque([node])
		while queue:
			node = queue.popleft()
			for neighbor in node.neighbors:
				if neighbor not in dic:  # neighbor is not visited
					neighborCopy = GraphNode(neighbor.label)
					dic[neighbor] = neighborCopy
					dic[node].neighbors.append(neighborCopy)
					queue.append(neighbor)
				else:
					dic[node].neighbors.append(dic[neighbor])
		return nodeCopy


if __name__ == "__main__":
	result = Solution().cloneGraph([[2, 4], [1, 3], [2, 4], [1, 3]])
	print(result)
