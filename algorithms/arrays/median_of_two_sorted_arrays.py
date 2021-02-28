"""
    Created by Mustafa Sencer Özcan on 19.05.2020.
"""
from typing import List


class Solution:
    def find_median_sorted_arrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_1, len_2 = len(nums1), len(nums2)
        if len_1 > len_2:
            len_2, len_1, nums2, nums1 = len_1, len_2, nums1, nums2

        if len_2 == 0:
            raise ValueError

        i_min, i_max, half_len = 0, len_2, (len_1 + len_2) / 2

        while i_min <= i_max:
            pass


if __name__ == '__main__':
    result = Solution().find_median_sorted_arrays([2, 3, 4], [2, 3, 4, 5, 6])
    assert result == None
    print(result)
