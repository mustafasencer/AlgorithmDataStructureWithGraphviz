"""
nums non-empty array nums consisting of N integers is given. The array contains an odd number of elements, and each element of
the array can be paired with another element that has the same value, except for one element that is left unpaired.

For example, in array nums such that:

  nums[0] = 9  nums[1] = 3  nums[2] = 9
  nums[3] = 3  nums[4] = 9  nums[5] = 7
  nums[6] = 9
the elements at indexes 0 and 2 have value 9,
the elements at indexes 1 and 3 have value 3,
the elements at indexes 4 and 6 have value 9,
the element at index 5 has value 7 and is unpaired.
Write a function:

class Solution { public int solution(int[] nums); }

that, given an array nums consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.

For example, given array nums such that:

  nums[0] = 9  nums[1] = 3  nums[2] = 9
  nums[3] = 3  nums[4] = 9  nums[5] = 7
  nums[6] = 9
the function should return 7, as explained in the example above.

Write an efficient algorithm for the following assumptions:

N is an odd integer within the range [1..1,000,000];
each element of array nums is an integer within the range [1..1,000,000,000];
all but one of the values in nums occur an even number of times.
"""


def solution(nums):
    """
    1. loop over and store the item in an hash table
    2. find the element not divisible by 2.
    """
    lookup = {}
    for item in nums:
        lookup[item] = lookup.get(item, 0) + 1

    for key, value in lookup.items():
        if value % 2:
            return key
    return None


if __name__ == "__main__":
    nums = [9, 3, 9, 3, 9, 7, 9]
    result = solution(nums)
    assert result == 7
