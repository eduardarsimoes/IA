import sys
import time
# funcao que le a matriz do arquivo e molda numa lista


def leMatriz(arq):
    arq = open("mapa.txt", "r")
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


def heuristica(pAtual, pProx):
    # distancia de manhattan
    (x1, y1) = pAtual[0], pAtual[1]
    (x2, y2) = pProx[0], pProx[1]
    return abs(x1 - x2) + abs(y1 - y2)


def desenhaCaminho(mapa, caminho, ini, fim):
    print('\n\nCaminho a ser percorrido:\n')
    impr = ''
    caminho.reverse()
    for item in caminho:
        impr += "("+str(item[0])+","+str(item[1]) + ") -> "
        #print(item, end="")
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


def a_star(matriz, naoAchou, posInicial, posFinal, inicio, fim):
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

        # posicoes:  0 = ^,   1 = >,  2 = v,  3 = <
        for pos in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            posVizinho = (posAtual[0] + pos[0], posAtual[1] + pos[1])

            # se vizinho estiver em uma das listas
            if posVizinho in dic or posVizinho == posInicial:
                continue

            # se nao existir vizinho
            if posVizinho[0] < 0 or posVizinho[1] < 0 or posVizinho[0] >= len(matriz) or posVizinho[1] >= len(matriz[-1]):
                continue

            # se vizinho for barreira
            if matriz[posVizinho[0]][posVizinho[1]] == 1:
                continue

            # se vizinho for objetivo
            if posVizinho == posFinal:
                naoAchou = False
                break

            # calculando g, h e f
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


def main():
    start = time.time()
    naoAchou = True

    arquivo = sys.argv[1]

    posInicial = int(sys.argv[2].strip()), int(sys.argv[3].strip())

    matriz = leMatriz(arquivo)
    inicio = matriz[posInicial[0]][posInicial[1]]

    posFinal = int(sys.argv[4].strip()), int(sys.argv[5].strip())
    objetivo = matriz[posFinal[0]][posFinal[1]]

    caminho = a_star(matriz, naoAchou, posInicial, posFinal, inicio, objetivo)
    desenhaCaminho(matriz, caminho, posInicial, posFinal)
    end = time.time()
    print()
    print("Tempo de execução: %.3f segundos" % (end-start))
    print()


if __name__ == '__main__':
    main()
