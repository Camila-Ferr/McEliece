import random
import numpy as np
class Hadamart():
    def __init__(self, mensagem):
        self.g = np.matrix([[0, 0, 0, 0, 1, 1, 1, 1],
                            [0, 0, 1, 1, 0, 0, 1, 1],
                            [0, 1, 0, 1, 0, 1, 0, 1]])

        self.h = np.matrix([[0, 0, 0, 1, 0, 0, 0, 0],
                           [0, 1, 1, 0, 1, 0, 0, 0],
                           [1, 0, 1, 0, 0, 1, 0, 0],
                           [1, 1, 0, 0, 0, 0, 1, 0],
                           [1, 1, 1, 0, 0, 0, 0, 1]])
        self.mensagem = mensagem

        self.gt = np.transpose(self.g)

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

test = Hadamart([1,0,1,1,0,1,1,1])
test.hadamard()