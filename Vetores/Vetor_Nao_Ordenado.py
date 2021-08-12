# -*- coding: utf-8 -*-

import numpy as np


class VetorNaoOrdenado:
    def __init__(self, capacidade):
        # contrutor da classe
        self.capacidade = capacidade  # self.capacidade cria a propriedade capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)  # Cria um array com o tamanho e tipo passados

    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i])

    # O(1) ou O(2)
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
                return i  # retorna o index de onde está alocado o valor
        return -1

    # O(n)
    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:  # Se não foi encontrado a posição retorna -1
            return -1
        else:  # Sobrescreve a posição com os valores posteriores e subtrai 1 posição da ultima posição
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao -= 1


vetor = VetorNaoOrdenado(5)


vetor.insere(3)
vetor.insere(2)
vetor.insere(4)
vetor.insere(5)
vetor.insere(6)
vetor.insere(1)

vetor.imprime()

vetor.pesquisar(5)

vetor.pesquisar(9)

vetor.excluir(2)

