"""
https://leetcode.com/problems/word-pattern/
"""


def solution(nums, pattern):
    lookup = {}

    nums = nums.split(" ")
    if len(nums) != len(pattern):
        return False

    for i, word in enumerate(nums):
        if word in lookup:
            pattern_letter = lookup[word]
            if pattern_letter == pattern[i]:
                continue
            else:
                return False
        else:
            lookup[word] = pattern[i]

    return True


if __name__ == '__main__':
    nums = "dog cat cat dog"
    pattern = "abba"
    solution(nums, pattern)
