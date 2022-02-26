def Levenshtein(s1: str, s2: str):
    dp = [[1 for j in range(len(s1) + 1)] for i in range(len(s2) + 1)]
    for i in range(len(s1) + 1):
        dp[0][i] = i
    for i in range(len(s2) + 1):
        dp[i][0] = i

    for i in range(1, len(s2) + 1):
        for j in range(1, len(s1) + 1):
            if s2[i - 1] == s1[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
    print(dp[len(s2)][len(s1)])


while True:
    try:
        Levenshtein(input(), input())
    except:
        break
