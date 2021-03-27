import numpy as np
import matplotlib.pyplot as plt
import math

def spline(x, y):
    """
    Retorna todos os coeficientes de todos os polinomios
    ou seja, todos os ak, bk, ck, dk
    """
    n = len(x)
    a = {k: v for k, v in enumerate(y)}
    h = {k: x[k + 1] - x[k] for k in range(n - 1)}

    A = [[1] + [0] * (n - 1)]
    for i in range(1, n - 1):
        row = [0] * n
        row[i - 1] = h[i - 1]
        row[i] = 2 * (h[i - 1] + h[i])
        row[i + 1] = h[i]
        A.append(row)
    A.append([0] * (n - 1) + [1])

    B = [0]
    for k in range(1, n - 1):
        row = 3 * (a[k + 1] - a[k]) / h[k] - 3 * (a[k] - a[k - 1]) / h[k - 1]
        B.append(row)
    B.append(0)

    c = dict(zip(range(n), np.linalg.solve(A, B)))

    b = {}
    d = {}
    for k in range(n - 1):
        b[k] = (1/h[k]) * (a[k + 1] - a[k]) - (h[k]/3) * (2*c[k]+c[k+1])
        d[k] = (c[k+1] - c[k]) / (3*h[k])

    s = {}
    for k in range(n - 1):
        print(f'a{k} = {a[k]} | b{k} = {b[k]} | c{k} = {c[k]} | d{k} = {d[k]}')
        eq = f'{a[k]}{b[k]:+}*(x{-x[k]:+}){c[k]:+}*(x{-x[k]:+})**2{d[k]:+}*(x{-x[k]:+})**3'
        s[k] = {'eq': eq, 'domain': [x[k], x[k+1]]}

    return s

def f(x):
    return math.exp(-x ** 2) + math.cos(x) + 3


if __name__ == '__main__':

    # pontos = [[-7.025, 1.679], [-5.383, 3.818], [-3.077, 3.62], [-1.387, 2.953], [-0.076, 3.924], [1.966, 4.794], [2.303, 4.567], [4.621, 2.292], [5.89, 2.46], [7.713, 3.007], [9.652, 0.669], [11.965, -1.338], [12.886, -1.221]]
    # x = [0] * len(pontos)
    # y = [0] * len(pontos)
    # for i in range(len(pontos)):
    #     x[i] = pontos[i][0]
    #     y[i] = pontos[i][1]

    x = [0.622, 2.738, 3.926, 5.779]
    y = [f(i) for i in x]

    eqs = spline(x, y)

    #xn = [-4.719, -4.403, -1.99, -0.784, 11.161]

    for key, value in eqs.items():
        def p(x):
            return eval(value['eq'])
        t = np.linspace(*value['domain'], 100)
        plt.plot(t, p(t), label=f"$S_{key}(x)$")
        # for i in range(len(xn)):
        #     if xn[i] > value['domain'][0] and xn[i] < value['domain'][1]:
        #         #print(i, 'equaçao', ' | ponto:  ',  xn[i], '| domain', value['domain'])
        #         print(p(xn[i]))

    plt.scatter(x, y)
    plt.legend()
    plt.savefig('spline.png')

