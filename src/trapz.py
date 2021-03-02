import math

def trapz(f, a, b, n):

    h = (b - a) / n
    soma = 0
    for k in range(1, n):
        soma += f(a + k * h)
    soma *= 2
    soma += (f(a) + f(b))
    soma *= (h/2)

    return soma

def f(x):
    return  math.exp(-x ** 2)

def g(x):
    return math.cos(x ** 2)

if __name__ == '__main__':

    a = 0
    b = 1

    n = 10

    r = trapz(f, a, b, n)
    print(r)