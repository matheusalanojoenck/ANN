from matplotlib import pyplot as plt
import numpy as np

def lagrange(x, y):
    # a eq do polinomio de lagrange
    n = len(x)
    eq = ''
    if n == len(y):
        for k in range(n):
            number = '*'.join([f'(x{-xi:+})' for i, xi in enumerate(x) if i != k])
            denom = '*'.join([f'({x[k]}{-xi:+})' for i, xi in enumerate(x) if i != k])
            eq += f'{y[k]:+}*({number})/({denom})'
        return eq
    else:
        raise TypeError('O numero de coordenadas x é diferente do numeor de coordenadas y')

if __name__ == '__main__':

    x = [1, 2, 3, 3.2, 4.1, 5.7]  # coordenadas do ponto x
    y = [2, 5, 1, 2, 1, 10]  # coordenadas do ponto y

    eq = lagrange(x,y)

    # Fenomeno de Runge
    def f(x):
        return 1 / (1 + 25 * x ** 2)
    num = 20
    x2 = [-1 + (2/(num-1)) * i for i in range(num)]
    y2 = [f(i) for i in x2]
    eq2 = lagrange(x2, y2)

    def subs(x):
        # o valor do polinomio de lagrange em um ponto x
        return eval(eq2)
    print('p(x) = ', eq2, '\n')

    # plot do grafico
    t = np.linspace(-1, 1, 200)

    plt.plot(t, subs(t), label='lagrange')
    plt.plot(t, f(t), label='funçao')
    plt.scatter(x2, y2)
    plt.legend()
    plt.savefig('langrange.png')
