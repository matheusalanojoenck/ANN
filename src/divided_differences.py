import matplotlib.pyplot as plt
import numpy as np
import math

def diveded_differnces(x, y):
    Y = [item for item in y] # vai mudando a cada iteração
    n = len(y)
    coeffs = [y[0]] + [0] * (n - 1)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            numer = Y[j + 1] - Y[j]
            denom = x[j + 1 + i] - x[j]
            Y[j] = numer / denom
        coeffs[i + 1] = Y[0]
    return coeffs

def eq(x, coeffs):
    """
    Constroi uma equação do tipo
    a0 + a1*(x-x1) + a2*(x-x1)*(x-x2) + a3*(x-x1)*(x-x2)*(x-x3)
    """

    n = len(x)
    equation = ''
    for i in range(n):
        print(f'a{i} = ', coeffs[i])
        sign = ''
        if i != 0:
            sign = "*"
        equation += f'{coeffs[i]:+}{sign}' + '*'.join([f'(x{-xj:+})' for j, xj in enumerate(x) if j < i])
    return  equation

def f(x):
    return math.exp(math.cos(x) ** 2) + math.exp(-x ** 2) + math.log(x)

if __name__ == '__main__':

    x = [2.243, 3.653, 4.304, 7.367, 8.613]
    #y = [4.22, 4.668, 4.757, 4.911, 4.885, 4.664, 4.018, 3.716, 3.209, 2.642, 2.577, 2.271, 2.208, 2.346, 2.439, 2.837, 2.94]

    y = [0] * len(x)
    for i in range(len(x)):
        y[i] = f(x[i])

    coeffs = diveded_differnces(x, y)

    print(coeffs)
    poly = eq(x, coeffs)
    print('p(x) = ', poly)

    t = np.linspace(min(x), max(x), 100)
    def p(x):
        return eval(poly)

    plt.plot(t, p(t))
    plt.scatter(x, y, zorder=10)
    plt.savefig("div_diff.png")

