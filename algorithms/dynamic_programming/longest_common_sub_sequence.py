"""
Longest common sub sequence
"""


def lcs(str0, str1):
    m = len(str0)
    n = len(str1)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    """
    Following steps build L[m+1][n+1] in bottom up fashion 
    Note: L[i][j] contains length of LCS of X[0..i-1] 
    and Y[0..j-1]
    """
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif str0[i - 1] == str1[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


if __name__ == '__main__':
    X = "AGGTAB"
    Y = "GXTXAYB"
    result = lcs(X, Y)
    assert result == 4
