"""Hint: Move pointers intelligently in order to solve it!"""


def solution(s: str) -> int:
    if not s:
        return 0
    lookup = {}
    longest_value = 0
    count_from = 0

    for i, value in enumerate(s):
        if value in lookup:
            # second pointer should be moved left to the last occurrence
            count_from = max(lookup[value] + 1, count_from)
        lookup[value] = i
        longest_value = max(longest_value, i - count_from + 1)

    return longest_value


def solution_1(s):
    dict_ = {}
    counter = begin = end = d = 0
    while end < len(s):
        if dict_[s[end]] > 0:
            counter += 1
        dict_[s[end]] += 1
        end += 1
        while counter > 0:
            if dict_[s[begin]]:
                counter -= 1
            s[begin] -= 1
            begin += 1
        d = max(d, end - begin)
    return d


def solution_2(s):
    lookup = {}
    dp = [1] * len(s)
    start = 0

    for i in range(len(s)):
        current = s[i]

        if current in lookup:
            if start < lookup[current]:
                start = i
            else:
                dp[i] = i - start + 1
        elif i != 0:
            dp[i] = dp[i - 1] + 1

        lookup[current] = i

    return max(dp)


if __name__ == "__main__":
    result = solution_2("abbacdabc")
    assert result == 4
