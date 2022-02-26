def computeTime():
    number = int(input())
    matrixs = {}
    result = 0
    for i in range(number):
        matrixs[chr(ord('A') + i)] = list(map(int, input().strip().split()))
    s = input()
    temp = []
    for i in s:
        if i != ")":
            temp.append(i)
        else:
            c = temp.pop()
            b = temp.pop()
            result += matrixs[b][0] * matrixs[b][1] * matrixs[c][1]
            temp.pop()
            matrixs[b] = [matrixs[b][0], matrixs[c][1]]
            temp.append(b)
    print(result)

while True:
    try:
        computeTime()
    except:
        break