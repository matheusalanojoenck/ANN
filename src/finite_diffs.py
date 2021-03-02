import  random
import numpy as np

def prod(lst):
    p = 1
    for i in lst:
        p *= i
    return p

def finite_diffs(xs, ordem, x0, f):
    A = []
    B = []
    n = len(xs)
    for i in range(n):
        # para construir a matraiz A
        A.append([0] * n)
        for j in range(n):
            A[i][j] = xs[j] ** i

        # para construir a matraiz B
        potencias = [k + 1 for k in range(i - ordem, i)]
        fatorial = 0 if i < ordem else prod(potencias)
        termo = fatorial * x0 ** (i - ordem)
        B.append(termo)
    A = np.array(A, dtype='float')
    B = np.array(B, dtype='float')
    cs = np.linalg.solve(A, B)

    # para construir a som que da a aproximaçao
    soma = 0
    for ck, xk in zip(cs, xs):
        soma += ck * f(xk)
    return soma


def f(x):
    return x ** x

if __name__ == '__main__':
    x0 = 1.4827
    ordem = 3

    # pontos para construir formula
    num_pontos = 15
    a = x0 - 0.23423442342
    b = x0 + 0.12313453
    xs = [a + (b - a) * random.random() for _ in range(num_pontos)]
    xs.sort()

    r = finite_diffs(xs, ordem, x0, f)
    print(xs)
    print(f'aproximacao para a derivada de ordem {ordem} de f no ponto {x0}', r)
