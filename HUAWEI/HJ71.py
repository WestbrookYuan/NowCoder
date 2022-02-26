def match(string:str, rule:str):
    dp = [[False for _ in range(len(string) + 1)] for _ in range(len(rule) + 1)]
    dp[0][0] = True
    for i in range(1, len(rule)+1):
        if rule[i-1] == "*":
              dp[i][0] = True
        else:
            break
    for i in range(1, len(rule)+1):
        for j in range(1, len(string)+1):
            if rule[i-1] == "*":
                dp[i][j] = dp[i-1][j] or dp[i][j-1]
            elif rule[i-1] == "?" and string[j-1].isalnum():
                dp[i][j] = dp[i-1][j-1]
            elif rule[i-1].lower() == string[j-1].lower():
                dp[i][j] = dp[i-1][j-1]
    return dp[len(rule)][len(string)]


while True:
    try:
        pattern, string = input(), input()
        if match(string, pattern):
            print('true')
        else:
            print('false')
    except:
        break