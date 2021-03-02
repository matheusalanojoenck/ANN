import math

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

    a = 0
    b = 1

    # o número de parábolas é metade de n
    n = 6

    r = simps(f, a, b, n)
    print(r)
