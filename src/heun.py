import math

def heun(f, x0, y0, h, n):
    r = []
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h, y0 + h * m1)
        y1 = y0 + h * (m1 + m2) /2
        x0 += h
        y0 = y1
        r.append((x0, y0))
    return r

def f(x, y):
    return 1 + x * y

def g(x, y):
    return y*(1 - x) + x + 2

def h(x, y):
    return y * math.cos(x) + 1

def m(x, y):
    return y + math.exp(-x**2) + 3

if __name__ == '__main__':

    x0 = 0.1724
    y0 = 1.10093
    r = heun(m, x0, y0, h=0.18617, n=10)

    x, y = zip(*r)

    for i in range(len(r)):
        print(f'x_{i + 1} = {x[i]}\ny_{i + 1} = {y[i]}\n')

