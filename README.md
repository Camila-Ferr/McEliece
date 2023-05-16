# Código Linear

#### Um código linear é um tipo de código de correção de erro utilizado para proteger a transmissão de informações digitais em canais de comunicação propensos a erros, como em redes de computadores ou em sistemas de armazenamento de dados.

#### A ideia básica de um código linear é que cada mensagem que precisa ser transmitida é vista como um vetor de bits, que é então transformado em outro vetor de bits (chamado de código) usando uma matriz chamada de matriz geradora. Essa matriz é projetada de forma a garantir que todos os possíveis códigos tenham algumas propriedades úteis, como distâncias mínimas bem definidas entre eles.

#### Uma vez que um código linear é gerado, ele pode ser transmitido através de um canal sujeito a erros, como um canal de rádio ou uma rede de computadores. Quando o receptor recebe o código, ele usa outra matriz chamada de matriz de verificação de paridade (ou matriz de verificação de erro) para detectar e corrigir erros que possam ter ocorrido durante a transmissão.

#### A principal vantagem dos códigos lineares é que eles são fáceis de implementar e possuem um alto grau de eficiência na correção de erros. Além disso, existem muitos algoritmos eficientes disponíveis para a decodificação de códigos lineares, o que torna sua utilização muito conveniente em muitas aplicações práticas.


## Informações:

* Tamanho do Bloco é dado por **n = 2^r -1**
* Tamanho da Mensagem é dada por **k = 2^r - r -1**
* onde r é um inteiro >= 2


## Matriz Geradora (G):

* A Matriz **G = (I | P)**
*  Dimensão (k x n)
> - onde I é a matriz identidade **k x k**
> - onde P é a matriz **k x (n - k)**


## Matriz de Paridade (H):

