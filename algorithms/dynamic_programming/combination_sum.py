"""
    Created by Mustafa Sencer Özcan on 21.05.2020.
    BACKTRACK!

    Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

    The same repeated number may be chosen from candidates unlimited number of times.

    Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.
"""
from typing import List


class Solution:
    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
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

    def _test(self, candidates, target):
        result = []
        self.dfs(result, candidates, target, [])
        return result

    def dfs(self, result_, candidates, remain, path):
        if remain < 0:
            return
        if remain == 0:
            result_.append(path)
            return
        for i in range(len(candidates)):
            self.dfs(result_, candidates[i:], remain - candidates[i], path + [candidates[i]])


if __name__ == '__main__':
    # result = Solution().combination_sum([2, 3, 6, 7], 7)
    result = Solution()._test([2, 3, 6, 7], 7)
    print(result)
