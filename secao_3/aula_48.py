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
