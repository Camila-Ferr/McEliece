import numpy as np

class ChavesMcELiece():
    def __init__(self,n,k):
        self.n = n
        self.k = k
        self.privateKey()
        self.publicKey()

    def privateKey(self):

        self.g = np.random.randint(2, size=(self.k,self.n))
        self.s = self.s()
        self.p = self.permutacao(np.random.permutation(self.n),self.n)

    def publicKey(self):
        resultado =np.dot(self.s,self.g)
        resultado = np.dot(resultado,self.p)
        self.gLinha = self.limpa_public_key(resultado)

    #Transforma para matriz de 1 e 0
    def limpa_public_key(self, public_key):
        for i in range (0,len(public_key)):
            for j in range (0,len(public_key[i])):
                public_key[i][j] = public_key[i][j] %2
        return public_key

    #Cria uma matriz permutação
    def permutacao(self, permutacao,n):
        linha = np.array(np.zeros((n, n)))
        matriz = np.asmatrix(linha)
        for i in range (0,n):
            for j in range(0,n):
                if (j == permutacao[i]):
                    linha[i][j] = 1
                else:
                    linha[i][j] = 0
        return matriz

    #Matriz aleatória inversível
    def s(self):
        continua = True
        while(continua):
            s = np.random.randint(2, size=(self.k,self.k))
            #Se determinante = 0, matriz não é inversível
            if (np.linalg.det (s) != 0):
                return s

