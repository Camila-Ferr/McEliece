import random
import numpy as np
import generateKeys
from codigoErro.hamming_code import Hamming_code


#Imagine que Bob queira enviar uma mensagem para Alice,
# ele vai gerar as chaves privadas dele e vai recuperar a pública da Alice
#A partir da chave pública dela, ele envia a mensagem
class CriptoMcELiece():
    def __init__(self, mensagem, publicKey):
        self.mensagem = mensagem
        self.publicKey = publicKey
        self.n = publicKey.shape[1]
        self.k = publicKey.shape[0]
        self.mensagemCriptografada = self.encriptografa()

    def encriptografa(self):
        # self.erro= self.gera_vetor_erro()
        print(self.limpa_mensagem((np.dot(self.mensagem,self.publicKey))))
        return self.limpa_mensagem((np.dot(self.mensagem,self.publicKey)) )

    def limpa_mensagem(self,mensagem):
        for i in range (0,len(mensagem)):
            mensagem[i] = mensagem[i] %2
        return mensagem

    def gera_vetor_erro(self):
        vetor_erro = Hamming_code([self.mensagem]).hamming_15x11()
        print("Vetor de erro: "+ str(vetor_erro))
        return vetor_erro



