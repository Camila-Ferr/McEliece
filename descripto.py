#Agora a Alice irá descriptografar a mensagem
import numpy as np

import generateKeys
from cripto import CriptoMcELiece


class DescriptoMcELiece():
    def __init__(self, n,k):
        self.keys = generateKeys.ChavesMcELiece(n,k)

    def descripto(self,mensagem,erro):
        self.mensagem = mensagem
        first_multiplo= np.dot(mensagem,self.keys.s)
        first_multiplo = np.dot(first_multiplo,self.keys.g)
        print(np.linalg.inv(self.keys.p))
        second_multiplo = np.dot(erro,np.linalg.inv (self.keys.p))
        print(first_multiplo)
        print(second_multiplo)

descriptografia = DescriptoMcELiece(10,20)
mensagem_cripto= CriptoMcELiece(np.array([1,0,0,0,0,0,0,0,1,0]),descriptografia.keys.gLinha)
print("Mensagem criptografada:")
print(mensagem_cripto.mensagemCriptografada)

mensagem_descripto = descriptografia.descripto(mensagem_cripto.mensagemCriptografada,mensagem_cripto.erro)
print("Mensagem descriptografada :")
print(mensagem_descripto)