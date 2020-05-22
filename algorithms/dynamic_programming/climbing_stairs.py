"""
    Created by Mustafa Sencer Özcan on 22.05.2020.
"""


class Solution:
    def climbStairs(self, n: int) -> int:
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
    result = Solution().climbStairs(8)
    print(result)
