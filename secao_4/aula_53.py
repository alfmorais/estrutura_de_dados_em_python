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
        
    def imprime():
        if self.ultima_posicao == -1:
            print('O vetor está vazio.')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, '-', self.valores(i)


vetor = vetor_nao_ordenado(5)
vetor.imprime()
