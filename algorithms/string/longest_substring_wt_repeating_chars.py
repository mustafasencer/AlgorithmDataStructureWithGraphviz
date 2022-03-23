"""
    Created by Mustafa Sencer Özcan on 19.05.2020.
"""


class Solution:
    def length_longest_substring(self, s: str) -> int:
        if not s:
            return 0
        lookup = {}
        longest_value = 0
        last_index = 0

        for i, value in enumerate(s):
            if value in lookup:
                # second pointer should be moved left to the last occurrence
                last_index = max(lookup[value] + 1, last_index)
            lookup[value] = i
            longest_value = max(longest_value, i - last_index + 1)

        return longest_value

    def test_(self, s):
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


if __name__ == '__main__':
    result = Solution().length_longest_substring("abbacdabc")
    assert result == 4
    print(result)
