import numpy as np
from sympy import *
from sympy.abc import x

def GoppaCode():
    def __init__(self, p, n,t):
        self.p = p # primo
        self.n = n # ordem do campo finito
        self.t = t # grau do polinômio de Goppa

    def createFiniteGalois(self):
        GF = np.array([0, 1])

        for i in range(1, self.n):
            GF = np.append(GF, GF[-1] + 1)
            if GF[-1] == self.p-1:
                GF = np.append(GF, 0)
        self.GF = GF.reshape((self.n, -1))

# Criação do polinômio irreversível
    def irreductible_poly(self):
        self.irr_poly = self.GF.irreducible_poly(self.p, self.n)
        print(self.irr_poly)

# Criação do polinômio de Goppa
    def goppa_poly(self):
        g_poly = np.array([1, 1, 0, 0, 1]) # x^4 + x^3 + 1

# Cálculo das raízes do polinômio de Goppa
roots = []
for i in range(2**n):
    if (g_poly*GF[i]).sum() % p == 0:
        roots.append(i)
roots = np.array(roots)

# Criação da matriz de verificação de paridade
H = np.zeros((n-t, n))
for i in range(n-t):
    H[i][roots[i]] = 1
    for j in range(t):
        H[i][(roots[i]**(j+1)) % 2**n] = 1

# Criação da matriz geradora
G = np.zeros((t, n))
for i in range(t):
    G[i][i] = 1
    for j in range(n):
        G[i][j] = (irr_poly[j]*(roots[i]**(j+1))) % p
G = np.linalg.inv(G)

# Impressão das matrizes geradora e de verificação de paridade
print("Matriz geradora G:\n", G)