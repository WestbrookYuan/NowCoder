def yanghui(line:str):
    line = int(line)
    row = line
    col = 2 * line + 1
    triangle = [[0 for j in range(col)] for i in range(row)]
    triangle[0][col//2] = 1
    for i in range(1, row):
        for j in range(1,col-1):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j] + triangle[i-1][j+1]
    for i in range(len(triangle[row-1])):
        if triangle[row-1][i] != 0 and triangle[row-1][i] % 2 == 0:
            return i
    return -1

# while True:
#     try:
#         print(yanghui(input()))
#     except:
#         break
print(yanghui(10000000000000000))
# import sys
#
# num = [int(n) for n in sys.stdin.read().split()]
# for i in num:
#     if i < 3:
#         print(-1)
#     elif i % 4 == 3 or i % 4 == 1:
#         print(2)
#     elif i % 4 == 0:
#         print(3)
#     elif i % 4 == 2:
#         print(4)