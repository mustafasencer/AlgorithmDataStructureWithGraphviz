"""
    Created by Mustafa Sencer Özcan on 20.05.2020.
"""
from heapq import heappush, heappop
from typing import List

from data_structures.doubly_linked_list.node import Node
from data_structures.linked_list.build.builder import build_linked_list
from drawer.linked_list import LinkedListDrawer


class Solution:
    def mergeKLists(self, lists: List[Node]) -> Node:
        queue = []
        fake = cur = Node(-1)
        i = 0
        for node in lists:
            heappush(queue, (node.val, i, node))
            i += 1
        while queue:
            cur.next = heappop(queue)[-1]
            cur = cur.next
            if cur.next:
                heappush(queue, (cur.next.val, i, cur.next))
                i += 1
        return fake.next


if __name__ == '__main__':
    l1 = build_linked_list([1, 4, 5])
    l2 = build_linked_list([1, 3, 4])
    l3 = build_linked_list([2, 6])
    result = Solution().mergeKLists([l1, l2, l3])
    LinkedListDrawer().visualize(result)
