import random
import numpy as np
class Execute():
    def __init__(self, h, g, p):
        self.h = h
        self.g = g
        self.p = p
        self.gt = np.transpose(self.g)
        self.algoritmo()


    def algoritmo (self):
        print("Entrada:")
        print(self.p)
        x = np.dot(self.gt, self.p)
        print("multiplicação: gt por p")
        print(x)
        # print("Acrescentando erro")
        x = self.limpa_matrix(x)
        x = self.acrescenta_erro(x)
        # print(x)
        print("Resultado final")
        print(self.verifica_erro(x, self.h))



    def limpa_matrix(self, x):
        for i in range (0,len(x)):
            x[i] = x[i] %2
        return x

    def acrescenta_erro(self,x):
        indice = random.randint(0,x.size -1)
        print(indice+1)
        x[indice] = (x[indice] + 1)%2
        return x

    def verifica_erro (self,x,matrix):

        return (self.limpa_matrix((np.dot(matrix, x))))