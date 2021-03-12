import random
import math
import numpy

geracoes = []
novageracao = []


# Gera populacao inicial
def populationInitialization():
    nmrIndividuos = 10  # populacao
    minimo = -20  # menorValorX
    maximo = 20  # maiorValorX
    qtdBits = 16  # qtdCromossomos
    population = []

    for i in range(nmrIndividuos):
        cromossomos = ''

        for j in range(qtdBits):
            bit = random.randint(0, 1)
            if cromossomos == '':
                cromossomos = str(bit)
            else:
                cromossomos += str(bit)

        population.append([cromossomos, math.inf])

    # Calcula aptidao dos individuos
    population = fitnessFunction(minimo, maximo, qtdBits, population)

    return population
    # print("POPULACAO INICIAL:\n ", population)


# Calcula aptidao
def fitnessFunction(minimo, maximo, bits, population):
    # Calculando cada individuo
    for i in range(len(population)):
        decimal = int(population[i][0], 2)

        # x ∈ [−20, +20]
        x = minimo + (((maximo - minimo) * decimal) / ((2 ** bits) - 1))

        # Cálculo de aptidão
        aptidao = round((math.cos(x) * x) + 2, 2)

        population[i][1] = aptidao

    # Ordenando, pois queremos o minimo
    population.sort(key=lambda fitness: fitness[1])

    # print("\n POPULACAO COM APTIDAO CALCULADA:\n", population)
    return population


# Por torneio = 2 pais
def selection(population):
    pais = []

    for i in range(len(population)):
        individuo1 = population[random.randint(0, len(population) - 1)]
        individuo2 = population[random.randint(0, len(population) - 1)]

        if min(individuo1[1], individuo2[1]) == individuo1[1]:
            pai = individuo1
        else:
            pai = individuo2
        pais.append(pai)

    # print("\nPAIS SELECIONADOS: \n", pais)
    return pais


# r <= 0,6
def crossOver(pais, torneio):
    filhos = []

    for i in range(0, len(pais) - 1, torneio):
        r = round(random.uniform(0, 1), 1)
        if r <= 0.6:
            corte = random.randint(1, 16)

            pai1 = pais[i][0]
            pai2 = pais[i + 1][0]
            # print(pai1, pai2)
            # print(pai1[0:corte], pai2[corte:len(pai2)], pai1[0:corte] + pai2[corte:len(pai2)])
            filho = [pai1[0:corte] + pai2[corte:len(pai2)], math.inf]
            filha = [pai2[0:corte] + pai1[corte:len(pai1)], math.inf]
            # print("Filho: \n", filho)
            # print("Filha: \n", filha)
        else:
            filho = pais[i]
            filha = pais[i + 1]

        filhos.append(filho)
        filhos.append(filha)
    # print("\nFILHOS CROSSOVER: \n", filhos)
    return filhos


# r <= 0,01
def mutation(filhos):
    for i in range(len(filhos)):
        individuo = filhos[i][0]

        for j in range(len(individuo)):
            r = round(random.uniform(0, 1), 2)

            if r <= 0.01:
                if individuo[j] == "0":
                    individuo = individuo[:j] + "1" + individuo[j + 1:]
                else:
                    individuo = individuo[:j] + "0" + individuo[j + 1:]
    # print("\nFILHOS MUTACAO: \n", filhos)
    fitnessFunction(-20, 20, 16, filhos)
    # print("\nFILHOS MUTACAO - DEPOIS APTIDAO: \n", filhos)
    return filhos


# Elitismo: guardando os melhores para a nova geracao, nesse caso: 2
def elitismo(filhos, population):
    global novageracao
    global geracoes

    filhos.sort(key=lambda x: x[1])
    population.sort(key=lambda x: x[1])

    if filhos[-1] > population[0]:
        for i in range(len(filhos)):
            if filhos[i][1] == population[-1][1]:
                del filhos[i]
                break
        filhos.append(population[0])

    filhos.sort(key=lambda x: x[1])
    # print("\nMelhor aptidao: {}".format(filhos[0][1]))
    novageracao = filhos.copy()
    geracoes.append(novageracao)
    novageracao = []


def printaTabelas():
    global geracoes
    soma = 0
    contador = 1
    for geracao in geracoes:
        print("######## GERACAO {} ########".format(contador))
        print("____________________________")
        print("    INDIVIDUOS     |  F(x)  ")
        for individuo in geracao:
            print(individuo)
            soma += individuo[1]
        print("____________________________")
        print("MELHOR APTIDAO: {}".format(min(geracao, key=lambda x: x[1])[1]))
        print("MEDIA: {}\n\n".format(soma / len(geracao)))
        contador += 1


def main():
    global geracoes

    torneio = 2  # qtdPaisCrossOver
    qtdGeracoes = 10  # inicialmente
    totalGeracoes = 2  # 1 rodada com 10 e uma com 20 geracoes

    while totalGeracoes > 0:

        # Inicializa a populacao
        population = populationInitialization()

        solucao = True
        while solucao:

            # Seleciona individuos aleatorios para serem pais
            pais = selection(population)

            # Faz o crossover dos individuos
            filhos = crossOver(pais, torneio)

            # Aplica mutacao em todos menos no melhor individuo
            filhos = mutation(filhos)

            # Sobrevivencia
            elitismo(filhos, population)

            if len(geracoes) == qtdGeracoes:
                printaTabelas()
                print("############################ FIM\n\n")
                solucao = False

        totalGeracoes -= 1
        qtdGeracoes = 20


if __name__ == '__main__':
    main()
