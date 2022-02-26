import numpy as np
def compute(matrix1: list, matrix2: list):
    new_martix = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(new_martix)):
        for j in range(len(new_martix[0])):
            for k in range(len(matrix1[0])):
                new_martix[i][j] += matrix1[i][k]* matrix2[k][j]

    print(new_martix)
m1 = [[1, 2, 3],
      [3, 2, 1]]
m2 = [[1, 2],
      [2, 1],
      [3, 3]]

compute(m1, m2)

m1 = np.array(m1)
m2 = np.array(m2)
print(m1.dot(m2))