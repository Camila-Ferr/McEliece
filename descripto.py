#Agora a Alice irá descriptografar a mensagem
import numpy as np

import generateKeys
from codigoErro.hamming_code import Hamming_code
from cripto import CriptoMcELiece


class DescriptoMcELiece():
    def __init__(self, n,k):
        self.keys = generateKeys.ChavesMcELiece(n,k)

    def descripto(self,mensagem,erro):
        self.c = mensagem
        self.t = erro
        self.cLinha = np.dot(self.c, np.linalg.inv(self.keys.p))

        #cLinha = msg +eP-1
        eInvP = np.dot(erro,np.linalg.inv(self.keys.p))


        #tirar os erros da mensagem
        self.mensagem = self.corrigir_erros()
        # return (np.dot(ms,np.linalg.inv(self.keys.s)))

    def corrigir_erros(self):
        hamming = Hamming_code([self.mensagem])
        vetor_erro = hamming.verifica_erro(self.mensagem, hamming.h_7x4)
        print(vetor_erro)


    def decode(self, msg):
        #transformar msg para ms
        return [1,1,0,1]


descriptografia = DescriptoMcELiece(12,4)
mensagem_cripto= CriptoMcELiece(np.array([1,0,1,0]),descriptografia.keys.gLinha)
print("Mensagem criptografada:")
print(mensagem_cripto.mensagemCriptografada)

mensagem_descripto = descriptografia.descripto(mensagem_cripto.mensagemCriptografada,mensagem_cripto.erro)
print("Mensagem descriptografada :")
print(mensagem_descripto)