from data_structures.linked_list import LinkedListNode
from problems.linked_list.build_linked_list import build_linked_list


class Solution:
    def reorderList(self, head: LinkedListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        head, middle = self._split(head)
        middle = self._reverse(middle)
        head = self._merge(head, middle)
        return head

    def _split(self, head):
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            fast = fast.next

        middle = slow.next
        slow.next = None
        return head, middle

    def _reverse(self, head):
        cur = head
        result = None
        while cur:
            next_node = cur.next
            cur.next = result
            result = cur
            cur = next_node
        return result

    def _merge(self, a, b):
        head = a
        tail = a

        a = a.next
        while b:
            tail.next = b
            tail = tail.next

            b = b.next

            if a:
                a, b = b, a
        return head


if __name__ == "__main__":
    linked_list = build_linked_list([1, 2, 3, 4])
    result = Solution().reorderList(linked_list)
    assert result is None
