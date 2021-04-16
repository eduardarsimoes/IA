# Inteligência Artificial - Trabalho 03 2020/2 EAD
### Alunos: Caicke Pinheiro e Eduarda Simões<BR><BR>

## Como executar
O código foi desenvolvido em **Python** e para executá-lo, navegue até o diretório em que o arquivo `.py` se encontra e execute o arquivo.

```
python3 pso.py
```
<BR>
	
## Definições
Alguns critérios foram definidos, conforme as especificações do trabalho, sendo respectivamente:<br>

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

<p align="justify">
	O algoritmo de otimização por enxame de partículas (<b>PSO</b>) é utilizado para tratar problemas no domínio contínuo. O PSO emergiu é um tipo de inteligência de enxame inspirado no comportamento de bandos de pássaros. A busca por alimentos e a interação entre aves ao longo do vôo são modeladas como um mecanismo de otimização. Fazendo uma analogia, o termo partícula é adotado para simbolizar os pássaros e representar as possíveis soluções do problema a ser resolvido. A área sobrevoada pelos pássaros é equivalente ao espaço de busca e encontrar o local com comida, ou o ninho, corresponde a encontrar a solução ótima. Para que o bando de pássaros sempre se aproxime do objetivo, ao invés de se perder ou nunca alcançar o alvo focado, utiliza-se o indicador denominado fitness, função que irá avaliar o desempenho das partículas. Para alcançar o alvo focado, sejam os alimentos ou os ninhos, os pássaros fazem uso de suas experiências e da experiência do próprio brando. O termo indicador da experiência ou conhecimento individual de cada partícula, isto é, seu histórico de vida, é o pbest. Em uma abordagem mais simples, o responsável por representar o conhecimento do enxame como um todo é o gbest. Para melhor entendimento:
</p>

<br>


![Tabela de identificação](https://github.com/eduardarsimoes/IA_Algoritmos/blob/main/A_pso/image/tabela_identificacao.PNG)

<BR>

## Implementação

![Fluxograma](https://github.com/eduardarsimoes/IA_Algoritmos/blob/main/A_pso/image/fluxograma.jpg)

Considerando o fluxograma, seguimos os seguintes passos:
- Iniciamos a população 
- Calculamos a aptidão e a melhor posição local até o momento de cada partícula
- Descobrimos a partícula com melhor aptidão global
- Atualizamos a velocidade e a nova posição para cada partícula
- Repetimos o processo até as condições de parada definidas

### Inicializando a população
Para inicializar a população, geramos posições aleatórias para cada partícula e uma velocidade aletória comum a todas elas.

![main inicializacao](https://github.com/eduardarsimoes/IA_Algoritmos/blob/main/A_pso/image/init.PNG)
![particula inicializacao](https://github.com/eduardarsimoes/IA_Algoritmos/blob/main/A_pso/image/particula_init.PNG)

### Calculando a aptidão e a melhor posição local
Para calcular a aptidão foi usada a função eggholder.

![particula aptidao](https://github.com/eduardarsimoes/IA_Algoritmos/blob/main/A_pso/image/particula_aptidao.PNG)
![main ptidao](https://github.com/eduardarsimoes/IA_Algoritmos/blob/main/A_pso/image/aptidao.PNG)

### Descobrindo a partícula com melhor aptidão na escala global
Feito os cálculos de aptidão, podemos descobrir qual partícula possui a melhor aptidão, para usar sua posição no cálculo de atualização de velocidade.

![Melhor aptidao](https://github.com/eduardarsimoes/IA_Algoritmos/blob/main/A_pso/image/gbest.PNG)

### Atualizando velocidade e posição local
Por fim, a velocidade e posição local são atualizadas através das respectivas fórmulas.

![main atualizacao](https://github.com/eduardarsimoes/IA_Algoritmos/blob/main/A_pso/image/atualizacao.PNG)

![particula atualizacao velocidade](https://github.com/eduardarsimoes/IA_Algoritmos/blob/main/A_pso/image/particula_atualizacao_v.PNG)

![particula atualizacao posicao](https://github.com/eduardarsimoes/IA_Algoritmos/blob/main/A_pso/image/particula_atualizacao_pos.PNG)

## Resultados


