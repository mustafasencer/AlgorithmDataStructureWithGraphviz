from typing import List


def solution(nums: List[int]) -> bool:
    """
    1. loop over the array
    2. check if any index has a circular path
    3. if local set has the index stored then the circularity is confirmed
    """
    is_seen = set()

    for i in range(len(nums)):

        while True:
            local = set()

            if i in is_seen:
                break
            if i in local:
                return True

            is_seen.add(i)
            local.add(i)

            prev = i
            i = (i + nums[i]) % len(nums)
            if prev == i or (nums[i] > 0) != (nums[prev] > 0):
                break

    return False


if __name__ == "__main__":
    nums = [2, 3, 1, 4, 0]
    result = solution(nums)
    assert result is True
    print(result)
