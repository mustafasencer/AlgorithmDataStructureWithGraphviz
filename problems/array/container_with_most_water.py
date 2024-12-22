"""Calculate max area based on the item at index i and the difference between i and j."""


def solution(height: list[int]) -> int:
    """1."""
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


def solution_2(height):
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


if __name__ == "__main__":
    result_ = solution([1, 8, 6, 2, 5, 4, 8, 3, 7])
    result = solution_2([1, 8, 6, 2, 5, 4, 8, 3, 7])
    assert result == result_
