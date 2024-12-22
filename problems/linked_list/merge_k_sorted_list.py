from heapq import heappop, heappush
from typing import List

from data_structures.linked_list import DoublyLinkedListNode
from problems.linked_list.build_linked_list import build_linked_list
from visualization.linked_list import LinkedListDrawer


def solution(lists: List[DoublyLinkedListNode]) -> DoublyLinkedListNode:
	queue = []
	fake = cur = DoublyLinkedListNode(-1)
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


if __name__ == "__main__":
	l1 = build_linked_list([1, 4, 5])
	l2 = build_linked_list([1, 3, 4])
	l3 = build_linked_list([2, 6])
	result = solution([l1, l2, l3])
	LinkedListDrawer().visualize(result)
