from data_structures.linked_list import LinkedListNode
from problems.linked_list.build_linked_list import build_linked_list
from visualization.linked_list import LinkedListDrawer


class Solution:
    def mergeTwoLists(self, l1: LinkedListNode, l2: LinkedListNode) -> LinkedListNode:
        dummy = cur = LinkedListNode(0)
        while l1 and l2:
            if l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

    def _test(self, l1, l2):
        fake = cur = LinkedListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return fake.next


if __name__ == "__main__":
    l1 = build_linked_list([1, 2, 4])
    l2 = build_linked_list([1, 3, 4])
    result = Solution()._test(l1, l2)
    LinkedListDrawer().visualize(result)
