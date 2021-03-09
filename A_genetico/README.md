# Inteligência Artificial - Trabalho 02 2020/2 EAD
### Alunos: Caicke Pinheiro e Eduarda Simões<BR><BR>

## Como executar
O código foi desenvolvido em **Python** e para executá-lo, navegue até o diretório em que o arquivo `.py` se encontra e execute o arquivo.

```
python3 a-genetico.py
```
<BR>
## Definições
Alguns critérios foram definidos conforme orientação do trabalho, sendo respectivamente:<br>
<ul>
    <li>numero de individuos na populacao = 10;</li>
    <li>minimo de X = -20;</li>
    <li>maximo de X = 20;</li>
    <li>torneio = 2;</li>
    <li>geracoes = 10 e 20;</li>
	<li>cromossomos por individuo = 16 bits</li>
</ul><br>
E, a partir disso, outros foram definidos pelo grupo, são eles:<br>
<ul>
    <li>numero de elitismo = 2;</li>
    <li>numero de descendentes (crossover) na nova geracao = 2;</li>
</ul>
<BR>

## Explicação teórica

O **algoritmo genético** é uma técnica de busca utilizada na ciência da computação para achar soluções aproximadas em problemas de otimização e busca.

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

## Resultado
