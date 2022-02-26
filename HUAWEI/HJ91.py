def findroute(string: str):
    [n, m] = list(map(int, string.strip().split()))
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = 1
    for j in range(n + 1):
        dp[0][j] = 1
    dp[0][0] = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m][n]


print(findroute("1 2"))
