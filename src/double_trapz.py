import math

def double_trapz(f, a: float, b: float, c: float, d: float, n1: int, n2: int) -> float:
    if n1 <= 0 or n2 <= 0:
        raise ValueError('n1 ou n2 menores/iguais a zero')
    h1 = (b - a) / n1
    h2 = (d - c) / n2
    soma_interior = 0
    for i in range(1, n1):
        for j in range(1, n2):
            soma_interior += f(a + i * h1, c + j * h2)
    soma_arestas_horizontais = 0
    for i in range(1, n1):
        for j in [0, n2]:
            soma_arestas_horizontais += f(a + i * h1, c + j * h2)
    soma_arestas_verticais = 0
    for j in range(1, n2):
        for i in [0, n1]:
            soma_arestas_verticais += f(a + i * h1, c + j * h2)
    soma_verticies = 0
    for i in [0, n1]:
        for j in [0, n2]:
            soma_verticies += f(a + i * h1, c + j * h2)
    return (h1 * h2 / 4) * (soma_verticies + 4 * soma_interior + 2 * (soma_arestas_horizontais + soma_arestas_verticais))


def f(x, y):
    return math.exp(-(x + y) ** 2)

def g(x, y):
    return math.sqrt(x**2 + y**4)

def t(x, y):
    return math.cos(x + math.log(y**2 + 1)) ** 2

def q(x, y):
    return math.sqrt(1 + math.sin(x**2 + math.cos(y)))

def m(x, y):
    return math.sin(x**2 + y**2 + 1) + 2

if __name__ == '__main__':
    a, b = [-0.91, 0.917]
    c, d =  [-0.716, 0.851]
    n1, n2 = 248, 123

    r = double_trapz(m, a, b, c, d, n1, n2)
    print(r)
    # print(0.1010133843750915)
    # print((abs(r - 0.1010133843750915)))