# basta aplicar o metodo de extrapolaçao de Richardson sobree a formula da Regra dops Trapwzios
import math

def trapz(f, a, b, h):

    soma = 0.0
    n = int((b - a) / h)
    for k in range(1, n):
        soma += f(a + k * h)
    return (h/2) * (f(a) + 2 * soma + f(b))

def romberg(col1):
    col1 = [item for item in col1] # copia coluna 1
    n = len(col1)
    for j in range(n - 1):
        temp_col = [0] * (n - 1 - j)
        for i in range(n - 1 - j):
            power = j + 1 # é igual o numero da coluna anterior
            temp_col[i] = (4 ** power * col1[i + 1] - col1[i]) / (4 ** power - 1)
        col1[:n - 1 - j] = temp_col
        print(f'F_{j+2}', temp_col)
    return col1[0] # a aproximacao procurada

def f0(x):
    return math.exp(-x**2)

def f1(x):
    return math.sin(x / math.sqrt(x**2 + 1)) + 1

def f2(x):
    return math.sqrt(1 + math.cos(x)**2)

def f3(x):
    return math.sqrt(math.sin(math.cos(math.log(x**2 + 1) + 2) + 3) + 4)

def f4(x):
    return math.sin(math.exp(-x ** 2)) + 1

if __name__ == '__main__':

    a, b = [0.854, 1.854]

    h = 1.0
    k = 2
    hs = [h/2 ** i for i in range(k)]

    col1 = [trapz(f0, a, b, hi) for hi in hs]
    print('F_1', col1)
    r = romberg(col1)
    s = f'o numero {r} é uma aproximacao  para integral de exp(-x^2) em [{a}, {b}] com erro O(h^({2*k}))'
    print(s)

