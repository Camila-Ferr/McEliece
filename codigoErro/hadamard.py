import numpy as np
from parameters.Hadamard_g_h import Haddamard_g_h
from Execute import *
class Hadamard():
    def __init__(self, mensagem):
        self.parametros5x3 = Haddamard_g_h(3, "Hadammard 8x5x3")
        self.g = self.parametros5x3.getG()
        self.h = self.parametros5x3.getH()
        self.execute = Execute(self.h,self.g,mensagem)
        self.mensagem = mensagem

test = Hadamard([1,0,0])
# test.hadamard()