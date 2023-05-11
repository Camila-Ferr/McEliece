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



## Código de Hadamard:


