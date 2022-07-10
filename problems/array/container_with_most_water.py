"""
    Created by Mustafa Sencer Özcan on 20.05.2020.

    Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
    n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
    Find two lines, which together with x-axis forms a container, such that the container contains the most water.

    Note: You may not slant the container and n is at least 2.
"""
from typing import List


class Solution:
    def max_area(self, height: List[int]) -> int:
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

    def test_(self, height):
        i = 0
        j = len(height) - 1
        max_area = 0

        while i < j:
            max_area = max(max_area, min(height[i], height[j]) * (j - i))

            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max_area

    def test__(self, height):
        for i in range(len(height)):
            pass


if __name__ == "__main__":
    result = Solution().test_([1, 8, 6, 2, 5, 4, 8, 3, 7])
    result_ = Solution().max_area([1, 8, 6, 2, 5, 4, 8, 3, 7])
    assert result == result_
