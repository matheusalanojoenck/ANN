from matplotlib import pyplot as plt
import numpy as np
import math

def lagrange(x, y):
    # a eq do polinomio de lagrange
    n = len(x)
    if n == len(y):
        eq = ''
        c = ''
        for k in range(n):
            number = '*'.join([f'(x{-xi:+})' for i, xi in enumerate(x) if i != k])
            denom = '*'.join([f'({x[k]}{-xi:+})' for i, xi in enumerate(x) if i != k])
            c = f'{y[k]:+}/({denom})' # coeficientes do polinominio de lagrange
            print(eval(c))
            eq += f'{y[k]:+}*({number})/({denom})'
        return eq
    else:
        raise TypeError('O numero de coordenadas x é diferente do numeor de coordenadas y')

if __name__ == '__main__':

    x = [0.016, 0.558, 0.946, 1.206, 1.562, 2.089, 2.65, 2.806, 3.091, 3.642, 3.899, 4.601, 4.853]  # coordenadas do ponto x
    y = [4.016, 4.519, 4.781, 4.886, 4.919, 4.723, 4.238, 4.067, 3.732, 3.078, 2.806, 2.301, 2.225]  # coordenadas do ponto y

    #eq = lagrange(x,y)

    # Fenomeno de Runge
    def f(x):
        return 4 + math.sin(x)-((x ** 2) / 30)
    def f1(x):
        return x**3 * math.exp(-x) * math.sqrt(math.cos(x**2) + 3)
    # num = 10
    # x2 = [-1 + (2/(num-1)) * i for i in range(num)]
    x2 = [1.74386, 2.94509, 5.11921, 6.24493]
    y2 = [f1(i) for i in x2]
    eq2 = lagrange(x2, y2)

    def subs(x):
        # o valor do polinomio de lagrange em um ponto x
        return eval(eq2)
    print('p(x) = ', eq2, '\n')

    # plot do grafico
    # t = np.linspace(0.184, 3.929, 100)
    #
    # plt.plot(t, subs(t), label='lagrange')
    # plt.plot(t, f(t), label='funçao')
    # plt.scatter(x2, y2)
    # plt.legend()
    # plt.savefig('langrange.png')
