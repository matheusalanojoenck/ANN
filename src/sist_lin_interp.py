import math
import numpy as np

def f(x):
    return x**3 * math.exp(-x) * math.sqrt(math.cos(x**2) + 2)

if __name__ == '__main__':
    p = 3 + 1
    # pontos = [[1.365, 4.917], [2.291, 4.577], [3.749, 2.961], [5.234, 2.22], [6.972, 3.015]]
    x = [1.30143, 2.91645, 5.27773, 6.63686]
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
    print(coeffs)