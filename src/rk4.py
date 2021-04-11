import math

def rk4(f, x0, y0, h, n):
    r = []
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h/2, y0 + (h/2) * m1)
        m3 = f(x0 + h/2, y0 + (h/2) * m2)
        m4 = f(x0 + h, y0 + h * m3)
        yk = y0 + h * (m1 + 2 * m2 + 2 * m3 + m4) / 6
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

    x0 = 0.57727
    y0 = 1.82833
    r = rk4(h, x0, y0, h=0.12316, n=10)

    x, y = zip(*r)

    for i in range(len(r)):
        print(f'x_{i + 1} = {x[i]}\ny_{i + 1} = {y[i]}\n')