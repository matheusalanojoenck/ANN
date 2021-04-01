import math
import numpy as np
from typing import List


def px(coeffs_: List[float], x_):
    soma = 0
    for j in range(len(coeffs_)):
        soma += coeffs_[j] * x_**j
    return soma

def f(x):
    return 4 + math.sin(x) - ((x**2) / 30)

if __name__ == '__main__':
    p = 8 + 1
    # x = [0.551, 0.631, 1.113, 2.032, 2.429, 3.308, 3.862, 3.952, 4.7]
    # y = [4.513, 4.577, 4.856, 4.758, 4.457, 3.47, 2.843, 2.755, 2.264]
    # values = [0.858, 1.077, 2.175, 2.344, 2.777, 3.871]

    # pontos = [[0.641,4.584] , [0.882,4.746], [1.677,4.901], [2.989,3.854], [3.313,3.464], [4.137,2.591], [4.709,2.261], [5.927,2.48], [6.474,2.793]]

    x = [0.327, 0.637, 1.512, 1.852, 2.252, 3.122, 3.686, 4.074, 4.48]
    values = [0.461, 0.625, 1.351, 2.014, 2.634, 3.975]
    y = [f(i) for i in x]

    pontos = []
    for i in range(len(x)):
        row = [x[i], y[i]]
        pontos.append(row)

    A = []
    B = []
    for i in range(p):
        row = []
        B.append(pontos[i][1])
        for j in range(p):
            row.append(pontos[i][0] ** j)
        A.append(row)
    # print(A)
    # print(B)

    coeffs = np.linalg.solve(A, B)
    print(list(coeffs))
    for i in values:
        print(abs(f(i) - px(coeffs, i)))
        # print(px(coeffs, values[i]))