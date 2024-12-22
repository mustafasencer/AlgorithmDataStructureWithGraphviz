from typing import List


def solution(nums1: List[int], nums2: List[int]) -> float:
    """
    1. No explanation! (Hard)
    """
    len_1, len_2 = len(nums1), len(nums2)
    if len_1 > len_2:
        len_2, len_1, nums2, nums1 = len_1, len_2, nums1, nums2

    if len_2 == 0:
        raise ValueError

    i_min, i_max, _half_len = 0, len_2, (len_1 + len_2) / 2

    while i_min <= i_max:
        pass


if __name__ == "__main__":
    result = solution([2, 3, 4], [2, 3, 4, 5, 6])
    assert result is None
    print(result)
