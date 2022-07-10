"""
    Created by Mustafa Sencer Özcan on 19.05.2020.
    Hint: Move pointers intellugently in order to solve it!
"""


class Solution:
    @staticmethod
    def length_longest_substring(s: str) -> int:
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

    @staticmethod
    def length_longest_substring_2(s):
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


if __name__ == "__main__":
    result = Solution().length_longest_substring("abbacdabc")
    assert result == 4
    print(result)
