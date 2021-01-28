"""
    Created by Mustafa Sencer Özcan on 19.05.2020.
"""
from typing import List


class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        index = 0
        for value in nums:
            if index < 2 or nums[index - 2] < value:
                nums[index] = value
                index += 1
        return len(nums[:index])


if __name__ == '__main__':
    result = Solution().remove_duplicates([1, 1, 1, 2, 2, 3])
    print(result)
