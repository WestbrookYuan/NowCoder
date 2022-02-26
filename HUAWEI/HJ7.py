n = int(input())
indexs = []
values = []
for i in range(n):
    line = input()
    line = line.split(" ")
    indexs.append(int(line[0]))
    values.append(int(line[1]))
dice = {}
for i in range(len(indexs)):
    if not indexs[i] in dice:
        dice[indexs[i]] = values[i]
    else:
        dice[indexs[i]] += values[i]

for i,j in sorted(dice.items()):
    print(f'{i} {j}')