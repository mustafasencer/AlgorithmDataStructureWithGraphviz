from data_structures.linked_list import LinkedListNode
from problems.linked_list.build_linked_list import build_linked_list


class Solution:
    def merge_two_lists(self, l1: LinkedListNode, l2: LinkedListNode) -> LinkedListNode:
        fake = cur = LinkedListNode(0)
        while l1 and l2:
            if l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next
        cur.next = l1 or l2
        return fake.next


if __name__ == "__main__":
    l1 = build_linked_list([1, 2, 4])
    l2 = build_linked_list([1, 3, 4])
    result_list = Solution().merge_two_lists(l1, l2)
    result = []
    while result_list:
        result.append(result_list.val)
        result_list = result_list.next
    assert result == [1, 1, 2, 3, 4, 4]
