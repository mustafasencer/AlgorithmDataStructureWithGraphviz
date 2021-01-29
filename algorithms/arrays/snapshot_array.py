import bisect
from functools import lru_cache


class SnapshotArray(object):
    def __init__(self, n):
        self.cache = [[[-1, 0]] for _ in range(n)]
        self.snap_id = 0

    def set(self, index, val):
        self.cache[index].append([self.snap_id, val])

    def snap(self):
        self.snap_id += 1
        return self.snap_id - 1

    @lru_cache(maxsize=None)
    def get(self, index, snap_id):
        i = bisect.bisect(self.cache[index], [snap_id + 1]) - 1
        return self.cache[index][i][1]


if __name__ == '__main__':
    obj = SnapshotArray(3)
    obj.set(0, 5)
    obj.snap()
    obj.set(0, 6)
    result = obj.get(0, 0)
    assert result == 5
    print(result)
