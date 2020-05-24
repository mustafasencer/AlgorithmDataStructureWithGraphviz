"""
    Created by Mustafa Sencer Özcan on 21.05.2020.
    backtrack
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.backtrack(result, candidates, [], target, 0)
        return result

    def backtrack(self, result_, nums, temp, remain, start):
        if remain < 0:
            return
        if remain == 0:
            result_.append(temp)
            return
        else:
            for i in range(start, len(nums)):
                self.backtrack(result_, nums, temp + [nums[i]], remain - nums[i], i)


if __name__ == '__main__':
    result = Solution().combinationSum([2, 3, 6, 7], 7)
    print(result)
