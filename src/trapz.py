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

def h(x):
    return x**2 * math.cos(3*x**2)


if __name__ == '__main__':

    a = -0.953
    b = 1.209
    n = 128
    r = trapz(h, a, b, n)
    print(r)


    # intervalo = [-0.704, 0.513]
    # subintervalos = [1, 3, 7, 18, 42, 70, 129, 281, 507, 1042]
    # for i in range(len(subintervalos)):
    #     print(trapz(f, intervalo[0], intervalo[1], subintervalos[i]))

    # x = [0.79664, 1.51745, 1.70088, 3.75536, 3.82042, 4.52281, 4.61101, 4.86443, 4.99453]
    # y = [2.99248, 2.23076, 2.08935, 2.06027, 1.82852, 2.0813, 2.50914, 2.93904, 2.44177]
    # soma = 0
    # for i in range(len(x) - 1):
    #     def eq_reta(x_):
    #         m = (y[i+1] - y[i]) / (x[i+1] - x[i])
    #         n = y[i] - m * x[i]
    #         #print('m: ', m, ' | n: ', n)
    #         #print(f'({x[i]}, {y[i]}), ({x[i+1]}, {y[i+1]})')
    #         return m * x_ + n
    #
    #     soma += trapz(eq_reta, x[i], x[i+1], 1)
    #
    # print(soma)

