from collections import defaultdict


def solve(nums):
    """
    1.
    """
    groups = defaultdict(lambda: [])

    for i in range(len(nums)):
        groups[nums[i]].append(i)

    return [v[i : i + k] for k, v in groups.items() for i in range(len(v), k)]


def chunk(list, size):
    for i in range(0, len(list), size):
        yield list[i : i + size]


if __name__ == "__main__":
    group_sizes = [3, 3, 3, 3, 3, 1, 3]
    result = solve(group_sizes)
    assert result == []
