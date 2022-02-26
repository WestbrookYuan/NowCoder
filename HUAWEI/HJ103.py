def Redraiment(spots: list):
    if len(spots) == 1:
        return 1

    dp = [1 for _ in spots]
    for i in range(1, len(spots)):
        for j in range(i):
            if spots[i] > spots[j]:
                dp[i] = max(spots[i], spots[j] + 1)
    return max(dp)



