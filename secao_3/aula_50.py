'''
Notação Big-O

    Como comparar dois algoritmos?
    Comparação objetiva entre algoritmos
    Considera diferenças entre poder de processamento, sistema operacional, linguagem de programação.
    O quanto a "complexidade" do algoritmo aumenta de acordo com as entradas.

'''

# Função 1 - O(n)

def soma(n):
    soma = 0
    for i in range(n + 1)
        soma += i
    
    return soma

# Função que retorna o tempo de execução da função
%timeit soma(10)

# Função 2

def soma_2(n):
    return (n * (n * 1)) / 2

%timeit soma_2(10)

'''
Tempo de execução das funções

Função soma = 663 ns
Função soma_2 = 116 ns

'''

# Função 3
def lista_1():
    lista = []
    for i in range(1000):
        lista += [i]
    
    return lista

print(lista_1())
%timeit lista_1

# Função 4
def lista_2():
    return range(1000)

print(lista_2())
%timeit lista_2()

from math import log
import numpy as np 
import matplotlib.pyplot as plt

n = np.linspace(1, 10, 100)

print(len(n))
np.ones(n.shape)


labels = ['Constant', 'Logaritmhmic', 'Linear', 
          'Log Linear', 'Quadratic', 'Cubic', 'Exponential']

big_o = [np.ones(n.shape), np.log(n), n, n * np.log(n), n**2, n**3, 2**n]

plt.figure(figsize=(10,8))
plt.ylim(0,100)
for i in range(len(big_o))
    plt.plot(n, big_o[i], label = labels[i])
plt.legend()
plt.ylabel('Runtime')
plt.xlabel('n')