import random
import matplotlib.pyplot as plt
import numpy as np
import math
from typing import List

def modelo(x):
    return 2 * math.exp(0.3 * x) + 3 * random.random()

# a, b = 0, 10
# x = a + (b - a) * np.random.rand(50)
# x.sort()
# y = [modelo(xi) for xi in x]


x = [0.0251, 0.6401, 0.8416, 1.1842, 1.72, 2.0679, 2.3642, 2.854]
y = [2.2251, 4.7429, 5.4953, 6.3624, 11.3061, 15.0322, 19.9302, 31.3503]

def best_exp(x: List[float], y: List[float]):
    sum_x = sum(x)
    sum_x2 = sum(xi ** 2 for xi in x)
    A = [[len(x), sum(x)], [sum_x, sum_x2]]
    y_ = [math.log(yi) for yi in y]
    sum_xy = sum(xi * yi for xi, yi in zip(x, y_))
    B = [sum(y_), sum_xy]
    a0, a1 = np.linalg.solve(A, B)
    a, b = math.exp(a0), a1
    return a, b

a, b = best_exp(x, y)

def bexp(x):
    return a * math.exp(b * x)

if __name__ == '__main__':

    print(a, b)
    t = np.linspace(min(x), max(x), 100)
    bexpt = [bexp(i) for i in t]
    plt.plot(t, bexpt)
    plt.scatter(x, y)
    plt.savefig('pontos_exp.png')
