'''
1 - Inserção de um novo jogador no vetor
2 - Pesquisa Linear do vetor não ordenado
3 - Exclusão de um valor dentro do vetor não ordenado
'''
import numpy as np

class vetor_nao_ordenado():
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    # O(n)
    def imprime():
        if self.ultima_posicao == -1:
            print('O vetor está vazio.')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, '-', self.valores(i)

    # O(1) - O(2)
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor

    # O(n)
    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i
        return -1

vetor = vetor_nao_ordenado(5)
vetor.imprime()

# Insere dados
vetor.insere(2)
vetor.imprime()

vetor.insere(3)
vetor.insere(5)
vetor.insere(8)
vetor.insere(1)

# Pesquisar dados
vetor.pesquisar(8)
vetor.pesquisar(9)

