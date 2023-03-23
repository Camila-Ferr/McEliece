import numpy as np
import math
class Paramters():
    def __init__(self, paridade, dados,tituloLogger):
        self.tituloLogger = tituloLogger
        self.paridade = paridade
        self.dados = dados
        self.dimensions_h = [paridade, paridade+dados]
        self.dimensions_g = [dados, dados+paridade]
        self.createH()
        self.createG()

    "Marca onde a linha começa no h"

    def createH(self):
        h = np.zeros((self.dimensions_h[0], self.dimensions_h[1]))

        for linha in range (0, self.dimensions_h[0]):
            for coluna in range (linha, self.dimensions_h[1]):

                if (coluna + 1 == 2**linha):
                    h = self.determinateMatrixH(linha,coluna,h)

        self.h= h
        print("Matriz H " +self.tituloLogger + " :")
        print(self.h)

    " Responsável por intercalar linha a linha"
    def determinateMatrixH(self, linha, coluna,h):
        passe = 2**linha
        contador = 0
        vez = 1

        for i in range(coluna, self.dimensions_h[1]):
            if contador == passe:
                contador = 0
                if (vez == 0):
                    vez = 1
                else:
                    vez = 0
            h[linha][i] = vez
            contador +=1
        return h

    "Função de apoio para criação da matriz g"
    def exponencia(self,x):
        return math.log10(x + 1) / math.log10(2)


    "Cria a matriz G e define a identidade da matriz"

    def createG(self):
        g = np.zeros((self.dimensions_g[0], self.dimensions_g[1]))
        print(g)
        ultimoIdentidade = 0
        posicoesIdentidade = []
        for coluna in range (0,self.dimensions_g[1]):
            if ((self.exponencia(coluna))%1 == 0):
               pass
            else:
                g[ultimoIdentidade][coluna] = 1
                posicoesIdentidade.append(coluna + 1)
                ultimoIdentidade +=1
        self.preencheTodaMatriz (g,posicoesIdentidade)
        print("Matriz G " + self.tituloLogger + " :")
        self.g = g
        print(self.g)


    "Função que preenche todas as posições da matriz"
    def preencheTodaMatriz(self,g,posicoesIdentidade):
        contagem = 0
        for coluna in range (0,self.dimensions_g[1]):
            if ((self.exponencia(coluna))%1 == 0):
                g = self.preencheLinha(g, coluna, posicoesIdentidade, contagem)
                contagem +=1

    "Função que consulta o h e preenche as colunas de paridade"
    def preencheLinha(self,g, coluna, posicoesIdentidade,contagem):
        for i in range (0, self.dimensions_g[0]):
            linha_h = contagem
            coluna_h = posicoesIdentidade[i] -1

            if (self.h[linha_h][coluna_h] ==1):
                g[i][coluna] = 1

        return g

    def getG(self):
        return self.g

    def getH(self):
        return self.h





