import numpy as np
import math
class Haddamard_g_h():
    def __init__(self, k,tituloLogger):
        self.k = k
        self.tituloLogger = tituloLogger
        self.dimensions_h = [2**k, 2**k - k]
        self.dimensions_g = [k, 2**k]
        self.n = 2**k
        self.createG()
        self.createH()

    "Cria a matriz G e define a identidade da matriz"

    def createG(self):
        g = np.zeros((self.dimensions_g[0], self.dimensions_g[1]))
        gLinha = np.zeros((self.dimensions_g[0],2**(self.k-1)))
        colunaGLinha = -1


        for coluna in range(0,self.dimensions_g[1]):
            continua = False
            atual = self.intBin(coluna)
            if (atual[0] == "1"):
                continua = True
                colunaGLinha +=1

            for linha in range (0, self.dimensions_g[0]):
                g[linha][coluna] = atual[linha]
                if (continua):
                    gLinha[linha][colunaGLinha] = atual[linha]

        self.g = g
        self.gLinha = gLinha

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
        h =  np.zeros((self.n-self.k,self.n))
        h = self.createIdentidade(h)
        gtransposta = self.g.transpose()

        for linha in range (0,len(gtransposta)-self.k): #linha
            for coluna in range (0, self.n -(self.n-self.k)):
                h[linha][coluna] = gtransposta[self.k+linha][coluna]

        self.h = h

    def createIdentidade(self,h):
        identidade = np.zeros((self.n-self.k,self.n-self.k))
        for i in range (0,len(identidade)):
            h[i][self.k+i] = 1
        return h


    def getG(self):
        return self.g

    def getGLinha(self):
        return self.gLinha

    def getH(self):
        return self.h


parameters = Haddamard_g_h(3,"Hadamard")
