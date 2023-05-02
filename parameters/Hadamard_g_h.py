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
        gLinha = np.zeros((self.dimensions_g[0],2**(self.k-1)))
        colunaGLinha = -1

        for coluna in range(0,self.dimensions_g[1]):
            continua = False
            atual = self.intBin(coluna + 1)
            if (atual[0] == "1"):
                continua = True
                colunaGLinha +=1

            for linha in range (0, self.dimensions_g[0]):
                g[linha][coluna] = atual[linha]
                if (continua):
                    gLinha[linha][colunaGLinha] = atual[linha]

        self.g = g
        print("Create G:")
        print(g)
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
        h =  np.zeros((self.n-self.k - 1,self.n - 1))
        h = self.createIdentidade(h)
        gtransposta = self.g.transpose()
        print("G transposta")
        print(gtransposta)
        for linha in range (0,len(gtransposta)-self.k): #linha
            for coluna in range (0, self.n -(self.n-self.k)):
                h[linha][coluna] = gtransposta[self.k + linha][coluna]
        # h = self.arruma(h)
        self.h = h
        print("Create H:")
        print(h)

# Identidade está correta
    def createIdentidade(self,h):
        identidade = np.zeros((self.n-self.k - 1,self.n-self.k - 1))
        print(identidade)
        for i in range (0,len(identidade)):
            h[i][i + self.k] = 1
        return h

    def arruma(self,h):
        for coluna in range (0,self.dimensions_h[0]-1):
            print(coluna)
            if (coluna-1)>1 and (self.exponencia(coluna)%1 == 0) and (self.exponencia(coluna+1)%1 != 0):
                h[:, [coluna-1, coluna]] = h[:, [coluna, coluna-1]]
                print(h)
        return h

    def exponencia(self,x):
        return math.log10(x + 1) / math.log10(2)


    def getG(self):
        return self.g

    def getGLinha(self):
        return self.gLinha

    def getH(self):
        return self.h


parameters = Haddamard_g_h(3,"Hadamard")
