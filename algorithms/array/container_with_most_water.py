"""
    Created by Mustafa Sencer Özcan on 20.05.2020.
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        j = len(height) - 1
        i = 0
        while i != j:
            if height[i] > height[j]:
                max_area = max(height[j] * (j - i), max_area)
                j -= 1
            else:
                max_area = max(height[i] * (j - i), max_area)
                i += 1
        return max_area


if __name__ == '__main__':
    result = Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print(result)
