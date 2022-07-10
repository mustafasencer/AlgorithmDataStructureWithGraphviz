"""
    Created by Mustafa Sencer Özcan on 21.05.2020.
"""
from collections import defaultdict
from typing import List


class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        memo = {}
        for item in strs:
            sort_ = "".join(sorted(item))
            if sort_ in memo:
                memo[sort_].append(item)
            else:
                memo[sort_] = [item]
        result = [v for k, v in memo.items()]
        return result

    def test(self, strs: List[str]):
        lookup = defaultdict(list)

        for item in strs:
            key = "".join(sorted(item))
            lookup[key].append(item)

        return [value for _, value in lookup.items()]


if __name__ == "__main__":
    result = Solution().test(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(result)
