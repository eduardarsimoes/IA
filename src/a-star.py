import sys

# Funcao que le a matriz do arquivo
def leMatriz(arq):
    arq = open("mapa.txt", "r")
    linha = arq.readline()
    linhas = []
    matriz = []
    
    while linha != "":
        lin = linha.strip().split(" ")
        linhas.append(lin)
        linha = arq.readline()

    # Transforma os elementos matriz em numeros inteiros
    for elem in linhas:
        valores = [int(val) for val in elem]
        matriz.append(valores)
        
    return matriz

# Funcao que calcula a distancia dos pontos
def heuristica(pAtual, pProx):
    # Distancia de manhattan
    (x1, y1) = pAtual[0], pAtual[1]
    (x2, y2) = pProx[0], pProx[1]
    
    return abs(x1 - x2) + abs(y1 - y2)

# Funcao que desenha o caminho percorrido do ponto de partida ao ponto final
def desenhaCaminho(mapa, caminho, ini, fim):
    print('\n\nCaminho a ser percorrido:\n')
    impr = ''
    caminho.reverse()
    
    for item in caminho:
        impr += "("+str(item[0])+","+str(item[1]) + ") -> "
    print(impr[:-4])

    for item in caminho:
        mapa[ini[0]][ini[1]] = 'start'  # marca um x no começo
        mapa[item[0]][item[1]] = '*'
    print()
    
    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            print("\t", mapa[i][j], end="")
        print()

        mapa[fim[0]][fim[1]] = 'end'  # marca um x na chegada
    print()

# Funcao A*
def a_star(matriz, naoAchou, posInicial, posFinal):
    listaAberta = []
    listaFechada = []
    dic = {}
    
    while naoAchou:
        if not listaAberta:
            atual = [None, posInicial, None]
            listaAberta.append(atual)
            posAtual = posInicial
            dic[posInicial] = 0
        else:
            atual = listaAberta[0]
            posAtual = atual[1]

        # Posicoes:  0 = ^,   1 = >,  2 = v,  3 = <
        for pos in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            posVizinho = (posAtual[0] + pos[0], posAtual[1] + pos[1])

            # Verifica se vizinho ja foi visitado anteriormente
            if posVizinho in dic or posVizinho == posInicial:
                continue

            # Verifica se as posicoes estao fora da matriz
            if verifica_posicoes(matriz, posVizinho):
                continue
            
            # Verifica se vizinho é uma barreira
            if matriz[posVizinho[0]][posVizinho[1]] == 1:
                continue

            # Verifica se vizinho é o objetivo
            if posVizinho == posFinal:
                naoAchou = False
                break

            # Calcula h, g e f
            h = heuristica(posVizinho, posFinal)
            g = int(dic.get(posAtual)) + 1
            f = g + h

            dic[posVizinho] = g
            listaAberta.append([f, posVizinho, posAtual])

        listaAberta.remove(atual)
        listaFechada.append(atual)
        listaAberta.sort(key=lambda x: x[0])

    caminho = []
    pai = posAtual
    caminho.append(posVizinho)
    
    for i in range(len(listaFechada)-1, -1, -1):
        if listaFechada[i][1] == pai:
            caminho.append(pai)
            pai = listaFechada[i][2]

    return caminho

# Funcao que verifica se as posicoes estao fora da matriz
def verifica_posicoes(matriz, pos):
    if pos[0] < 0 or pos[1] < 0 or pos[0] >= len(matriz) or pos[1] >= len(matriz[-1]):
        return True
    return False

# Funcao que pede para inserir posicoes adequadas com a matriz
def ajustes_posicoes(pos, frase):
    pos = input("Posicoes {} incorretas, insira novamente: ".format(frase)).strip()
    return int(pos[0]), int(pos[1])

# Main
def main():
    naoAchou = True

    arquivo = sys.argv[1]
    matriz = leMatriz(arquivo)
    
    posInicial = int(sys.argv[2].strip()), int(sys.argv[3].strip())
    posFinal = int(sys.argv[4].strip()), int(sys.argv[5].strip())
    
    # Verifica se as posicoes estao de acordo com a matriz passada
    while verifica_posicoes(matriz, posInicial):
        posInicial = ajustes_posicoes(posInicial, "iniciais")
        
    while verifica_posicoes(matriz, posFinal):
        posFinal = ajustes_posicoes(posInicial, "finais")

    # Calcula e printa o caminho na tela
    caminho = a_star(matriz, naoAchou, posInicial, posFinal)
    desenhaCaminho(matriz, caminho, posInicial, posFinal)


if __name__ == '__main__':
    main()
