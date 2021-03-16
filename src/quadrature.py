import math

def f(x):
    return math.exp(-x ** 2)

def quadrature (f, lista_de_pontos_e_pesos):
    soma = 0
    for x_k, c_k in lista_de_pontos_e_pesos:
        soma += c_k * f(x_k)
    return soma

def change(f, a, b, u):
   return f((b + a) / 2 + (b - a) * u / 2) * (b - a) / 2

def g(u):
    return change(f, a, b, u)



if __name__ == '__main__':

    n2 = [(0.5773502692, 1.0000000000), (-0.5773502692, 1.0000000000)]
    n3 = [(0.7745966692, 0.5555555556), (0.0000000000, 0.88888888889), (-0.7745966692, 0.5555555556)]
    n4 = [(0.8611363116, 0.3478548451), (0.3399810436, 0.6521451549), (-0.3399810436, 0.6521451549),
          (-0.8611363116, 0.3478548451)]
    n5 = [(0.9061798459, 0.2369268850), (0.5384693101, 0.4786286705), (0.0000000000, 0.5688888889),
          (-0.5384693101, 0.4786286705), (0.9061798459, 0.2369268850)]

    print('{x:<20}{c:<20}'.format(x='x_k', c='c_k'))
    for x_k, c_k in n3:
        print('{x:<20}{c:<20}'.format(x=x_k, c=c_k))

    a, b = [2, 5]
    r = quadrature(g, n5)
    print(r)