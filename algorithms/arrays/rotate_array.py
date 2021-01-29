from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        result = []

        for i in range(length - k, 2 * length - k):
            i = i % length
            result.append(nums[i])

        return result

    def test(self, nums, k):
        l = len(nums)
        k = k % l
        nums[:] = nums[l - k:] + nums[:l - k]


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    result = Solution().rotate(nums, k)
    Solution().test(nums, k)
    assert nums == result
