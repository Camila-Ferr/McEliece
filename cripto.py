import random
import numpy as np
import generateKeys
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
        self.erro = [1,1,0,0,0,0,0,0,0,0,0,0]
        return self.limpa_mensagem((np.dot(self.mensagem,self.publicKey)) + self.erro)

    def limpa_mensagem(self,mensagem):
        for i in range (0,len(mensagem)):
            mensagem[i] = mensagem[i] %2
        return mensagem

    def gera_vetor_erro(self):
        verifica = True
        vetor = []

        while(verifica):
            vetor = np.zeros(self.n)

            for i in range(int((self.n - self.k)/2)):
                numero = random.randint(0,1)
                vetor[random.randint(0, self.n - 1)] = numero
                if (numero == 1):
                    verifica = False
        print("Vetor de erro: "+ str(vetor))
        return vetor



