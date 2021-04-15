# Inteligência Artificial - Trabalho 03 2020/2 EAD
### Alunos: Caicke Pinheiro e Eduarda Simões<BR><BR>

## Como executar
O código foi desenvolvido em **Python** e para executá-lo, navegue até o diretório em que o arquivo `.py` se encontra e execute o arquivo.

```
python3 pso.py
```
<BR>
## Definições
Alguns critérios foram definidos conforme orientação do trabalho, sendo respectivamente:<br>

   - número de partículas P da população: ?;</li>
   - velocidades iniciais: ~[-77, +77];</li>
   - intervalo de X: [−512, +512];</li>
   - intervalo de Y: [−512, +512];</li>
   - critério de parada: 20, 50 e 100 iterações;</li>
   - tamanho da população: 50 e 100 individuos;</li>
   - atualização velocidade da partícula: vi(t + 1) = W ∗ vi(t) + ϕ1 ∗ rand1(.) ∗ ( pB − xi(t) ) + ϕ2 ∗ rand2( gB − xi(t) );</li>
   - atualização da posição da partícula: xi(t + 1) + xi(t) + vi(t + 1);</li>
   - mínimo global:</li>
    ![Mínimo global](https://github.com/eduardarsimoes/IA_Algoritmos/blob/main/A_pso/image/minimo_global.PNG)
   - função eggholder:</li>
    ![Função eggholder](https://github.com/eduardarsimoes/IA_Algoritmos/blob/main/A_pso/image/funcao.PNG)

<BR>

## Explicação teórica

O **algoritmo pso** é uma técnica de busca utilizada na ciência da computação para achar soluções aproximadas em problemas de otimização e busca.

<br>

<figure style="text-align:center">
	<img src="https://www.electricalelibrary.com/wp-content/uploads/2018/04/Fluxograma-AG-PT.png" alt="tickstales.com" style="zoom:50%;" />
<i>Imagem retirada em <a href="www.electricalelibrary.com">www.electricalelibrary.com</a></i>
</figure>

<br>
<br>

O  que torna o algoritmo genético diferente de outros algoritmos tradicionais de otimização é que se baseia num conjunto de soluções possíveis, usando transações probabilísticas e seus resultados não são apresentados como solução única. A função-objetivo é o objeto da otimização, que nesse caso é dada como '<i><b>f(n)</b> = cos(X) * x + 2</i>'.  
<br>

## Implementação
Para a implementação do algoritmo, seguimos os seguintes passos:
<ul>
	<li>Iniciamos a população, com cada indivíduo sendo uma cadeia de bits aleatórios;</li>
	<li>Calculamos a aptidão de cada indíviduo, usando a função <i>fitness</i>;</li>
	<li>Selecionamos indívduos para o torneio, a fim de escolher os melhores pais</li>
	<li>Realizamos o crossover entre os pais, para gerar filhos com as cadeias de bits combinadas</li>
	<li>Realizamos o crossover entre os pais, para gerar filhos com as cadeias de bits combinadas</li>
	<li>Depois de obter a nova geração, realizamos mutação entre os indivíduos, porém mantendo os mais aptos (elitismo)</li>
</ul>

### Inicializando a população
Para inicializar a população, geramos uma cadeia aleatória, juntando um bit randômico 16 vezes (16bits) e inicializamos a aptidão com "- infinito", pois iremos calcular mais à frente e consequentemente, substituir o valor.

![inicializando-populacao](https://user-images.githubusercontent.com/37307708/111018959-f1364500-839a-11eb-9e3a-5d514b321a32.png)

### Calculando aptidão
No cálculo da aptidão, fixamos os valores mínimos e máximos entre -20 e 20, como dado na especificação e calculamos um valor x usando a função abaixo:

![funcao](https://user-images.githubusercontent.com/37307708/110559442-fc7f3b80-8122-11eb-8c0a-0982303f64bf.PNG)

Depois de calculada, colocamos a aptidão obtida em uma tupla, juntamente com o indivíduo correspondente.

![fitness-function](https://user-images.githubusercontent.com/37307708/111018980-0e6b1380-839b-11eb-8d7f-18a18d73be4a.PNG)

### Torneio com os melhores pais
Após descobrirmos as aptidões de cada indivíduos, os selecionamos aleatoriamente para dois torneios, disputando entre eles para ver quem tem a maior aptidão e escolhendo os ganhadores para serem os pais que iremos realizar o crossover.

![torneio](https://user-images.githubusercontent.com/37307708/111019020-568a3600-839b-11eb-8c40-8a0ef18fefb5.PNG)

Com isso, conseguimos realizar o crossover, combinando os genes dos melhores pais da geração.

### Crossover
No crossover, geramos um ponto de corte aleatório, misturamos os bits dos pais e, caso a taxa do bit fique abaixo da taxa escolhida como parâmetro (no nosso caso, 60%), ele é passado para a cadeia do filho.

![crossover](https://user-images.githubusercontent.com/37307708/111019044-74579b00-839b-11eb-9ec9-d9eade2c0749.PNG)

### Mutação
Depois disso, passamos a nova população gerada (menos os melhores - elitismo) para a nossa função de mutação.

![mutacao](https://user-images.githubusercontent.com/37307708/111019060-98b37780-839b-11eb-845e-ef18532b4d4b.PNG)

No elitismo, verificamos basicamente se "vale a pena" adicionar o filho gerado na próxima geração, ou seja, se o pior pai for
melhor que o melhor filho, o pai continua na próxima geração e o filho é excluído.

![elitismo](https://user-images.githubusercontent.com/37307708/111019088-c26c9e80-839b-11eb-93e0-881f97f7d00a.PNG)


## Resultados
A cada execução, os resultados variam, mas na média, os resultados foram bons, minimizando bastante da geração inicial para a geração 20 (por exemplo).

Nas figura abaixo, por exemplo, temos a comparação do resultado das gerações 1 e 20, com o algoritmo rodando com 10 interações.

![ger1](https://user-images.githubusercontent.com/37307708/111018902-a9afb900-839a-11eb-89f8-4a2d291b4364.PNG)
![ger20](https://user-images.githubusercontent.com/37307708/111018933-d06def80-839a-11eb-9ec4-1625614063e1.PNG)

Segue também a tabela das médias dos resultados para cada geração, de uma execução com 10 gerações:

![media-10-geracoes](https://user-images.githubusercontent.com/37307708/111019502-69523a00-839e-11eb-866b-17912ab61d31.PNG)
