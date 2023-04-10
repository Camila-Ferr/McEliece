import numpy as np
import math
class Haddamard_g_h():
    def __init__(self, k,tituloLogger):
        self.tituloLogger = tituloLogger
        self.dimensions_h = [2**k, 2**k - k]
        self.dimensions_g = [k, 2**k]
        self.createG()

    "Cria a matriz G e define a identidade da matriz"

    def createG(self):
        g = np.zeros((self.dimensions_g[0], self.dimensions_g[1]))

        for coluna in range(0,self.dimensions_g[1]):
            atual = self.intBin(coluna)
            for linha in range (0, self.dimensions_g[0]):
                g[linha][coluna] = atual[linha]
        self.g = g
        print(g)

    def intBin(self,x):
        retorno = []
        bin = format(x, "b")
        contador = len(bin)
        if (contador < self.dimensions_g[0]) :
            for i in range (contador, self.dimensions_g[0]):
                retorno.append("0")
        for i in bin:
            retorno.append(i)
        return retorno


    def getG(self):
        return self.g

    def getH(self):
        return self.h


parameters = Haddamard_g_h(3,"Hadamard")
