import numpy as np
import matplotlib.pyplot as plt

# f1(x) = 1, f2(x)=x, f3(x)=(3x^2-1)/2 em C[-1, 1]

n5 = [(0.9061798459, 0.2369268850), (0.5384693101, 0.4786286705), (0.0000000000, 0.5688888889),
      (-0.5384693101, 0.4786286705), (0.9061798459, 0.2369268850)]


def f(x):
    if x >= 0:
        return 1
    return 2


def quadrature(f, lista_de_pontos_e_pesos):
    # serve apenas para integrais no intervalo [-1, 1]
    soma = 0
    for x_k, c_k in lista_de_pontos_e_pesos:
        soma += c_k * f(x_k)
    return soma


def f1(x): return 1
def f2(x): return x
def f3(x): return (3 * x ** 2 - 1) / 2


def coeffs_best_func(f, a, b, fs):
    if a != -1 or b != 1:
        raise ValueError('a deve ser -1 e b deve ser 1, realize uma mudança de variáveis')
    coeffs = []
    for k in range(len(fs)):
        # ck = integral de f*fk em [a, b] dividido por integarl de fk * fk em [a, b]
        def ffk(x):
            return f(x) * fs[k](x)

        def fkfk(x):
            return fs[k](x) ** 2
        ck = quadrature(ffk,  n5) / quadrature(fkfk, n5)
        coeffs.append(ck)
    return coeffs


if __name__ == '__main__':

    fs = [f1, f2, f3]
    a, b = [-1, 1]
    coeffs = coeffs_best_func(f, a, b, fs)
    print(coeffs)

    def g(x):
        s = 0
        for k, ck in enumerate(coeffs):
            s += ck * fs[k](x)
        return s

    t = np.linspace(a, b, 100)
    ft = [f(i) for i in t]
    gt = [g(i) for i in t]

    plt.plot(t, ft, label="funcao f")
    plt.plot(t, gt, label="funcao g")
    plt.legend()
    plt.savefig('best_func_ortho.png')


