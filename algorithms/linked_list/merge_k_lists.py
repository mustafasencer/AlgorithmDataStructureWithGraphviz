import heapq
from queue import PriorityQueue

from data_structures.linked_list.build import build_linked_list
from data_structures.linked_list.node import Node


def merge_k_sorted_lists(lists):
    queue = lists
    while queue:
        node = queue.pop(0)


def test(lists):
    ret = []
    for lst in lists:
        while lst:
            ret.append(lst.val)
            lst = lst.next

    return sorted(ret)


def test_(lists):
    result, heap = [], []
    for lst in lists:
        while lst:
            heapq.heappush(heap, lst.val)
            lst = lst.next

    while heap:
        result.append(heapq.heappop(heap))
    return result


def deneme(lists):
    dummy = Node(None)
    curr = dummy
    q = PriorityQueue()
    for node in lists:
        if node:
            q.put((node.val, node))
    while q.qsize() > 0:
        curr.next = q.get()[1]
        curr = curr.next
        if curr.next:
            q.put((curr.next.val, curr.next))
    return dummy.next


if __name__ == '__main__':
    q = PriorityQueue()

    q.put((2, 'g'))
    q.put((3, 'f'))
    q.put((3, 'w'))

    print(q.get())
    print(q.get())
    linked_list_1 = build_linked_list([1, 4, 5])
    linked_list_2 = build_linked_list([2, 3, 4])
    linked_list_3 = build_linked_list([3, 6])
    lists = [linked_list_1, linked_list_2, linked_list_3]
    result = deneme(lists)
    print(result)
