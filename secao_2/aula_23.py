import numpy as np

#Definindo uma matriz de 2 linhas, 3 colunas
matriz = np.array([[2, 3, 1],
                   [4, 5, 7]])

#Imprimindo a matriz
print(matriz)

#Verificando o quantide de linhas e colunas
print(matriz.shape)

#Acessando a linha da matriz
print(matriz[0])
print(matriz[1])

#Acessando linhas e colunas
print(matriz[0][1])
print(matriz[1][2])

#Acessando todos os itens de uma matriz
foi i in range(matriz.shape[0]):
    print(matriz[i])
    for j in range(matriz.shape[1]):
        print(matriz[j])
