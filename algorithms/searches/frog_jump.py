"""
A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.

Count the minimal number of jumps that the small frog must perform to reach its target.

Write a function:

def solution(X, Y, D)

that, given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or greater than Y.

For example, given:

  X = 10
  Y = 85
  D = 30
the function should return 3, because the frog will be positioned as follows:

after the first jump, at position 10 + 30 = 40
after the second jump, at position 10 + 30 + 30 = 70
after the third jump, at position 10 + 30 + 30 + 30 = 100
Write an efficient algorithm for the following assumptions:

X, Y and D are integers within the range [1..1,000,000,000];
X ≤ Y.
"""


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def solution(K, M, A):
    # write your code in Python 3.6
    max_sum = 0
    min_sum = 0
    for item in A:
        max_sum += item
        min_sum = max(min_sum, item)

    result = min_sum

    while min_sum <= max_sum:
        mid_sum = int((max_sum + min_sum) / 2)

        ok = check_divisibility(mid_sum, K, A)

        if ok:
            result = mid_sum

            max_sum = mid_sum - 1

        else:
            min_sum = mid_sum + 1
    return result


def check_divisibility(mid_sum, K, A):
    remaining_block_count = K
    current_block_sum = 0

    for item in A:
        current_block_sum += item

        if current_block_sum > mid_sum:
            remaining_block_count -= 1
            current_block_sum = item

        if not remaining_block_count:
            return False

    return True


if __name__ == '__main__':
    K = 3
    M = 5
    A = [2, 1, 5, 1, 2, 2, 2]
    result = solution(K, M, A)
    print(result)
