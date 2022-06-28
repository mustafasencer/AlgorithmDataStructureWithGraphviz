from collections import Counter, OrderedDict
from typing import List


def solve(nums: List[int]):
    counter = Counter(nums)

    sorted_dict = OrderedDict(sorted(counter.items(), key=lambda x: x[1]))

    return [k for k, v in sorted_dict.items() for _ in range(v)]


if __name__ == '__main__':
    nums = [2, 3, 1, 3, 2]
    result = solve(nums)
    assert result == []
