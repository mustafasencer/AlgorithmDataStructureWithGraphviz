"""
For a given array nums of N integers and a sequence S of N integers from the set {−1, 1}, we define val(nums, S) as follows:

val(nums, S) = |sum{ nums[i]*S[i] for i = 0..N−1 }|

(Assume that the sum of zero elements equals zero.)

For a given array nums, we are looking for such a sequence S that minimizes val(nums,S).

Write a function:

def solution(nums)

that, given an array nums of N integers, computes the minimum value of val(nums,S) from all possible values of val(nums,S) for all possible sequences S of N integers from the set {−1, 1}.

For example, given array:

  nums[0] =  1
  nums[1] =  5
  nums[2] =  2
  nums[3] = -2
your function should return 0, since for S = [−1, 1, −1, 1], val(nums, S) = 0, which is the minimum possible value.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..20,000];
each element of array nums is an integer within the range [−100..100].
"""


def solution(nums):
	N = len(nums)
	M = 0

	for i in range(N):
		nums[i] = abs(nums[i])
		M = max(nums[i], M)

	S = sum(nums)
	count = [0] * (M + 1)

	for i in range(N):
		count[nums[i]] += 1
	dp = [-1] * (S + 1)

	dp[0] = 0

	for a in range(1, M + 1):
		if count[a] > 0:
			for j in range(S):
				if dp[j] >= 0:
					dp[j] = count[a]
				elif j >= a and dp[j - a] > 0:
					dp[j] = dp[j - a] - 1

	result = S
	for i in range(S // 2 + 1):
		if dp[i] >= 0:
			result = min(result, S - 2 * i)

	return result


if __name__ == "__main__":
	nums = []
	result = solution(nums)
	assert result == 0
