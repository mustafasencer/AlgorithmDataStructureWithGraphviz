from data_structures.heap.max_heapify import heapify


def heap_sort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(int(n / 2 - 1), -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


if __name__ == '__Main__':
    arr = [12, 11, 13, 5, 6, 7]
    heap_sort(arr)
    n = len(arr)
    print("Sorted array is")
    for i in range(n):
        print("%d" % arr[i]),
