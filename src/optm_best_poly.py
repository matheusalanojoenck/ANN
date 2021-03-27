import numpy as np
from typing import List

def best_poly(x: List[float], y: List[float], k):
    A = []
    B = []
    k += 1
    n = len(x)

    for m in range(k):
        soma_xy = 0
        row = []
        for j in range(k):
            soma_x = 0
            for i in range(n):
                soma_x += x[i] ** (j+m)
            row.append(soma_x)
        for i in range(n):
            soma_xy += y[i]*(x[i] ** m)
        B.append(soma_xy)
        A.append(row)

    coeffs = np.linalg.solve(A, B)

    return coeffs

if __name__ == '__main__':
    x = [-3.5587, -3.076, -1.1056, -0.2392, 0.8796, 1.1445, 2.1264, 4.0298]
    y = [6.7833, 7.7406, 4.1749, 4.5008, 6.278, 6.1979, 4.6112, 4.8515]
    k = 5
    coeffs = best_poly(x, y, k)
    print(coeffs)
