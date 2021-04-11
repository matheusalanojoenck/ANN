import math

def ralston(f, x0, y0, h, n):
    r = []
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + (3/4) * h, y0 + (3/4) * h * m1)
        yk = y0 + h * (m1 + 2 * m2) / 3
        x0 += h
        y0 = yk
        r.append((x0, y0))
    return r

def f(x, y):
    return 1 + x * y

def g(x, y):
    return y*(1 - x) + x + 2

def h(x, y):
    return y * math.cos(x) + 1

if __name__ == '__main__':

    x0 = 0.40967
    y0 = 1.89727
    r = ralston(h, x0, y0, h=0.14777, n=10)

    x, y = zip(*r)

    for i in range(len(r)):
        print(f'x_{i + 1} = {x[i]}\ny_{i + 1} = {y[i]}\n')