import heapq
from heapq import heapify

from problems.heap.max_heapify import heapify as heapify_


def heap_sort(arr):
    length = len(arr)

    # Build a max heap.
    for i in range(int(length / 2 - 1), -1, -1):
        heapify_(arr, length, i)

    # One by one extract elements
    for i in range(length - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify_(arr, i, 0)


def heap_sort_1(arr):
    heapq.heapify(arr)


def test_heap_sort(array):
    heapify(array)


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    heap_sort_1(arr)
    assert arr == [5, 6, 7, 11, 12, 13]
