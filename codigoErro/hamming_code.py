import random
import numpy as np
from parameters.hamming_h_g import Hamming_h_g as Paramters
class Hamming_code():
    def __init__(self, p):
        self.p = p
        if (len(p)) == 4:
            self.parametros7x4 = Paramters(3,4,"Hamming 7x4")
            self.h_7x4 = self.parametros7x4.getH()
            self.gt_7x4 = np.transpose(self.parametros7x4.getG())
            self.hamming(self.gt_7x4, self.h_7x4)
            print(np.dot(self.parametros7x4.getG(), np.transpose(self.h_7x4)))

        elif (len(p) == 11):
            self.parametros15x11 = Paramters(4,11,"Hamming 15x11")
            self.h_15x11 = self.parametros15x11.getH()
            self.gt_15x11 = np.transpose(self.parametros15x11.getG())

        elif (len(p) == 26):
            self.parametros31x26 = Paramters(5,26,"Hamming 31x26")
            self.h_31x26 = self.parametros31x26.getH()
            self.gt_31x26 = np.transpose(self.parametros31x26.getG())

        self.p = p

    def hamming(self, gt, h):
        print("Entrada:")
        print(self.p)
        x = np.dot(gt, self.p)
        print("multiplicação: gt por p")
        print(x)
        print("Acrescentando erro")
        x = self.limpa_hamming(x)
        x = self.acrescenta_erro(x)
        print(x)
        print("Resultado final")
        print(self.verifica_erro(x, h))



    def limpa_hamming(self, x):
        for i in range (0,len(x)):
            x[i] = x[i] %2
        return x

    def acrescenta_erro(self,x):
        indice = random.randint(0,x.size -1)
        print(indice+1)
        x[indice] = (x[indice] + 1)%2
        return x

    def verifica_erro (self,x,matrix):

        return (self.limpa_hamming((np.dot(matrix, x))))


# test = Hamming_code([1,0,1,1,0,1,1,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0])

test = Hamming_code([1,0,1,0])