import random
import numpy as np

from codigoErro.Execute import Execute
from parameters.hamming_h_g import Hamming_h_g as Paramters
class Hamming_code():
    def __init__(self, p):
        self.mensagem = p
        self.h = []
        self.g = []

        if (len(p)) == 4:
            self.parametros7x4 = Paramters(3,4,"Hamming 7x4")
            self.h = self.parametros7x4.getH()
            self.g = self.parametros7x4.getG()

            print(np.dot(self.parametros7x4.getG(), np.transpose(self.h)))

        elif (len(p) == 11):
            self.parametros15x11 = Paramters(4,11,"Hamming 15x11")
            self.h = self.parametros15x11.getH()
            self.g = self.parametros15x11.getG()

        elif (len(p) == 26):
            self.parametros31x26 = Paramters(5,26,"Hamming 31x26")
            self.h = self.parametros31x26.getH()
            self.g = self.parametros31x26.getG()

        self.execute = Execute(self.h, self.g, self.mensagem)



test = Hamming_code([1,0,1,1,0,1,1,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0])

# test = Hamming_code([1,0,1,0])