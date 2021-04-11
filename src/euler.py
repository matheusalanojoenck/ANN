import matplotlib.pyplot as plt
import numpy as np


def euler(f, x0: float, y0: float, h: float, n: int):
    xs, ys, = [], []
    for k in range(n):
        x = x0 + k * h
        y = y0 + h * f(x, y0)
        xs.append(x + h)
        ys.append(y)
        y0 = y
    return xs, ys


def f(x, y):
    return np.cos(x**2 + y + 1)

def g(x, y):
    return y*(1 - x) + x + 2

def h(x, y):
    return y * np.cos(x) + 1


if __name__ == '__main__':
    x0 = 0.74506
    y0 = 1.33292
    r = euler(h, x0, y0, h=0.1236, n=10)

    k = 1
    for x, y in zip(*r):
        print(f'x_{k} = {x}\ny_{k} = {y}\n')
        k += 1

    xs, ys = r
    plt.scatter(xs, ys)
    plt.savefig('euler.png')
