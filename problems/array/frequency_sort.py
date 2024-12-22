from collections import Counter, OrderedDict


def solve(nums: list[int]):
    """
    1. build counter dict
    2. loop over the counter and build an ordered dict based on the count value for each item
    3. loop over the ordered dict and return the original array ordered.
    """
    counter = Counter(nums)

    sorted_dict = OrderedDict(sorted(counter.items(), key=lambda x: x[1]))

    return [k for k, v in sorted_dict.items() for _ in range(v)]


if __name__ == "__main__":
    nums = [2, 3, 1, 3, 2]
    result = solve(nums)
    assert result == []
