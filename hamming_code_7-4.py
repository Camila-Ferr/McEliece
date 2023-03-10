import random
import numpy as np
class Hamming_code():
    def __init__(self, p):
        self.gt_7x4 = np.matrix([[1, 1, 0, 1], [1, 0, 1, 1], [1, 0, 0, 0], [0, 1, 1, 1], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
        self.h_7x4 = np.matrix([[1, 0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 0, 1, 1], [0, 0, 0, 1, 1, 1, 1]])

        self.gt_15x14 = np.matrix([1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0],[0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0], [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], [0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1])
        self.h_15x14 = np.matrix([[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]])

        self.p = p

    def hamming_7x4(self):
        print("Entrada:")
        print(self.p)
        x = np.dot(self.gt_7x4, self.p)
        print("multiplicação: gt por p")
        print(x)
        print("Acrescentando erro")
        x = self.limpa_hamming(x)
        x = self.acrescenta_erro(x[0])
        print(x)
        print("Resultado final")
        self.test(x)

    def hamming_15x14(self):
        print("Entrada:")
        print(self.p)
        print("multiplicação: gt por p")
        x = np.dot(self.gt_15x14, self.p)
        print(x)
        x = self.limpa_hamming(x)
        print("Acrescentando erro")
        x = self.acrescenta_erro(x[0])
        print(x)
        print("Resultado final")
        self.test(x)

    def limpa_hamming(self, x):
        for i in range (0,len(x)):
            x[i] = x[i] %2
        return x

    def acrescenta_erro(self,x):
        indice = random.randint(0,x.size -1)
        print(indice+1)
        x[0,indice] = (x[0,indice] + 1)%2
        return x

    def test (self,x):
        x = np.array(x)
        print(self.limpa_hamming((np.dot(self.h_7x4, x[0]))))


test = Hamming_code([1,0,1,1])
test.hamming_7x4()