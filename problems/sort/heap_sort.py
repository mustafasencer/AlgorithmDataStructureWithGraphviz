from heapq import heapify

from problems.max_heapify import heapify as heapify_


def heap_sort(arr):
    length = len(arr)

    # Build a maxheap.
    for i in range(int(length / 2 - 1), -1, -1):
        heapify_(arr, length, i)

    # One by one extract elements
    for i in range(length - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify_(arr, i, 0)


def test_heap_sort(array):
    heapify(array)


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    heap_sort(arr)
    # test_heap_sort(arr)
    length = len(arr)
    print("Sorted array is")
    for i in range(length):
        print("%d" % arr[i])
