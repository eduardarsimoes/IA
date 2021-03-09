import random
import math

geracoes      = []
population    = []
novageracao   = []

# Gera populacao inicial
def populationInitialization(numeroIndividuos):
  global population, novageracao

  if novageracao:
    geracoes.append(population)
    population = []
    population = novageracao.copy()
    novageracao = []
    numeroIndividuos = numeroIndividuos - len(population)

  for i in range (numeroIndividuos):
    cromossomos = ''
    
    for j in range(16):
      bit = random.randint(0,1)
      if cromossomos == '':
        cromossomos = str(bit)
      else:
        cromossomos += str(bit)

    population.append([cromossomos, math.inf])
  
  #print("POPULACAO INICIAL: \n{}\n\n".format(population))


# Calcula aptidao
def fitnessFuction(minimo, maximo, bits):
  global population

  # Calculando cada individuo
  for i in range (len(population)):
    decimal = int(population[i][0],2)

    # x ∈ [−20, +20]
    x = minimo + (((maximo - minimo) * decimal)/(2 ** bits) - 1)
    
    # Cálculo de aptidão
    aptidao = round(math.cos(x) * x + 2,2)
    
    population[i][1] = aptidao

  # Ordenando, pois queremos o minimo
  population.sort(key = lambda x:x[1])
  #print("INDIVIDUOS INICIAIS COM RESPECTIVAS APTIDAO: \n{}\n\n".format(population))


# Por torneio = 2 pais
def selection(torneio):
  global population
  pais = []

  for i in range(len(population)):
    individuo1 = population[random.randint(0, len(population)-1)]
    individuo2 = population[random.randint(0, len(population)-1)]

    #print('PAI {} x PAI {} \n'.format(individuo1,individuo2))
    
    if min(individuo1[1], individuo2[1]) == individuo1[1]:
      pai = individuo1
    else:
      pai = individuo2
    
    pais.append(pai)

    #print('PAI VENCEDOR {} \n'.format(pai))
  
  #print("{} PAIS: \n{}\n\n".format(len(pais),pais))

  return pais


#r <= 0,6
def crossOver(pais):
  filho = ''
  filha = ''
  filhos = []
  global novageracao

  for i in range(0,len(pais),2):
    r = round(random.uniform(0,1),1)

    if r <= 0.6:
      corte = random.randint(0,15)
      filho = pais[i][0:corte] + pais[i+1][corte:len(pais[i+1])]
      filha = pais[i+1][0:corte] + pais[i][corte:len(pais[i])]
    else:
      filho = pais[i]
      filha = pais[i+1]

    filhos.append(filho)
    filhos.append(filha)
    
  #print("\n{} Filhos CrossOver: \n{}\n\n".format(len(novageracao),novageracao))
  return filhos


#r <= 0,01
def mutation(filhos):

  for i in range(len(filhos)):
    individuo = filhos[i][0]
    for j in range(len(individuo)):
      
      r = round(random.uniform(0,1), 2)
           
      if r <= 0.01:
        if individuo[i] == "0":
          individuo = individuo[:i] + "1" + individuo[i+1:]
        else:
          individuo = individuo[:i] + "0" + individuo[i+1:]
  
  return filhos
  #print("Filho Mutacao: \n{}\n\n".format(individuo))
  


# Elitismo: guardando os melhores para a nova geracao, nesse caso: 2
def elitismo(filhos, pais, qtdElitismo):
  global novageracao

  filhos.sort(key = lambda x:x[1])
  pais.sort(key = lambda x:x[1])

  for i in range(qtdElitismo):
    novageracao.append(filhos[i])
    novageracao.append(pais[i])


def printaTabelas():
  global geracoes

  contador = 0
  for geracao in geracoes:
    if contador == 0:
      print("######## POPULACAO INICIAL ########")
    else:
      print("######## GERACAO {} ########".format(contador))
    print("____________________________")
    print("    INDIVIDUOS     |  F(x)  ")
    for individuo in geracao:
      print(individuo)
    print("____________________________\n\n\n\n")
    
    contador +=1



def main():
  nmrIndividuos = 10  
  minimo        = -20 #menorValorX
  maximo        = 20  #maiorValorX
  qtdBits       = 16  #qtdCromossomos
  torneio       = 2   #qtdPaisCrossOver
  qtdElitismo   = 2   #qtdMelhoresAptidoesParaNovaGeracao
  qtdGeracoes   = 10
  solucao       = True

  i = 2
  while i > 0: 
    while solucao:
      # Inicializa a populacao
      populationInitialization(nmrIndividuos)

      # Calcula aptidao dos individuos
      fitnessFuction(minimo, maximo, qtdBits)

      # Seleciona individuos aleatorios para serem pais
      pais = selection(torneio)

      # Faz o crossover dos individuos
      filhos = crossOver(pais)

      # Aplica mutacao em todos menos no melhor individuo
      filhos = mutation(filhos)

      # Sobrevivencia
      elitismo(filhos, pais, qtdElitismo)

      if len(geracoes) == qtdGeracoes+1:
        printaTabelas()
        solucao = False
        print("############################ \n\n")
    i -=1
    qtdGeracoes = 20
    solucao = True
    

if __name__ == '__main__':
  main()
