# TODO: Complete in linear time xDD
def longest_palindrome(s):
    # Transform S into T.
    # For example, S = "abba", T = "^#a#b#b#a#$".
    # ^ and $ signs are sentinels appended to each end to avoid bounds checking
    separated_string = '#'.join('^{}$'.format(s))
    n = len(separated_string)
    P = [0] * n
    C = R = 0
    for i in range(1, n - 1):
        P[i] = (R > i) and min(R - i, P[2 * C - i])  # equals to i' = C - (i-C)
        # Attempt to expand palindrome centered at i
        while separated_string[i + 1 + P[i]] == separated_string[i - 1 - P[i]]:
            P[i] += 1

        # If palindrome centered at i expand past R,
        # adjust center based on expanded palindrome.
        if i + P[i] > R:
            C, R = i, i + P[i]

    # Find the maximum element in P.
    max_len, center_index = max((n, i) for i, n in enumerate(P))
    return s[(center_index - max_len) // 2: (center_index + max_len) // 2]


def helper(s, l, r):
    while l >= 0 and r < len(s) and s[r] == s[l]:
        l -= 1
        r += 1
    return s[l + 1: r]


class Solution:
    def test(self, string):
        pass

    def longest_palindrome(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            # handle the odd cases
            tmp = helper(s, i, i)
            if len(tmp) > len(result):
                result = tmp
            # handle the even cases
            tmp = helper(s, i, i + 1)
            if len(tmp) > len(result):
                result = tmp
        return result


if __name__ == '__main__':
    result = Solution().longest_palindrome("babad")
    print(result)
