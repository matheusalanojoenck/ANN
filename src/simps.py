import math
import numpy as np

def f(x):
    return math.exp(-x ** 2)

def simps(f, a, b, n):

    h = (b - a) / n
    if n % 2 != 0 or n <= 0:
        raise ValueError("n tem de ser par e positivo")

    soma_odd, soma_even = 0, 0
    for k in range(1 ,n, 2):
        soma_odd += f(a + k * h)
    for k in range(2, n, 2):
        soma_even += f(a + k * h)
    return (h / 3) * (f(a) + 4 * soma_odd + 2 * soma_even + f(b))



if __name__ == '__main__':

    # a = 0
    # b = 1
    # # o número de parábolas é metade de n
    # n = 6
    # r = simps(f, a, b, n)
    # print(r)

    # intervalo = [-0.753, 1.172]
    # subintervalos = [2, 4, 8, 18, 42, 70, 132, 276, 552, 1096]
    # for i in range(len(subintervalos)):
    #     print(simps(f, intervalo[0], intervalo[1], subintervalos[i]))

    x = [0.13573, 0.32679, 0.51785, 1.307905, 2.09796, 3.225485, 4.35301, 4.38408, 4.41515]
    y = [1.67226, 2.33534, 2.81039, 2.46089, 2.0096, 2.99762, 1.3209, 1.4359, 1.56482]
    soma = 0
    for i in range(0,(len(x) - 2), 2):
        if (x[i+1] - x[i]) == (x[i+2] - x[i+1]):
            soma += ((x[i+1] - x[i]) / 3) * (y[i] + 4*y[i+1] + y[i+2])
        else:
            A = np.array([[x[i]**2, x[i], 1], [x[i+1]**2, x[i+1], 1], [x[i+2]**2, x[i+2], 1]])
            B = np.array([y[i], y[i+1], y[i+2]])
            abc = np.linalg.solve(A, B)
            def parabola_eq(x):
                return abc[0] * x**2 + abc[1] * x + abc[2]
            soma += simps(parabola_eq, x[i], x[i+2], 2)
    print(soma)

