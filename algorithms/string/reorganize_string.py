import heapq
from collections import Counter, OrderedDict


def solve(s: str) -> str:
    a = sorted(sorted(s), key=s.count)
    h = len(s) // 2
    a[1::2], a[0::2] = a[:h], a[h:]
    return "".join(a) * (a[-1] != a[-2])


# [a: 2, b: 2, c: 1]
def solve_2(s: str) -> str:
    result = []
    counter = Counter(s)
    counter = [(-value, key) for key, value in counter.items()]

    heapq.heapify(counter)

    prev_key, prev_value = "", 0

    while counter:
        value, key = heapq.heappop(counter)

        result.append(key)

        if prev_value < 0:
            heapq.heappush(counter, (prev_value, prev_key))

        value += 1
        prev_value = value
        prev_key = key

    if len(result) != len(s):
        return ""
    return "".join(result)


if __name__ == '__main__':
    s = 'aaaab'
    result = solve_2(s)
    assert result == ""
