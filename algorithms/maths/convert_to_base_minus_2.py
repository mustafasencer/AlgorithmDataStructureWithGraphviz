"""
    Created by Mustafa Sencer Özcan on 25.05.2020.

    Given a number N, return a string consisting of "0"s and "1"s that represents its value in base -2 (negative two).

    The returned string must have no leading zeroes, unless the string is "0".
"""


class Solution:
    def solve(self, N):
        ans = []
        while N:
            ans.append(N & 1)
            N = (1 - N) >> 1
        return "".join(map(str, ans[::-1] or [0]))


if __name__ == '__main__':
    N = 20
    Solution().solve(N)
