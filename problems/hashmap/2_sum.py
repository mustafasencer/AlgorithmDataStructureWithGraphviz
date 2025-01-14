def solution(nums: list[int], target: int) -> list[int] | None:
    dict_ = {}
    for i, value in enumerate(nums):
        n = target - value
        if n in dict_:
            return [dict_[n], i]
        dict_[value] = i
    return None


def solution_1(nums: list[int], target: int) -> list[int] | None:
    lookup = {}
    for i in range(len(nums)):
        remaining = target - nums[i]

        if remaining in lookup:
            return [lookup[remaining], i]
        lookup[nums[i]] = i
    return None


if __name__ == "__main__":
    result = solution([2, 7, 11, 15], 9)
    result_2 = solution_1([2, 7, 11, 15], 9)
    assert result == result_2
