"""
Matrizes para se utilizar como exemplo:
1 2 1 8
2 -1 1 3
3 1 -1 2
espera-se:
det = 15
x = 1
y = 2
z = 3

1 1 1 6
1 2 2 9
2 1 3 11
espera-se:
det = 2
x = 3
y = 2
z = 1
"""

def Determinante(x, y, z):
    det = x[0] * y[1] * z[2] + x[1] * y[2] * z[0] + x[2] * y[0] * z[1] #primeira parte da determinante
    det = det + (x[0] * y[2] * z[1]) * -1 + (x[1] * y[0] * z[2]) * -1 + (x[2] * y[1] * z[0]) * -1 #segunda parte da determinante multiplicando por -1
    return det

def CramerX(x, y, z):
    xmatx = x.copy()
    xmaty = y.copy()
    xmatz = z.copy()
    xmatx[0] = x[3]
    xmaty[0] = y[3]
    xmatz[0] = z[3]
    """print("coluna X")
    print(xmatx)
    print(xmaty)
    print(xmatz)"""

    detx = Determinante(xmatx, xmaty ,xmatz)
    return detx

def CramerY(x, y, z):
    ymatx = x.copy()
    ymaty = y.copy()
    ymatz = z.copy()
    ymatx[1] = x[3]
    ymaty[1] = y[3]
    ymatz[1] = z[3]
    """print("coluna Y")
    print(ymatx)
    print(ymaty)
    print(ymatz)"""

    dety = Determinante(ymatx, ymaty, ymatz)
    return dety

def CramerZ(x, y, z):
    zmatx = x.copy()
    zmaty = y.copy()
    zmatz = z.copy()
    zmatx[2] = x[3]
    zmaty[2] = y[3]
    zmatz[2] = z[3]

    """print("coluna Z")
    print(zmatx)
    print(zmaty)
    print(zmatz)"""

    detz = Determinante(zmatx, zmaty, zmatz)
    return detz

def main():
    x = list(map(int, input("Digite os valores da primeira linha separando por espaço: ").split(" ")))
    y = list(map(int, input("Digite os valores da segunda linha separando por espaço: ").split(" ")))
    z = list(map(int, input("Digite os valores da terceira linha separando por espaço: ").split(" ")))
    # print(x)
    # print(y)
    # print(z)
    print("\nA matriz digitada é: ")
    print(f'|{str(x[0]).center(4)}{str(x[1]).center(4)}{str(x[2]).center(4)}| . | x | = {x[3]}')
    print(f'|{str(y[0]).center(4)}{str(y[1]).center(4)}{str(y[2]).center(4)}| . | y | = {y[3]}')
    print(f'|{str(z[0]).center(4)}{str(z[1]).center(4)}{str(z[2]).center(4)}| . | z | = {z[3]}')
    
    det = Determinante(x,y,z)
    print()
    if det == 0:
        print(f'A determinante é {det}')
        print("O sistema é possível e inderteminado (SPI) ou é impossível (SI)")
    else:
        detx = CramerX(x, y, z)
        dety = CramerY(x, y, z)
        detz = CramerZ(x, y, z)

        print(f'A determinante é {det}')
        print("Pela fórmula de Cramer: ")
        print(f'X = {detx} então, {detx} / {det} = {detx / det}')
        print(f'Y = {dety} então, {dety} / {det} = {dety / det}')
        print(f'Z = {detz} então, {detz} / {det} = {detz / det}')

if __name__ == "__main__":
    main()