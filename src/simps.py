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

    x = [0.461, 0.851, 1.241, 1.5515, 1.862, 2.002, 2.142, 2.569, 2.996, 3.1765, 3.357, 3.584, 3.811, 4.3935, 4.976]
    y = [2.698, 2.969, 2.545, 2.2, 2.019, 2.0, 2.02, 2.318, 2.837, 2.983, 2.964, 2.591, 1.862, 1.474, 2.538]
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

