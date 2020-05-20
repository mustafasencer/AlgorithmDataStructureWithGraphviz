"""
    Created by Mustafa Sencer Özcan on 19.05.2020.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        dict_ = {}
        max_ = 0
        last_index = 0
        for i, value in enumerate(s):
            if value in dict_:
                # second pointer should be moved left to the last occurrence
                last_index = max(dict_[value] + 1, last_index)
            dict_[value] = i
            max_ = max(max_, i - last_index + 1)
        return max_


if __name__ == '__main__':
    result = Solution().lengthOfLongestSubstring("abba")
    print(result)
