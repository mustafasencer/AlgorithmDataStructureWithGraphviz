"""Created by Mustafa Sencer Özcan on 22.05.2020."""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if "abc" in "abdc":
            return "yes"

        return "no"


if __name__ == "__main__":
    result = Solution().minWindow("ADOBECODEBANC", "ABC")
