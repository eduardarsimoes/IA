import sys

# Distância do ponto ao ponto de objetivo
def heuristica(pAtual, pProx):
  (x1, y1) = pAtual[0], pAtual[1]
  (x2, y2) = pProx[0], pProx[1]
  return abs(x1 - x2) + abs(y1 - y2)  

def leMatriz(arquivo):
    arq = open(arquivo, "r")
    linha = arq.readline()
    linhas = []
    matriz = []
    while linha != "":
        lin = linha.strip().split(" ")
        linhas.append(lin)
        linha = arq.readline()

    # transforma os elementos matriz em numeros inteiros
    for elem in linhas:
        valores = [int(val) for val in elem]
        matriz.append(valores)
    return matriz

def printaCaminho(mapa, caminho):

  print('\n\nCaminho\n')
  impr = ''
  for item in caminho:
    impr += "("+str(item[0])+","+str(item[1]) + ") -> "
  print(impr[:-4])

  for item in caminho:
    mapa[item[0]][item[1]] = '*'
  print()
  for i in range(len(mapa)):
    for j in range(len(mapa[0])):
      print("\t", mapa[i][j], end="")
      
    print()
# A*
def a_star(matriz, posInicial, posFinal, inicio, objetivo):
  naoAchou = True
  listaAberta = []
  listaFechada = []
  dic = {}

  while naoAchou:
    if listaAberta == []:
      atual = [None, posInicial, None]
      listaAberta.append(atual)
      posAtual = posInicial
      dic[posInicial] = 0
    else:
      atual = listaAberta[0]
      posAtual = atual[1]
    
    # Posicoes:    ^,      >,       v,      <
    for pos in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
      posVizinho = (posAtual[0] + pos[0], posAtual[1] + pos[1])
      
      # Verifica se vizinho esta em uma das listas
      if posVizinho in dic or posVizinho == posInicial:
        continue
      
      # Verifica se não existe a posição do vizinho
      if posVizinho[0] < 0 or posVizinho[1] < 0 or posVizinho[0] >= len(matriz) or posVizinho[1] >= len(matriz[-1]):
        continue

      # Verifica se a posição do vizinho é uma barreira
      if matriz[posVizinho[0]][posVizinho[1]] == 1:
        continue

      # Verifica se vizinho é o objetivo final
      if posVizinho == posFinal:
        naoAchou = False
        break
        
      # Calcula os valores de g, h e f
      h = heuristica(posVizinho, posFinal)
      g = int(dic.get(posAtual)) + 1 # De acordo com seu pai
      f = g + h
    
      dic[posVizinho] = g
      listaAberta.append([f,posVizinho,posAtual])
    
    # Atualiza as listas
    listaAberta.remove(atual)
    listaFechada.append(atual)
    listaAberta.sort(key=lambda x:x[0])
  
  # Define o caminho de acordo com seus pais
  caminho = []
  pai = posAtual
  caminho.append(posVizinho)
  for i in range(len(listaFechada)-1,-1,-1):
    if listaFechada[i][1] == pai:
      caminho.append(pai)
      pai = listaFechada[i][2]
  return caminho

def main():
  
  # Define
  
  # python main.py mapa.txt 0 0 9 8
  # ou python main.py mapa.txt 0, 0, 9, 8
  arquivo = sys.argv[1]

  posInicial = int(sys.argv[2].strip(",")), int(sys.argv[3].strip(","))

  matriz = leMatriz(arquivo)
  inicio = matriz[posInicial[0]][posInicial[1]]

  posFinal = int(sys.argv[4].strip(",")), int(sys.argv[5].strip(","))
  objetivo = matriz[posFinal[0]][posFinal[1]]

  caminho = a_star(matriz, posInicial, posFinal, inicio, objetivo)
  

  printaCaminho(matriz, caminho)

if __name__ == '__main__':
  main()
