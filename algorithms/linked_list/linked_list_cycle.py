"""
    Created by Mustafa Sencer Özcan on 26.05.2020.
"""
from data_structures.linked_list.build.builder import build_linked_list
from data_structures.linked_list.node import Node


class Solution:
    def hasCycle(self, head: Node) -> bool:
        if not head:
            return False
        fast = head
        slow = head
        try:
            while fast and slow:
                slow = slow.next
                fast = fast.next.next
                if slow is fast:
                    return True
        except:
            return False


if __name__ == '__main__':
    head = build_linked_list([3, 2, 0, -4])
    result = Solution().hasCycle(head)
    print(result)
