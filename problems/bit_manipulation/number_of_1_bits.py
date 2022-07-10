"""
    Created by Mustafa Sencer Özcan on 27.05.2020.

    Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).
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


if __name__ == "__main__":
    result = Solution().hammingWeight(23)
    print(result)
