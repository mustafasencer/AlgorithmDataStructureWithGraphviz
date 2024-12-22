from data_structures.linked_list import LinkedListNode
from problems.linked_list.build_linked_list import build_linked_list


class Solution:
    def hasCycle(self, head: LinkedListNode) -> bool:
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
        except Exception:
            return False

        return False


if __name__ == "__main__":
    head = build_linked_list([3, 2, 0, -4])
    result = Solution().hasCycle(head)
