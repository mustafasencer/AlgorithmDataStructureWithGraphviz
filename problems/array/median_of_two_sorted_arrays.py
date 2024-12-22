def solution(nums1: list[int], nums2: list[int]) -> float:
    """1. No explanation! (Hard)."""
    len_1, len_2 = len(nums1), len(nums2)
    if len_1 > len_2:
        len_2, len_1, nums2, nums1 = len_1, len_2, nums1, nums2

    if len_2 == 0:
        raise ValueError

    i_min, i_max, _ = 0, len_2, (len_1 + len_2) / 2

    while i_min <= i_max:
        return 1

    return 0


if __name__ == "__main__":
    result = solution([2, 3, 4], [2, 3, 4, 5, 6])
    if result is not None:
        raise ValueError
