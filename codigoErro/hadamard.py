import numpy as np
from parameters.Hadamard_g_h import Haddamard_g_h
class Hadamard():
    def __init__(self, mensagem):
        self.parametros5x3 = Haddamard_g_h(3, "Hadammard 8x5x3")
        self.gt = np.transpose(self.parametros5x3.getG())
        self.h = self.parametros5x3.getH()
        print(self.parametros5x3.getG())
        print(self.h)
        print("aq")
        print(np.dot(self.parametros5x3.getH(), np.transpose(self.parametros5x3.getG())))

        self.mensagem = mensagem

        # self.gt = np.transpose(self.g)

    def hadamard(self):
        print("Entrada:")
        print(self.mensagem)
        x = np.dot(self.gt, self.mensagem)
        print("multiplicação: gt por mensagem")
        x = self.limpa_haddamard(x)
        print(x)

        # print("Acrescentando erro")
        # x = self.acrescenta_erro(x[0])
        # print(x)
        print("Resultado final")
        x = self.test(x,self.h)
        print(x)

    def test (self,x,matrix):
        # x = np.array(x)
        return (self.limpa_haddamard((np.dot(matrix, x))))

    def limpa_haddamard(self, x):
        for i in range (0,len(x)):
            x[i] = x[i] %2
        return x

test = Hadamard([1,0,1])
test.hadamard()