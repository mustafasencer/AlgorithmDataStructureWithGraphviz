class Solution:
    def reverseBits(self, number: int) -> int:
        output = 0
        i = 0
        while i < 32:
            output = output << 1
            if number & 1 == 1:
                output = output | 1
            number = number >> 1
            i += 1
        return output


if __name__ == "__main__":
    result = Solution().reverseBits(4294967293)
    print(result)
