import numpy as np
from parameters.hamming_h_g import Paramters
class Hadamard():
    def __init__(self, mensagem):
        self.parametros5x3 = Paramters(4, 5, "Hadammard 8x5x3")
        self.gt = np.transpose(self.parametros5x3.getG())
        self.h = self.parametros5x3.getH()

        self.mensagem = mensagem

        # self.gt = np.transpose(self.g)

    def hadamard(self):
        print("Entrada:")
        print(self.mensagem)
        x = np.dot(self.gt, self.mensagem)
        print("multiplicação: gt por mensagem")
        print(x)
        # print("Acrescentando erro")
        # x = self.limpa_hamming(x)
        # x = self.acrescenta_erro(x[0])
        # print(x)
        print("Resultado final")
        self.test(x,self.h)

    def test (self,x,matrix):
        x = np.array(x)
        print(np.dot(matrix, x[0]))

test = Hadamard([1,0,1,0,0])
test.hadamard()