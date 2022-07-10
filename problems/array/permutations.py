from typing import List


def solve(nums: List[int]) -> List[List[int]]:
    def backtrack(start, end):
        if start == end:
            ans.append(nums[:])
        for i in range(start, end):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1, end)
            nums[start], nums[i] = nums[i], nums[start]

    ans = []
    backtrack(0, len(nums))
    return ans


def solve_2(nums):
    res = []
    dfs(nums, [], res)
    return res


def dfs(nums, path, res):
    if not nums:
        res.append(path)
    for i in range(len(nums)):
        dfs(nums[:i] + nums[i + 1 :], path + [nums[i]], res)


if __name__ == "__main__":
    nums = [1, 2, 3]
    result = solve_2(nums)
    assert result == []
