"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
"""


def solution(nums: list[int]) -> list[list[int]]:
    result = []
    nums.sort()
    length = len(nums)

    for i in range(length - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, length - 1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total < 0:
                l += 1
            elif total > 0:
                r -= 1
            else:
                result.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1

    return result


def solution_1(nums: list[int]) -> set:
    """
    1. loop over the nums array
    2. create left and right pointers and just move them according to the sum value
    3. if sum == 0 is found just add it to the set and move both pointers.
    """
    result = set()
    nums.sort()
    for i in range(1, len(nums) - 1):
        left, right = i - 1, i + 1

        while len(nums) > right > left >= 0:
            triplet_sum = nums[left] + nums[i] + nums[right]

            if triplet_sum > 0:
                left -= 1
                continue
            if triplet_sum < 0:
                right += 1
                continue
            result.add((nums[left], nums[i], nums[right]))
            right += 1
            left -= 1

    return result


if __name__ == "__main__":
    nums = [-1, -1, 1, 2, -1, -4, 2, -2, -3, 6]
    result = solution(nums)
    assert result == []
