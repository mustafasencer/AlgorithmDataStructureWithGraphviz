"""
    Created by Mustafa Sencer Özcan on 20.05.2020.
"""
from data_structures.linked_list.node import Node


class Solution:
    def removeNthFromEnd(self, head: Node, n: int) -> Node:
        fast = slow = head

        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


def push(value):
    global head
    new_node = Node(value)
    new_node.next = head
    head = new_node


if __name__ == '__main__':
    head = None
    for i in range(5, 0, -1):
        push(i)
    result = Solution().removeNthFromEnd(head, 2)
