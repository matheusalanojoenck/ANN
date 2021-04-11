import matplotlib.pyplot as plt
import math

def f(x, y):
    return x ** 2 + math.cos(y)

def g(x, y):
    return y*(1 - x) + x + 2

def h(x, y):
    return y * math.cos(x) + 1

def euler_half(f, x0: float, y0: float, h: float, n: int):
    r = []
    for i in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h / 2, y0 + (h / 2) * m1)
        yk = y0 + h * m2
        y0 = yk
        x0 += h
        r.append((x0, y0))
    return r

if __name__ == '__main__':
    x0 = 0.727
    y0 = 1.95195
    r = euler_half(h, x0, y0, h=0.13307, n=10)

    x, y = zip(*r)

    for i in range(len(x)):
        print(f'x_{i+1} = {x[i]}\ny_{i+1} = {y[i]}\n')

    plt.scatter(x, y)
    plt.savefig('euler_half.png')