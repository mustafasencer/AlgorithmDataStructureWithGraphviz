"""
    Created by Mustafa Sencer Özcan on 25.05.2020.

    Not completed yet!
    Check again.
"""
import collections

from data_structures.graph.directedgraph import AdjNode


class Solution:
    def cloneGraph(self, node: AdjNode) -> AdjNode:
        if not node:
            return
        nodeCopy = AdjNode(node.vertex)
        dic = {node: nodeCopy}
        queue = collections.deque([node])
        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor not in dic:  # neighbor is not visited
                    neighborCopy = AdjNode(neighbor.label)
                    dic[neighbor] = neighborCopy
                    dic[node].neighbors.append(neighborCopy)
                    queue.append(neighbor)
                else:
                    dic[node].neighbors.append(dic[neighbor])
        return nodeCopy


if __name__ == '__main__':
    result = Solution().cloneGraph([[2, 4], [1, 3], [2, 4], [1, 3]])
    print(result)
