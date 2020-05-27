"""
    Created by Mustafa Sencer Özcan on 27.05.2020.
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        i = 0
        while i < 32:
            if n & 1 == 1:
                result += 1
            n = n >> 1
            i += 1
        return result


if __name__ == '__main__':
    result = Solution().hammingWeight(23)
    print(result)
