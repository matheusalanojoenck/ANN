import math

def richardson(col1):
    col1 = [item for item in col1] # copia coluna 1
    n = len(col1)
    for j in range(n - 1):
        temp_col = [0] * (n - 1 - j)
        for i in range(n - 1 - j):
            power = j + 1 # é igual o numero da coluna anterior
            temp_col[i] = (2 ** power * col1[i + 1] - col1[i]) / (2 ** power - 1)
        col1[:n - 1 - j] = temp_col
        print(temp_col)
    return col1[0] # a aproximacao procurada

def f(x):
    return x ** x

def F1(f, x0, h):
    return (f(x0 + h) - f(x0)) / h

def F2(f, x0, h):
    return (f(x0) - f(x0 - h)) / h

def g(x):
    return math.cos(x ** x)


if __name__ == '__main__':
    x0 = 1.83958
    h = 0.4483
    col1 = [F1(f, x0, h / 2 ** i) for i in range(5)]
    print(col1)
    r = richardson(col1)
