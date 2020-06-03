"""
    Created by Mustafa Sencer Özcan on 22.05.2020.

    You are climbing a stair case. It takes n steps to reach to the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

    Note: Given n will be a positive integer.
"""


class Solution:
    def climb_stairs(self, n: int) -> int:
        if n == 0:
            return 0
        a = 0
        b = 1
        for _ in range(n):
            c = a + b
            a = b
            b = c
        return b


if __name__ == '__main__':
    result = Solution().climb_stairs(8)
    print(result)
