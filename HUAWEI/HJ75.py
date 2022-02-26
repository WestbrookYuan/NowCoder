def publicSubstring(str1: str, str2: str):
    m = len(str1)
    n = len(str2)
    maxlen = 0
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[j - 1] == str2[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if maxlen < dp[i][j]:
                    maxlen = dp[i][j]
    return maxlen


print(publicSubstring("asdfas", "werasdfaswer"))