* A Matriz **H = (-Pt | I')**
* Dimensão ((n - k) x n)
> - onde I' é a matriz identidade **k x k**
> - onde Pt é a matriz transposta de **P**


## Código de Hamming:
#### O Código de Hamming é um código linear que usa paridade para detectar e corrigir erros em uma mensagem transmitida. Para explicar a construção matemática deste código, podemos usar a seguinte notação:

* n é o comprimento da palavra-código;
* k é o número de bits de informação na palavra-código;
* d é a distância mínima entre as palavras-código, ou seja, a menor quantidade de bits que precisam ser modificados para transformar uma palavra-código em outra.
* A construção do Código de Hamming é baseada em uma matriz de verificação de paridade H, que é uma matriz (n-k) por n cujas linhas são ortogonais a todas as palavras-código. A matriz H pode ser construída da seguinte forma:

#### Escolha um número m tal que 2^m >= n + m + 1.
##### Isso garante que é possível construir uma matriz H com a distância mínima d = 3.
##### Enumere as colunas de H de 1 a n, e para cada coluna i, escreva o número i em binário de m bits. Por exemplo, se n = 7, então m = 3, e as colunas de H são numeradas como 001, 010, 011, 100, 101, 110 e 111.
##### Escreva cada coluna de H como uma combinação linear dos vetores canônicos de R^(n-k), ou seja, os vetores que têm um único elemento 1 e os demais elementos iguais a zero. Para a coluna i, o coeficiente da linha j é 1 se o j-ésimo bit de i em binário é 1, e 0 caso contrário. Por exemplo, a coluna 010 é escrita como (0, 1, 0, 0, 0, 0, 0) = 0e_1 + 1e_2 + 0e_3 + 0e_4 + 0e_5 + 0e_6 + 0*e_7.
##### Verifique que a matriz H assim construída tem distância mínima d = 3, ou seja, nenhuma duas colunas são iguais, nenhuma coluna é o complemento de outra coluna, e nenhuma três colunas formam uma combinação linear de duas outras colunas.
##### Com a matriz H em mãos, a matriz geradora G do Código de Hamming pode ser construída da seguinte forma:

#### - Escolha um vetor v de R^k com os k bits de informação que se deseja transmitir.
##### - Adicione (n-k) zeros a v para obter um vetor u de R^n.
##### - Calcule o vetor de verificação de paridade c = uH^T, onde H^T é a transposta de H.
##### - Adicione c a u para obter a palavra-código x = u + c.
##### - Para decodificar uma palavra-código recebida y de R^n, é possível usar a seguinte técnica:

#### Calcule o vetor de síndrome s = yH^T, onde H^T é a transposta de H.
##### - Se s = 0, então y é uma palavra-código válida.
##### - Se s não é zero, então localize a coluna de H cuja combinação linear com s tem a menor norma. O índice dessa coluna indica a posição do erro, e


#### A partir da matriz geradora G, podemos gerar todos os códigos válidos de Hamming. Suponha que queremos transmitir a mensagem original (1011). Para codificá-la usando o código de Hamming (7, 4), devemos multiplicar a mensagem original pela matriz geradora G: 

```
1 0 1 1     1 0 0 0 1 1 0
-------  x  -------------
            0 1 0 0 1 1 1
            0 0 1 0 1 0 1
            0 0 0 1 0 1 1
                      
= 1 0 1 1 0 1 0

```

#### O resultado é o código Hamming (7, 4) correspondente à mensagem original (1011).

##### Para decodificar um código recebido, usamos a matriz de verificação de paridade H. Suponha que o receptor recebe o código Hamming (7, 4) 1011010. Para verificar se o código recebido contém algum erro, devemos multiplicá-lo pela matriz H:

```
 1 0 1 1 0 1 0     1 0 1 1 0 1 0
 -------------  x  -------------
 1 1 0 1 0 0 0     1 1 0 1 0 0 0
 0 1 1 1 0 0 0     0 1 1 1 0 0 0
 1 1 1 0 0 0 0     1 1 1 0 0 0 0
                      
 = 0 0 1 0 0 0 0

```

#### O resultado é um vetor de verificação de paridade (0 0 1 0 0 0 0). Se o vetor de verificação de paridade não for o vetor nulo (todos os elementos iguais a zero), então o código recebido contém um erro e podemos corrigi-lo. Para corrigir o erro, devemos encontrar a posição do bit errado no vetor recebido e inverter seu valor (trocar 0 por 1 ou 1 por 0). A posição do bit errado é igual à posição do bit correspondente no vetor de verificação de paridade.

##### Por exemplo, o vetor de verificação de paridade (0 0 1 0 0 0 0) indica que o terceiro bit do código recebido (1011010) contém um erro. Portanto, devemos inverter o valor do terceiro bit para corrigir o erro. O código correto é (1010010).


## Álgebra Linear:

###### Pares: 0
###### Ímpares: 1
###### Sempre que falar de Z é (Z mod 2)

Com Z mod 2 = {0,1} -> 2 elementos
```
V1 = {[x1]}
     {[...]} : x1,x2,..,xn pertence Z}
     {[xn]}
```
-> Quantidade de vetores em V1 é 2^n 
-> os vetores diferentes de 0 são 2^n -1
-> Z^3 tem 7 vetores diferentes de 0

#### Definição: Uma matriz de Hamming é uma matriz H com K linhas e colunas de H são todos os vetores diferentes de 0 em Z^k (sendo K um inteiro positivo)
```
Quando K = 3

    [1 0 0 | 1 0 1 1]
H = [0 1 0 | 1 1 0 1] = [I | Q]
    [0 0 1 | 1 1 1 0]
```
Em geral podemos ter um vetor H = [I(k) Q]

Então Q é um k x (2^k -1 -k) Matriz

(L = 2^k -1 -k)
```                        
E com outra Matriz M := [Q]  -> Dimensão (2^k -1 linhas
                        [I(L)]   e 2^k -1 -k colunas)
```

Ex:
```
M = [Q]
    [I(4)]
```
Ker(H) = Núcleo (H)
### Fatos:

#### i) H é sobrejetivo
#### ii) M é injetiva
#### iii) Ker(H) = Imagem(M) (espaço nulo de H é o espaço da coluna de M)


### Provas:

#### i) H está na Forma Escalonada Reduzida e tem 3 pivos
#### ii) As colunas da Matriz identidade são linearmente independentes, então o mesmo é verdade para M
#### iii) Ker(H) contém a Imagem(M)
```
H * M = [I(3) Q] * [Q]   = [I(3)*Q + Q*I(4)]
                   [I(4)]

H * M = 2[Q] = 0  -> Uma Matriz 3x4
```
E agora Ker(H) está na Imagem(M)

> Como M é injetiva, dimensão(Imagem(M)) = 4 e como H é sobrejetiva, dimensão(Imagem(H)) = 3 portanto, a dimensão(ker(H)) = 4, e como eles tem a mesma dimensão, eles tem o mesmo subespaço.

###### Ker(H) = Imagem(M)
                       
> Com um vetor vazio, temos uma sequência de transformações lineares, que é uma sequência exata

###### {0} -> Z^4 --M--> Z^7 --H-->Z^3 --> {0}


### Propriedades:

```
H = [I(3) Q]   M = [Q]
                   [I(4)]
```
#### Notação: 
###### Imagem(M) = Ker(H) =: C (esse subespaço)

###### O subespaço sendo deslocado por algum vetor:

> Com Ci = C + ei = {V + ei: onde V está em C} ,para todo i pertence {1,..., 7} 

### Fatos:

#### i) Ci é o conjunto de solução de Hx = Hei, onde Hei é a coluna i de H

#### ii) Ci interseção Cj = conjunto vazio, para todo i =/ j

#### iii) C interseção Ci = conjunto vazio, para todo i

#### iV) Z^7 = C união todos os outros conjuntos de soluções homogêneas (Ci, i = 1 até 7)
 
 ###### é também uma união disjunta, então cada vetor de Z está exatamente em um desses subconjuntos. (é um conjunto de soluções do Sistema homogêneo ou está em um desses conjuntos de soluções dos diferentes sistemas não homogêneos)


### Prova:

#### i) ei é uma solução particular, e o conjunto de soluções de todo o sistema é:
 
> Hx = Hei é ei + C

#### ii) Suponha Mu1 + ei = Mu2 + ej
> Se aplicarmos H para essa igualdade

###### -> HMu1 + Hei = HMu2 + Hej, onde Hmu1 e Hmu2 é {0} 
> => Hei = Hej (eles são iguais), então i = j

#### iii) mesma prova de ii)

#### iV) número de Vetores em C é 2^4

> E o número de vetores em Ci é 2^4 e por ter 7 ci's, a união de todos os C é = 2^4 + 7 * 2^4

###### União tem 2^4(2^3) = 2^7 e Z tem 2^7 vetores

###### Então a união C união com Ci(i = 1 até 7) = Z^7

###### Qual a significância:

> H pode distinguir vetores C vs Ci por que
> HC = {0} e HCi = {Hei} e portanto, se voce aplicar H para algum vetor arbitrário

Vetor V em Z mod 2:

###### Se      Hv = 0 =>    v está em C
###### mas se  Hv = Hei =>  v está em Ci


### Aplicações:

> Se aplicarmos M em qualquer vetor u
```
Mu = [Qu] para todo u pertencente a Z^4
      [u]
```

> Tenta mandar uma mensagem u:
```
u = [0] -> o erro pode ocorrer em qualquer bit
    [1] 
    [1]
    [0]
```

Mas se mandar Mu pertence C (onde a mensagem está contida em C) e se tiver um erro qualquer:

###### (Mensagem) V = Mu + ei

##### Se 
   > Hv = 0 => v pertence C = Imagem(M) -> Sem erro
   > Hv = Hei => v pertence Ci = C + ei -> Com 1 erro no máximo

##### No primeiro caso:

> -> Mensagem Original: é o vetor correspondente às últimas quatro entradas de V

##### No Segundo caso:

> -> Um erro ocorreu na oitava entrada de V
> Para consertar:
> V + ei, as quatro últimas entradas desse vetor vai ser a mensagem original

Ex:
```
    [0]
v = [0]    
    [1]   -> Se aplicarmos Hv = [1 0 0 | 1 0 1 1]
    [1]                         [0 1 0 | 1 1 0 1] * V
    [0]                         [0 0 1 | 1 1 1 0]
    [1]                                      
    [1]                                      
   
```
```
                  [3]           [1]
teremos o vetor = [2] = mod 2 = [0]  -> e o erro está na sexta entrada
                  [3]           [1]
```

##### Isso quer dizer que a mensagem v teve um erro na sexta linha


