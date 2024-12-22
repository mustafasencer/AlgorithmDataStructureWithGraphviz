"""
Implement a SnapshotArray that supports the following interface:

SnapshotArray(length: int) initializes an array-like data structure with the given length.
 Initially, each element equals 0. void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id
"""

import bisect
from collections import defaultdict
from functools import cache


class SnapshotArray:
    def __init__(self, n) -> None:
        self.cache = [[[-1, 0]] for _ in range(n)]
        self.snap_id = 0

    def set(self, index, val) -> None:
        self.cache[index].append([self.snap_id, val])

    def snap(self):
        self.snap_id += 1
        return self.snap_id - 1

    @cache
    def get(self, index, snap_id):
        i = bisect.bisect(self.cache[index], [snap_id + 1]) - 1
        return self.cache[index][i][1]


class SnapshotArray1:
    def __init__(self, length: int) -> None:
        self.map = defaultdict(list)
        self.snapId = 0

    def set(self, index: int, val: int) -> None:
        if self.map[index] and self.map[index][-1][0] == self.snapId:
            self.map[index][-1][1] = val
            return
        self.map[index].append([self.snapId, val])

    def snap(self) -> int:
        self.snapId += 1
        return self.snapId - 1

    def get(self, index: int, snap_id: int) -> int:
        arr = self.map[index]
        left, right, ans = 0, len(arr) - 1, -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] <= snap_id:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        if ans == -1:
            return 0
        return arr[ans][1]


if __name__ == "__main__":
    obj = SnapshotArray(3)
    obj.set(0, 5)
    snap_id = obj.snap()
    obj.set(0, 6)
    result = obj.get(0, 0)
    assert snap_id == 0
    assert result == 5
