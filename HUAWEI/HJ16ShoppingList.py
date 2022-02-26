given = input().split()

money = int(given[0])
number = int(given[1])

primarys = {}
accessory = {}

for i in range(1, number + 1):
    price, importance, main = map(int, input().split())
    if main == 0:
        primarys[i] = [price, importance]
    else:
        if main in accessory:
            accessory[main].append([price, importance])
        else:
            accessory[main] = [[price, importance]]

weights = [[]]
value = [[]]
number = len(primarys)
dp = [[0] * (money + 1) for _ in range(number + 1)]

for key in primarys:
    w_temp, v_temp = [], []  # 只有主件
    w_temp.append(primarys[key][0])
    v_temp.append(primarys[key][0] * primarys[key][1])

    if key in accessory:  # 附件1
        w_temp.append(w_temp[0] + accessory[key][0][0])
        v_temp.append(v_temp[0] + accessory[key][0][0] * accessory[key][0][1])
        if len(accessory[key]) > 1:  # 附件2
            w_temp.append(w_temp[0] + accessory[key][1][0])
            v_temp.append(v_temp[0] + accessory[key][1][0] * accessory[key][1][1])
            w_temp.append(w_temp[0] + accessory[key][0][0] + accessory[key][1][0])
            v_temp.append(
                v_temp[0] + accessory[key][0][0] * accessory[key][0][1] + accessory[key][1][0] * accessory[key][1][1])
    weights.append(w_temp)
    value.append(v_temp)

for i in range(1, number + 1):
    for j in range(10, money + 1):
        max_temp = dp[i - 1][j]
        for k in range(len(weights[i])):
            if (j - weights[i][k]) >= 0:
                max_temp = max(max_temp, dp[i - 1][j - weights[i][k]] + value[i][k])
        dp[i][j] = max_temp
print(dp[number][money])
