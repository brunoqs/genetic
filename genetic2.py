import numpy as np
import random

class Genetic:

    def __init__(self, dna, n_populacao, taxa_crossover, taxa_mutacao, n_geracoes, limites, funcao):
        self.dna = dna  # tamanho do dna (cadeia de bits)
        self.n_populacao = n_populacao # tamanho da populacao
        self.taxa_crossover = taxa_crossover 
        self.taxa_mutacao = taxa_mutacao
        self.n_geracoes = n_geracoes # numero de geracoes
        self.limites = limites # limites da funcao 
        self.funcao = funcao 

        # criando populacao de forma randomica
        populacao = np.random.randint(2, size=(self.n_populacao, self.dna)) 
        self.populacao = populacao.tolist()

    def f(self, x):
        return self.funcao(x)

    def bin_to_int(self, binario):
        bin_str = ''.join(str(b) for b in binario)
        bin_str = '0b' + bin_str
        return int(bin_str, 2)

    # selecionar em 2 dna's aleatorios o melhor
    def selecao(self):
        pop1 = random.randint(0, len(self.populacao)-1)
        pop2 = random.randint(0, len(self.populacao)-1)
        
        melhor = max(self.bin_to_int(self.populacao[pop1]), self.bin_to_int(self.populacao[pop2]))

        if self.bin_to_int(self.populacao[pop1]) == melhor:
            return self.populacao[pop1]
        else:
            return self.populacao[pop2]
    
    def crossover(self, dna):
        if np.random.rand() < self.taxa_crossover:
            # escolhe o ponto de corte aleatoriamente
            corte = random.randint(0, self.dna) 
            for x in range(self.n_populacao):
                for y in range(corte, self.dna):
                    self.populacao[x][y] = dna[y]

    def mutacao(self, dna):
        for x in range(self.n_populacao):
            for y in range(self.dna):
                if np.random.rand() < self.taxa_mutacao:
                    self.populacao[x][y] = dna[y] 


def run(g):
    # fazer crossover e mutacao para cada geracao
    for i in range(g.n_geracoes):
        k = g.selecao()
        g.crossover(k)
        g.mutacao(k)

    for i in range(g.n_populacao):
        print(g.populacao[i], g.bin_to_int(g.populacao[i]), g.f(g.bin_to_int(g.populacao[i])))

if __name__ == '__main__':
    g = Genetic(
        dna=5,
        n_populacao=30,
        taxa_crossover=0.7,
        taxa_mutacao=0.1,
        n_geracoes=20,
        limites=[-10, 10],
        funcao=lambda x: x**2 - 3*x + 4
    )

    run(g)