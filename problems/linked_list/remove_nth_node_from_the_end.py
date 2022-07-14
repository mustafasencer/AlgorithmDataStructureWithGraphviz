from data_structures.linked_list import LinkedListNode


class Solution:
    def removeNthFromEnd(self, head: LinkedListNode, n: int) -> LinkedListNode:
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
    new_node = LinkedListNode(value)
    new_node.next = head
    head = new_node


if __name__ == "__main__":
    head = None
    for i in range(5, 0, -1):
        push(i)
    result = Solution().removeNthFromEnd(head, 2)
