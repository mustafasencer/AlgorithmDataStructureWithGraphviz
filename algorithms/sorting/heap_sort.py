from data_structures.heap.max_heapify import heapify as heapify_
from heapq import heapify


def heap_sort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(int(n / 2 - 1), -1, -1):
        heapify_(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify_(arr, i, 0)


def heap_sort_deneme(array):
    heapify(array)


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    # heap_sort(arr)
    heap_sort_deneme(arr)
    n = len(arr)
    print("Sorted array is")
    for i in range(n):
        print("%d" % arr[i]),
