import math
import numpy as np

class Haddamard_g_h():
    def __init__(self, k,tituloLogger):
        self.k = k
        self.tituloLogger = tituloLogger
        self.dimensions_h = [2**k - 1, 2**k - k - 1]
        self.dimensions_g = [k, 2**k - 1]
        self.n = 2**k
        self.createG()
        self.createH()

    "Cria a matriz G e define a identidade da matriz"

    def createG(self):
        g = np.zeros((self.dimensions_g[0], self.dimensions_g[1]))
        g = self.createIdentidade(g, self.k,0)
        prox = self.k

        for contador in range (1, self.dimensions_g[1]):
            if self.exponencia(contador)%1 != 0:
                atual = self.intBin(contador+1)
                for linha in range (0, self.dimensions_g[0]):
                    g[linha][prox] = atual[linha]
                prox += 1
        print("G: ")
        print(g)
        self.g = g

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


    def createH(self):
        h =  np.zeros((self.n-self.k - 1,self.n - 1))
        h = self.createIdentidade(h, (self.n-self.k - 1), self.k)
        gtransposta = self.g.transpose()

        for linha in range (0,len(gtransposta)-self.k): #linha
            for coluna in range (0, self.n -(self.n-self.k)):
                h[linha][coluna] = gtransposta[self.k + linha][coluna]

        self.h = h
        print("Create H:")
        print(h)

# Identidade está correta
    def createIdentidade(self,matrix, dimension, soma):
        identidade = np.zeros((dimension,dimension))
        for i in range (0,len(identidade)):
            matrix[i][i + soma] = 1
        return matrix

    def exponencia(self,x):
        return math.log10(x + 1) / math.log10(2)


    def getG(self):
        return self.g

    def getGLinha(self):
        return self.gLinha

    def getH(self):
        return self.h


# parameters = Haddamard_g_h(3,"Hadamard")
