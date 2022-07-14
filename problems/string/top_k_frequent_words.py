import collections
import heapq
from collections import defaultdict


def solution(nums, k):
    lookup = defaultdict(lambda: 0)

    for word in nums:
        lookup[word] += 1

    return [k for k, v in sorted(lookup.items(), key=lambda x: (-x[1], x[0]))][:k]


def solution_1(nums, k):
    counter = collections.Counter(nums)
    values = counter.most_common(k)
    return [i[0] for i in sorted(values, key=lambda x: (-x[1], x[0]))]


def solution_2(nums, k):
    counts = collections.Counter(nums)

    freqs = []
    heapq.heapify(freqs)
    for word, count in counts.items():
        heapq.heappush(freqs, ((count, word), word))  # here needs a bit more attention!
        if len(freqs) > k:
            heapq.heappop(freqs)

    res = []
    for _ in range(k):
        res.append(heapq.heappop(freqs)[1])
    return res[::-1]


if __name__ == '__main__':
    nums = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is", "kali"]
    k = 4
    result = solution_2(nums, k)
    print(result)
    assert result == ["the", "is", "sunny", "day"]
