**Sobre o Sistema Educacional e Ambientes - R**
==================================================

O **Exame Nacional do Ensino M�dio**, ou
[ENEM](https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/enem),
ocorre todo ano - desde 1998 - e � a maior prova do Brasil, com cerca de
[5 milh�es de inscri��es por
ano](http://portal.inep.gov.br/artigo/-/asset_publisher/B4AQV9zFY7Bv/content/5-8-milhoes-estao-inscritos-para-fazer-o-enem-2020/21206#:~:text=Finalizadas%20as%20etapas%20de%20inscri%C3%A7%C3%A3o,Ensino%20M%C3%A9dio%20(Enem)%202020.).   

Nesse �ltimo ano, a prova foi um pouco diferente, devido ao coronav�rus,
que acarretou em adia��o da prova, diversas
[medidas](https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/enem/orientacoes/medidas-de-prevencao-a-covid-19)
preventivas para a realiza��o do exame e a maior absten��o da hist�ria:
[mais da metade dos candidatos n�o foram realizar o
exame](https://educacao.uol.com.br/noticias/2021/01/17/mec-culpa-medo-da-covid-19-e-midia-contra-por-abstencao-de-515-no-enem.htm). 

![](https://github.com/KenzoBH/Data-Science/blob/main/Images/Slide2.PNG)

De fato, trata-se de uma grande experi�ncia na vida do estudante
brasileiro que busca uma vaga na universidade, visto que o ENEM � uma
porta de entrada para diversas faculdades acerca do pa�s - al�m de ser o
processo seletivo das universidades federais do Brasil. Diversas
universidades (inclusive p�blicas), al�m de seus pr�prios vestibulares,
oferecem vagas exclusivas para o exame, pelo
[SiSU](https://sisu.mec.gov.br/) (Sistema de Sele��o Unificada), e
diversas universidades particulares oferecem bolsas de estudos aos
participantes relativas �s suas notas no exame.   

A prova � realizada em dois dias: um reservado para as disciplinas de
Ci�ncias Humanas, Linguagens e a Reda��o, e outro dia para Matem�tica e
Ci�ncias da Natureza (atualmente a prova segue sse padr�o, mas j� foi
diferente, e pode ser diferente no momento de sua leitura).   

Neste artigo, a gente vai explorar um pouco os dados - disponibilizados
pelo pr�prio [Inep](https://enem.inep.gov.br/participante/), �rg�o
respons�vel pelo exame - relativos aos exames de 2007 a 2015 organizados
por escola. Os dados foram baixados neste
[link](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem-por-escola).   

� not�vel, portanto, que a escola em que o candidato estudou tem forte
influ�ncia no seu desempenho. Muitas vezes, com um ensino n�o t�o bom em
suas escolas, muitos buscam fazer cursinhos preparat�rios para o ENEM.   
Veremos a seguir as rela��es entre a natureza da escola com o desempenho
de seus estudantes. Como o ambiente influencia no futuro do candidato?
Influencia de fato? Veremos!  

***

## Sum�rio

1. [Importa��o do dataset](https://github.com/KenzoBH/Data-Science/blob/main/ENEM/ENEM.md#1-importa%C3%A7%C3%A3o-do-dataset)
2. [Brasil](https://github.com/KenzoBH/Data-Science/blob/main/ENEM/ENEM.md#2-brasil)
    1. [Desempenho por estado: qual o melhor estado em Ci�ncias Humanas?](https://github.com/KenzoBH/Data-Science/blob/main/ENEM/ENEM.md#21-desempenho-por-estado-qual-o-melhor-estado-em-ci%C3%AAncias-humanas)
    2. [Desempenho por tipo administrativo: escolas privadas v�o melhor no ENEM?](https://github.com/KenzoBH/Data-Science/blob/main/ENEM/ENEM.md#22-desempenho-por-tipo-administrativo-escolas-privadas-v%C3%A3o-melhor-no-enem)
3. [Sudeste](https://github.com/KenzoBH/Data-Science/blob/main/ENEM/ENEM.md#3-sudeste)
    1. [Desempenho no sudeste: SP � o melhor estado no ENEM?](https://github.com/KenzoBH/Data-Science/blob/main/ENEM/ENEM.md#31-desempenho-no-sudeste-sp-%C3%A9-o-melhor-estado-no-enem)
    2. [Desempenho no sudeste por tipo adminstrativo: como s�o as federais?](https://github.com/KenzoBH/Data-Science/blob/main/ENEM/ENEM.md#32-desempenho-no-sudeste-por-tipo-adminstrativo-como-s%C3%A3o-as-federais)
4. [S�o Paulo](https://github.com/KenzoBH/Data-Science/blob/main/ENEM/ENEM.md#4-s%C3%A3o-paulo)
    1. [Desempenho pela localiza��o: escolas urbanas e rurais](https://github.com/KenzoBH/Data-Science/blob/main/ENEM/ENEM.md#4-s%C3%A3o-paulo)
    2. [S�o Paulo capital: a geografia na nota](https://github.com/KenzoBH/Data-Science/blob/main/ENEM/ENEM.md#4-s%C3%A3o-paulo)
    3. [Sobre as p�blicas](https://github.com/KenzoBH/Data-Science/blob/main/ENEM/ENEM.md#43-sobre-as-p%C3%BAblicas)
    4. [Sobre as escolas t�cnicas](https://github.com/KenzoBH/Data-Science/blob/main/ENEM/ENEM.md#44-sobre-as-escolas-t%C3%A9cnicas)    
5. [Conclus�o](https://github.com/KenzoBH/Data-Science/blob/main/ENEM/ENEM.md#5-conclus%C3%A3o)

***

## 1. Importa��o do dataset

Primeiro, vamos importar as bibliotecas que iremos utilizar. A
biblioteca `tidyverse` ser� respons�vel pela manipula��o e visualiza��o
dos dados, enquanto que a `knitr` apenas para a melhor exposi��o das
tabelas aqui.

    library(tidyverse)
    library(knitr)

Assim que importadas, podemos fazer a leitura do *dataset*. O arquivo
baixado no site do Inep no link exposto tamb�m continham o dicion�rio
das vari�veis, que est� disposto mais abaixo, apenas com colunas que
iremos uilizar na nossa an�lise.

    enem <- read.csv("MICRODADOS_ENEM_ESCOLA.csv", sep=';')
    kable(
      head(enem)
      )

<table style="width:100%;">
<colgroup>
<col style="width: 1%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 4%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 1%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 3%" />
<col style="width: 4%" />
<col style="width: 3%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: right;">NU_ANO</th>
<th style="text-align: right;">CO_UF_ESCOLA</th>
<th style="text-align: left;">SG_UF_ESCOLA</th>
<th style="text-align: right;">CO_MUNICIPIO_ESCOLA</th>
<th style="text-align: left;">NO_MUNICIPIO_ESCOLA</th>
<th style="text-align: right;">CO_ESCOLA_EDUCACENSO</th>
<th style="text-align: left;">NO_ESCOLA_EDUCACENSO</th>
<th style="text-align: right;">TP_DEPENDENCIA_ADM_ESCOLA</th>
<th style="text-align: right;">TP_LOCALIZACAO_ESCOLA</th>
<th style="text-align: right;">NU_MATRICULAS</th>
<th style="text-align: right;">NU_PARTICIPANTES_NEC_ESP</th>
<th style="text-align: right;">NU_PARTICIPANTES</th>
<th style="text-align: right;">NU_TAXA_PARTICIPACAO</th>
<th style="text-align: right;">NU_MEDIA_CN</th>
<th style="text-align: right;">NU_MEDIA_CH</th>
<th style="text-align: right;">NU_MEDIA_LP</th>
<th style="text-align: right;">NU_MEDIA_MT</th>
<th style="text-align: right;">NU_MEDIA_RED</th>
<th style="text-align: right;">NU_MEDIA_OBJ</th>
<th style="text-align: right;">NU_MEDIA_TOT</th>
<th style="text-align: left;">INSE</th>
<th style="text-align: right;">PC_FORMACAO_DOCENTE</th>
<th style="text-align: right;">NU_TAXA_PERMANENCIA</th>
<th style="text-align: right;">NU_TAXA_APROVACAO</th>
<th style="text-align: right;">NU_TAXA_REPROVACAO</th>
<th style="text-align: right;">NU_TAXA_ABANDONO</th>
<th style="text-align: left;">PORTE_ESCOLA</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: right;">2007</td>
<td style="text-align: right;">11</td>
<td style="text-align: left;">RO</td>
<td style="text-align: right;">1100205</td>
<td style="text-align: left;">Porto Velho</td>
<td style="text-align: right;">11000058</td>
<td style="text-align: left;">CENTRO DE ENSINO CLASSE A</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">144</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">140</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">69.03</td>
<td style="text-align: left;"></td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">91.9</td>
<td style="text-align: right;">8.1</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">Maior que 90 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2006</td>
<td style="text-align: right;">11</td>
<td style="text-align: left;">RO</td>
<td style="text-align: right;">1100205</td>
<td style="text-align: left;">Porto Velho</td>
<td style="text-align: right;">11000058</td>
<td style="text-align: left;">CENTRO DE ENSINO CLASSE A</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">184</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">139</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">57.82</td>
<td style="text-align: left;"></td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: left;">Maior que 90 alunos</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2005</td>
<td style="text-align: right;">11</td>
<td style="text-align: left;">RO</td>
<td style="text-align: right;">1100205</td>
<td style="text-align: left;">Porto Velho</td>
<td style="text-align: right;">11000058</td>
<td style="text-align: left;">CENTRO DE ENSINO CLASSE A</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">220</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">145</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">64.83</td>
<td style="text-align: left;"></td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">86.5</td>
<td style="text-align: right;">12.4</td>
<td style="text-align: right;">1.1</td>
<td style="text-align: left;">Maior que 90 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2008</td>
<td style="text-align: right;">11</td>
<td style="text-align: left;">RO</td>
<td style="text-align: right;">1100205</td>
<td style="text-align: left;">Porto Velho</td>
<td style="text-align: right;">11000058</td>
<td style="text-align: left;">CENTRO DE ENSINO CLASSE A</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">186</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">171</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">72.16</td>
<td style="text-align: right;">60.02</td>
<td style="text-align: right;">NA</td>
<td style="text-align: left;"></td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">90.3</td>
<td style="text-align: right;">9.7</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">Maior que 90 alunos</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2007</td>
<td style="text-align: right;">11</td>
<td style="text-align: left;">RO</td>
<td style="text-align: right;">1100205</td>
<td style="text-align: left;">Porto Velho</td>
<td style="text-align: right;">11000171</td>
<td style="text-align: left;">CENTRO EDUCACIONAL MOJUCA</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">19</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">12</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">58.84</td>
<td style="text-align: left;"></td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">74.2</td>
<td style="text-align: right;">21.0</td>
<td style="text-align: right;">4.8</td>
<td style="text-align: left;">De 1 a 30 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2008</td>
<td style="text-align: right;">11</td>
<td style="text-align: left;">RO</td>
<td style="text-align: right;">1100205</td>
<td style="text-align: left;">Porto Velho</td>
<td style="text-align: right;">11000171</td>
<td style="text-align: left;">CENTRO EDUCACIONAL MOJUCA</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">33</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">13</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">59.81</td>
<td style="text-align: right;">42.49</td>
<td style="text-align: right;">NA</td>
<td style="text-align: left;"></td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">79.1</td>
<td style="text-align: right;">17.9</td>
<td style="text-align: right;">3.0</td>
<td style="text-align: left;">De 31 a 60 alunos</td>
</tr>
</tbody>
</table>

Irei verificar a propor��o de dados faltantes (`NA`) em cada coluna com
um la�o `for`. Irei imprimir aquelas em que a propor��o ultrapassa os
70%.

    for (i in 1:length(enem)){
      prop_na = (sum(is.na(enem[i]))/length(enem[[i]])) * 100 # calculo da propor��o em %
      if (prop_na > 70) {
      print(str_c(names(enem)[i], " = ", (prop_na)))
      }
    }

    ## [1] "NU_PARTICIPANTES_NEC_ESP = 73.6774904965033"
    ## [1] "NU_MEDIA_OBJ = 88.8894692551"
    ## [1] "NU_MEDIA_TOT = 71.8673282841473"
    ## [1] "PC_FORMACAO_DOCENTE = 73.6978033138911"
    ## [1] "NU_TAXA_PERMANENCIA = 82.08119323293"

Irei selecionar apenas algumas colunas para nossa an�lise.

    enem <- select(enem,
                   -NU_PARTICIPANTES_NEC_ESP, -NU_MEDIA_OBJ, -NU_MEDIA_TOT,
                   -PC_FORMACAO_DOCENTE, -NU_TAXA_PERMANENCIA,
                   -CO_MUNICIPIO_ESCOLA, -CO_ESCOLA_EDUCACENSO, -NU_MATRICULAS, 
                   -NU_PARTICIPANTES, -NU_TAXA_PARTICIPACAO, -INSE, -NU_TAXA_APROVACAO,
                   -NU_TAXA_REPROVACAO, -NU_TAXA_ABANDONO, -PORTE_ESCOLA
                   )
    kable(
      head(enem)
      )

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 11%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: right;">NU_ANO</th>
<th style="text-align: right;">CO_UF_ESCOLA</th>
<th style="text-align: left;">SG_UF_ESCOLA</th>
<th style="text-align: left;">NO_MUNICIPIO_ESCOLA</th>
<th style="text-align: left;">NO_ESCOLA_EDUCACENSO</th>
<th style="text-align: right;">TP_DEPENDENCIA_ADM_ESCOLA</th>
<th style="text-align: right;">TP_LOCALIZACAO_ESCOLA</th>
<th style="text-align: right;">NU_MEDIA_CN</th>
<th style="text-align: right;">NU_MEDIA_CH</th>
<th style="text-align: right;">NU_MEDIA_LP</th>
<th style="text-align: right;">NU_MEDIA_MT</th>
<th style="text-align: right;">NU_MEDIA_RED</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: right;">2007</td>
<td style="text-align: right;">11</td>
<td style="text-align: left;">RO</td>
<td style="text-align: left;">Porto Velho</td>
<td style="text-align: left;">CENTRO DE ENSINO CLASSE A</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
</tr>
<tr class="even">
<td style="text-align: right;">2006</td>
<td style="text-align: right;">11</td>
<td style="text-align: left;">RO</td>
<td style="text-align: left;">Porto Velho</td>
<td style="text-align: left;">CENTRO DE ENSINO CLASSE A</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2005</td>
<td style="text-align: right;">11</td>
<td style="text-align: left;">RO</td>
<td style="text-align: left;">Porto Velho</td>
<td style="text-align: left;">CENTRO DE ENSINO CLASSE A</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
</tr>
<tr class="even">
<td style="text-align: right;">2008</td>
<td style="text-align: right;">11</td>
<td style="text-align: left;">RO</td>
<td style="text-align: left;">Porto Velho</td>
<td style="text-align: left;">CENTRO DE ENSINO CLASSE A</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">72.16</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2007</td>
<td style="text-align: right;">11</td>
<td style="text-align: left;">RO</td>
<td style="text-align: left;">Porto Velho</td>
<td style="text-align: left;">CENTRO EDUCACIONAL MOJUCA</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
</tr>
<tr class="even">
<td style="text-align: right;">2008</td>
<td style="text-align: right;">11</td>
<td style="text-align: left;">RO</td>
<td style="text-align: left;">Porto Velho</td>
<td style="text-align: left;">CENTRO EDUCACIONAL MOJUCA</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">59.81</td>
</tr>
</tbody>
</table>

-   **NU\_ANO**: Ano da edi��o do ENEM por Escola.
-   **SG\_UF\_ESCOLA**: Sigla da Unidade da Federa��o da escola.
-   **NO\_MUNICIPIO\_ESCOLA**: Nome do munic�pio da escola.
-   **NO\_ESCOLA\_EDUCACENSO**: Nome da Escola no Educacenso do ano
    anterior.
-   **TP\_DEPENDENCIA\_ADM\_ESCOLA**: Tipo da depend�ncia administrativa
    da entidade (Escola) do Educacenso.
    -   1 - Federal,
    -   2 - Estadual,
    -   3 - Municipal,
    -   4 - Privada.
-   **TP\_LOCALIZACAO\_ESCOLA**: Tipo de Localiza��o da escola.
    -   1 - Urbana,
    -   2 - Rural.
-   **NU\_MEDIA\_CN**: M�dia das notas de Ci�ncias da Natureza do Ensino
    M�dio Regular.
-   **NU\_MEDIA\_CH**: M�dia das notas de Ci�ncias Humanas do Ensino
    M�dio Regular.
-   **NU\_MEDIA\_LP**: M�dia das notas de Linguagens e C�digos do Ensino
    M�dio Regular.
-   **NU\_MEDIA\_MT**: M�dia das notas de Matem�tica do Ensino M�dio
    Regular.
-   **NU\_MEDIA\_RED**: M�dia das notas de Reda��o do Ensino M�dio
    Regular.

Como iremos fazer a an�lise apenas do ENEM 2015, irei filtrar a coluna
"NU\_ANO" para recuperar as observa��es, que correspondem a uma escola, referentes apenas ao desempenho no exame de 2015. Nosso novo
*dataframe* ser� chamado de `enem2015`.

    enem2015 <- filter(enem, NU_ANO == 2015)
    kable(
      head(enem2015)
      )

<table>
<colgroup>
<col style="width: 2%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 8%" />
<col style="width: 32%" />
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: right;">NU_ANO</th>
<th style="text-align: right;">CO_UF_ESCOLA</th>
<th style="text-align: left;">SG_UF_ESCOLA</th>
<th style="text-align: left;">NO_MUNICIPIO_ESCOLA</th>
<th style="text-align: left;">NO_ESCOLA_EDUCACENSO</th>
<th style="text-align: right;">TP_DEPENDENCIA_ADM_ESCOLA</th>
<th style="text-align: right;">TP_LOCALIZACAO_ESCOLA</th>
<th style="text-align: right;">NU_MEDIA_CN</th>
<th style="text-align: right;">NU_MEDIA_CH</th>
<th style="text-align: right;">NU_MEDIA_LP</th>
<th style="text-align: right;">NU_MEDIA_MT</th>
<th style="text-align: right;">NU_MEDIA_RED</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: right;">11</td>
<td style="text-align: left;">RO</td>
<td style="text-align: left;">Porto Velho</td>
<td style="text-align: left;">CENTRO DE ENSINO CLASSE A</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">591.64</td>
<td style="text-align: right;">652.34</td>
<td style="text-align: right;">604.53</td>
<td style="text-align: right;">627.66</td>
<td style="text-align: right;">732.00</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: right;">11</td>
<td style="text-align: left;">RO</td>
<td style="text-align: left;">Porto Velho</td>
<td style="text-align: left;">CENTRO EDUCACIONAL MOJUCA</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">458.46</td>
<td style="text-align: right;">533.51</td>
<td style="text-align: right;">472.62</td>
<td style="text-align: right;">459.72</td>
<td style="text-align: right;">507.82</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: right;">11</td>
<td style="text-align: left;">RO</td>
<td style="text-align: left;">Porto Velho</td>
<td style="text-align: left;">CENTRO EDUCACIONAL OBJETIVO</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">529.05</td>
<td style="text-align: right;">583.87</td>
<td style="text-align: right;">547.11</td>
<td style="text-align: right;">507.22</td>
<td style="text-align: right;">652.43</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: right;">11</td>
<td style="text-align: left;">RO</td>
<td style="text-align: left;">Porto Velho</td>
<td style="text-align: left;">COLEGIO DOM BOSCO</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">508.74</td>
<td style="text-align: right;">586.45</td>
<td style="text-align: right;">531.35</td>
<td style="text-align: right;">529.87</td>
<td style="text-align: right;">591.84</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: right;">11</td>
<td style="text-align: left;">RO</td>
<td style="text-align: left;">Porto Velho</td>
<td style="text-align: left;">CENTRO EDUCACIONAL OBJETIVO - UNIDADE JARDIM AMERICA</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">523.38</td>
<td style="text-align: right;">591.66</td>
<td style="text-align: right;">563.45</td>
<td style="text-align: right;">528.93</td>
<td style="text-align: right;">583.48</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: right;">11</td>
<td style="text-align: left;">RO</td>
<td style="text-align: left;">Porto Velho</td>
<td style="text-align: left;">COLEGIO TIRADENTES DA POLICIA MILITAR DO ESTADO DE RONDONIA EEEFM TIRADENTES</td>
<td style="text-align: right;">2</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">505.77</td>
<td style="text-align: right;">582.16</td>
<td style="text-align: right;">527.39</td>
<td style="text-align: right;">492.85</td>
<td style="text-align: right;">580.83</td>
</tr>
</tbody>
</table>

Qual o tamanho do nosso `dataset`? At� agora s� mostrei as primeiras linhas do conjunto de dados, mas n�o sabemos sua dimens�o real. Vamos ver.
    
    dim(enem2015)
    
    #> [1] 15598    12

H� 15.598 escolas no nosso conjunto de dados.   
Dados prontos! (Na verdade, ainda n�o: veremos que algumas colunas ainda dever�o ser manipuladas).

***

## 2. Brasil

Agora, vamos comparar desempenho do pa�s inteiro nessa edi��o do ENEM. Come�aremos com a m�dia da nota em Ci�ncias Humanas. 

### 2.1. Desempenho por estado: qual o melhor estado em Ci�ncias Humanas?

Como se d� as m�dias dos estados na prova de Ci�ncias
Humanas? Quais suas expectativas?

    kable(
      enem2015 %>% 
        group_by(SG_UF_ESCOLA) %>% 
        summarise(MED_HUM = mean(NU_MEDIA_CH, na.rm = TRUE)) %>% 
        arrange(desc(MED_HUM))
      )

<table>
<thead>
<tr class="header">
<th style="text-align: left;">SG_UF_ESCOLA</th>
<th style="text-align: right;">MED_HUM</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;">DF</td>
<td style="text-align: right;">581.7894</td>
</tr>
<tr class="even">
<td style="text-align: left;">SP</td>
<td style="text-align: right;">580.9434</td>
</tr>
<tr class="odd">
<td style="text-align: left;">RJ</td>
<td style="text-align: right;">578.9549</td>
</tr>
<tr class="even">
<td style="text-align: left;">PR</td>
<td style="text-align: right;">578.5023</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MG</td>
<td style="text-align: right;">575.3918</td>
</tr>
<tr class="even">
<td style="text-align: left;">RS</td>
<td style="text-align: right;">568.9864</td>
</tr>
<tr class="odd">
<td style="text-align: left;">BA</td>
<td style="text-align: right;">568.3144</td>
</tr>
<tr class="even">
<td style="text-align: left;">SC</td>
<td style="text-align: right;">565.6487</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ES</td>
<td style="text-align: right;">560.5446</td>
</tr>
<tr class="even">
<td style="text-align: left;">PA</td>
<td style="text-align: right;">559.9895</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MS</td>
<td style="text-align: right;">557.5041</td>
</tr>
<tr class="even">
<td style="text-align: left;">PE</td>
<td style="text-align: right;">556.3348</td>
</tr>
<tr class="odd">
<td style="text-align: left;">GO</td>
<td style="text-align: right;">555.9471</td>
</tr>
<tr class="even">
<td style="text-align: left;">SE</td>
<td style="text-align: right;">553.4684</td>
</tr>
<tr class="odd">
<td style="text-align: left;">RN</td>
<td style="text-align: right;">552.8039</td>
</tr>
<tr class="even">
<td style="text-align: left;">RO</td>
<td style="text-align: right;">550.2621</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PB</td>
<td style="text-align: right;">549.3331</td>
</tr>
<tr class="even">
<td style="text-align: left;">MT</td>
<td style="text-align: right;">548.2156</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PI</td>
<td style="text-align: right;">547.7074</td>
</tr>
<tr class="even">
<td style="text-align: left;">AM</td>
<td style="text-align: right;">547.6730</td>
</tr>
<tr class="odd">
<td style="text-align: left;">AL</td>
<td style="text-align: right;">547.5946</td>
</tr>
<tr class="even">
<td style="text-align: left;">RR</td>
<td style="text-align: right;">545.9308</td>
</tr>
<tr class="odd">
<td style="text-align: left;">AC</td>
<td style="text-align: right;">544.3018</td>
</tr>
<tr class="even">
<td style="text-align: left;">CE</td>
<td style="text-align: right;">543.5448</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MA</td>
<td style="text-align: right;">541.3614</td>
</tr>
<tr class="even">
<td style="text-align: left;">AP</td>
<td style="text-align: right;">535.7428</td>
</tr>
<tr class="odd">
<td style="text-align: left;">TO</td>
<td style="text-align: right;">535.5845</td>
</tr>
</tbody>
</table>

Atingiu o que voc� esperava? **Vemos um destaque do Distrito Federal, dos
estados do Sudeste e do Sul**. Essas notas s�o boas, afinal? S�o t�o
distantes?  
Para termos uma no��o, a nota de corte para o curso de Medicina na
Universidade de S�o Paulo [chegou aos 920
pontos](https://g1.globo.com/educacao/enem/2019/noticia/2020/01/22/nota-de-corte-para-medicina-no-1o-dia-do-sisu-vai-de-71797-a-92813-na-ampla-concorrencia.ghtml)
na �ltima edi��o, ENEM 2019 (deve-se considerar uma m�dia ponderada com
as outras provas e a reda��o). A m�dia nacional, portanto, � *muito*
distante de uma nota para Medicina em S�o Paulo.  
Inclusive, n�o seria poss�vel matricular-se em nenhum curso da
Universidade de S�o Paulo com uma nota abaixo de 700 pontos, que foi a
[menor nota de
corte](https://querobolsa.com.br/sisu/notas-de-corte/faculdades/universidade-de-sao-paulo)
dessa mesma edi��o, para o curso de Lazer e Turismo Noturno.  
Vamos continuar nossa an�lise!  

### 2.2 Desempenho por tipo administrativo: escolas privadas v�o melhor no ENEM?

Agora, veremos se o tipo administrativo da escola est� relacionado com o
desempenho dos alunos.  
Primeiramente, vejamos a quantidade de escolas por tipo administrativo.

    kable(
      enem2015 %>% 
        group_by(TP_DEPENDENCIA_ADM_ESCOLA) %>% 
        summarise(N_ESCOLAS = n())
      )

<table>
<thead>
<tr class="header">
<th style="text-align: right;">TP_DEPENDENCIA_ADM_ESCOLA</th>
<th style="text-align: right;">N_ESCOLAS</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: right;">1</td>
<td style="text-align: right;">328</td>
</tr>
<tr class="even">
<td style="text-align: right;">2</td>
<td style="text-align: right;">8836</td>
</tr>
<tr class="odd">
<td style="text-align: right;">3</td>
<td style="text-align: right;">109</td>
</tr>
<tr class="even">
<td style="text-align: right;">4</td>
<td style="text-align: right;">6325</td>
</tr>
</tbody>
</table>

Conforme o dicion�rio exposto mais acima, podemos converter os valores
num�ricos para os valores reais das vari�veis, para melhor entendimento.

    enem2015$TP_DEPENDENCIA_ADM_ESCOLA <- factor(enem2015$TP_DEPENDENCIA_ADM_ESCOLA) # transforma��o em factor, vetor com valores definidos
    levels(enem2015$TP_DEPENDENCIA_ADM_ESCOLA) <- c("Federal","Municipal","Estadual","Privada") # mudan�a dos "levels" desse fator, valores que pode assumir

    kable(
      enem2015 %>% 
      group_by(TP_DEPENDENCIA_ADM_ESCOLA) %>% 
      summarise(N_ESCOLAS = n()) %>% 
      arrange(N_ESCOLAS)
      )

<table>
<thead>
<tr class="header">
<th style="text-align: left;">TP_DEPENDENCIA_ADM_ESCOLA</th>
<th style="text-align: right;">N_ESCOLAS</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;">Estadual</td>
<td style="text-align: right;">109</td>
</tr>
<tr class="even">
<td style="text-align: left;">Federal</td>
<td style="text-align: right;">328</td>
</tr>
<tr class="odd">
<td style="text-align: left;">Privada</td>
<td style="text-align: right;">6325</td>
</tr>
<tr class="even">
<td style="text-align: left;">Municipal</td>
<td style="text-align: right;">8836</td>
</tr>
</tbody>
</table>

Pronto! Muito melhor para nossa interpreta��o.  
Vamos ver um gr�fico de como os tipos adminitrativos se sa�ram na prova
de Matem�tica. Fa�a suas apostas.

    enem2015 %>% 
      ggplot(aes(x = TP_DEPENDENCIA_ADM_ESCOLA, y = NU_MEDIA_MT,
                 fill = TP_DEPENDENCIA_ADM_ESCOLA)) +
      geom_boxplot(show.legend = FALSE) +
      labs(title = "Desempenho em Matem�tica (ENEM 2015) por Tipo Administrativo",
           x = "Tipo Administrativo", y = "M�dia da Escola") +
      theme_bw()

![](a_files/figure-markdown_strict/matem�tica%20por%20tipo%20administrativo-1.png)

**A melhor escola do pa�s � uma escola privada**, e a
pior � uma municipal. Nota-se uma distribui��o um pouco parecida entre
as escolas federais e privadas - com exce��o de privadas com excelente
desempenho. As federais s�o �timas escolas. At� certo tempo, havia um
processo seletivo baseado em uma prova - vestibulinho - para o ingresso
dos alunos. Por�m, foi substitu�da pela an�lise do hist�rico escolar dos
alunos.  
Parece que a *exist�ncia de um processo seletivo aumenta o desempenho dos
alunos*. Pois, apesar de serem escolas p�blicas, as federais apresentam
um melhor desempenho. Veremos essa ideia se concretizando um pouco mais
adiante.

***

## 3. Sudeste

Partiremos para a an�lise da regi�o Sudeste, que obteve boas m�dias em
Ci�ncias Humanas.  
Irei criar uma nova vari�vel, `enem2015_sud`, referente �s escolas do
sudeste (pertencentes ao Esp�rito Santo, Minas Gerais, Rio de Janeiro ou
S�o Paulo).  

### 3.1 Desempenho no sudeste: SP � o melhor estado no ENEM?

Como � a distribui��o de cada estado em reda��o?

    enem2015_sud <- filter(enem2015, SG_UF_ESCOLA%in%c("ES", "MG", "RJ", "SP"))
    enem2015_sud %>% 
      ggplot(aes(x = SG_UF_ESCOLA,y = NU_MEDIA_RED, fill = SG_UF_ESCOLA)) +
      geom_boxplot(show.legend = FALSE) +
      labs(title = "Desempenho em Reda��o das Escolas do Sudeste, por Estado",
           x = "Estado", y = "M�dia da Escola em Reda��o") +
      theme_bw()

![](a_files/figure-markdown_strict/filtro%20sudeste-1.png)

O Esp�rito Santo apresenta um desempenho um pouco abaixo dos demais
estados. **No sudeste, a melhor escola em reda��o foi do Rio de Janeiro**. 

### 3.2 Desempenho no sudeste por tipo adminstrativo: como s�o as federais?

Vamos ver como se d� a rela��o com os tipos administrativos em cada
estado.

    enem2015_sud %>% 
      group_by(SG_UF_ESCOLA, TP_DEPENDENCIA_ADM_ESCOLA) %>% 
      summarise(MED_RED = mean(NU_MEDIA_RED, na.rm = TRUE)) %>% 
      ggplot(aes(x = SG_UF_ESCOLA, y = MED_RED, fill = TP_DEPENDENCIA_ADM_ESCOLA)) +
      geom_col(position = "dodge") +
      labs(title = "M�dia em Reda��o por Estados do Sudeste e Tipo Administrativo",
           x = "Estado", y = "M�dia em Reda��o do ENEM", fill = "Tipo Administrativo") +
      theme_bw()

![](a_files/figure-markdown_strict/sudeste%20e%20tipo%20administrativo-1.png)

Novamente, **as federais se destacam em rela��o �s outras p�blicas**, e
acabam superando as privadas no Esp�rito Santo e no Rio de Janeiro.  
Em Minas Gerais, a diferen�a entre as privadas com as municipais e
estaduais � mais evidente que nos outros estados. Por�m, n�o devido ao
mau-desempenho, mas sim, ao bom desempenho das privadas, que s�o as
melhores da regi�o. As federais de S�o Paulo s�o as piores.  
N�o h� estaduais no Esp�rito Santo! N�o achei nada a respeito no [site
da rede estadual de ensino do
ES](https://sedu.es.gov.br/rede-estadual-de-ensino), mas achei um fato
interessante de ser quetionado o porqu�.

H� dados faltantes?

    enem2015_ES <- enem2015 %>% 
      filter(SG_UF_ESCOLA == "ES") %>% 
      group_by(NU_MEDIA_RED)

    for (i in 1:length(enem2015_ES)){
      prop_na = (sum(is.na(enem2015_ES[i]))/length(enem2015_ES[[i]])) * 100
      print(str_c(names(enem2015_ES)[i], " = ", (prop_na)))
    }

    ## [1] "NU_ANO = 0"
    ## [1] "CO_UF_ESCOLA = 0"
    ## [1] "SG_UF_ESCOLA = 0"
    ## [1] "NO_MUNICIPIO_ESCOLA = 0"
    ## [1] "NO_ESCOLA_EDUCACENSO = 0"
    ## [1] "TP_DEPENDENCIA_ADM_ESCOLA = 0"
    ## [1] "TP_LOCALIZACAO_ESCOLA = 0"
    ## [1] "NU_MEDIA_CN = 0"
    ## [1] "NU_MEDIA_CH = 0"
    ## [1] "NU_MEDIA_LP = 0"
    ## [1] "NU_MEDIA_MT = 0"
    ## [1] "NU_MEDIA_RED = 0"

Bem, n�o encontrei nenhuma raz�o para isso, mas � um bom
questionamento.  
Partiremos para S�o Paulo.

***

## 4. S�o Paulo

Irei criar uma nova vari�vel, `enem2015_SP` que cont�m as escolas de S�o
Paulo.  

### 4.1. Desempenho pela localiza��o: escolas urbanas e rurais

Vamos ver a distribui��o pela localidade da escola (urbana ou rural)

    enem2015_SP <- filter(enem2015, SG_UF_ESCOLA == "SP")

    enem2015_SP %>% 
      group_by(TP_LOCALIZACAO_ESCOLA) %>% 
      summarise(N_ESCOLAS = n())

    ## Warning: `...` is not empty.
    ## 
    ## We detected these problematic arguments:
    ## * `needs_dots`
    ## 
    ## These dots only exist to allow future extensions and should be empty.
    ## Did you misspecify an argument?

    ## # A tibble: 2 x 2
    ##   TP_LOCALIZACAO_ESCOLA N_ESCOLAS
    ##                   <int>     <int>
    ## 1                     1      3291
    ## 2                     2        59

Assim como no tipo administrativo, devemos converter esses valores
apresentados.  
Vejamos o desempenho de cada tipo de localiza��o da prova de Ci�ncias da
Natureza.

    enem2015_SP$TP_LOCALIZACAO_ESCOLA <- factor(enem2015_SP$TP_LOCALIZACAO_ESCOLA)
    levels(enem2015_SP$TP_LOCALIZACAO_ESCOLA) <- c("Urbana", "Rural")

    enem2015_SP %>% 
      group_by(TP_LOCALIZACAO_ESCOLA) %>% 
      summarise(MED_NAT = mean(NU_MEDIA_CN, na.rm = TRUE)) %>% 
      ggplot(aes(x = TP_LOCALIZACAO_ESCOLA, y = MED_NAT, fill = TP_LOCALIZACAO_ESCOLA)) + 
      geom_col(show.legend = FALSE) +
      labs(title = "M�dia das escolas de S�o Paulo em Ci�ncias da Natureza por localiza��o",
           x = "Localiza��o", y  = "M�dia em Ci�ncias da Natureza (Biologia, Qu�mica e F�sica)") +
      theme_bw()

![](a_files/figure-markdown_strict/por%20localiza��o-1.png)

**O desempenho m�dio das urbanas supera - um pouco - as das escolas
rurais.**  

### 4.2 S�o Paulo capital: a geografia na nota

Vejamos agora o desempenho em reda��o em S�o Paulo. Qual a m�dia no
estado?  
*O tema desse ano foi: "A PERSIST�NCIA DA VIOL�NCIA CONTRA A MULHER NA
SOCIEDADE BRASILEIRA".*

    print(summary(enem2015_SP$NU_MEDIA_RED, na.rm = TRUE))

    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##   400.5   524.0   566.2   577.7   624.0   835.7

Irei filtrar as melhores escolas em S�o Paulo na reda��o para
analisarmos.

    SP_melhores <- enem2015_SP %>% 
      filter(NU_MEDIA_RED > 750) # considerei as escolas cujas m�dias de seus alunos superou 750 pontos
    kable(
      head(arrange(SP_melhores, desc(NU_MEDIA_RED)))
    )

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 9%" />
<col style="width: 27%" />
<col style="width: 11%" />
<col style="width: 9%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: right;">NU_ANO</th>
<th style="text-align: right;">CO_UF_ESCOLA</th>
<th style="text-align: left;">SG_UF_ESCOLA</th>
<th style="text-align: left;">NO_MUNICIPIO_ESCOLA</th>
<th style="text-align: left;">NO_ESCOLA_EDUCACENSO</th>
<th style="text-align: left;">TP_DEPENDENCIA_ADM_ESCOLA</th>
<th style="text-align: left;">TP_LOCALIZACAO_ESCOLA</th>
<th style="text-align: right;">NU_MEDIA_CN</th>
<th style="text-align: right;">NU_MEDIA_CH</th>
<th style="text-align: right;">NU_MEDIA_LP</th>
<th style="text-align: right;">NU_MEDIA_MT</th>
<th style="text-align: right;">NU_MEDIA_RED</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: right;">35</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">Ribeir�o Preto</td>
<td style="text-align: left;">SEB COC UNIDADE ALVARES CABRAL</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">676.02</td>
<td style="text-align: right;">683.77</td>
<td style="text-align: right;">632.48</td>
<td style="text-align: right;">719.44</td>
<td style="text-align: right;">835.71</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: right;">35</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">S�o Paulo</td>
<td style="text-align: left;">VITAL BRAZIL COLEGIO</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">631.11</td>
<td style="text-align: right;">664.92</td>
<td style="text-align: right;">605.77</td>
<td style="text-align: right;">714.21</td>
<td style="text-align: right;">830.78</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: right;">35</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">S�o Paulo</td>
<td style="text-align: left;">PENTAGONO COLEGIO UNIDADE CAIUBI</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">616.42</td>
<td style="text-align: right;">667.68</td>
<td style="text-align: right;">619.12</td>
<td style="text-align: right;">693.54</td>
<td style="text-align: right;">823.33</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: right;">35</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">S�o Carlos</td>
<td style="text-align: left;">SAO CARLOS INSTITUTO EDUCACAO DE ENSINO FUNDAMENTAL E MEDIO</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">648.93</td>
<td style="text-align: right;">688.47</td>
<td style="text-align: right;">635.75</td>
<td style="text-align: right;">709.35</td>
<td style="text-align: right;">821.94</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: right;">35</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">S�o Paulo</td>
<td style="text-align: left;">LICEU DE ARTES E OFICIOS DE SAO PAULO ESCOLA TECNICA</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">650.56</td>
<td style="text-align: right;">691.59</td>
<td style="text-align: right;">632.86</td>
<td style="text-align: right;">782.11</td>
<td style="text-align: right;">814.26</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: right;">35</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">S�o Paulo</td>
<td style="text-align: left;">OBJETIVO COLEGIO INTEGRADO</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">728.80</td>
<td style="text-align: right;">721.47</td>
<td style="text-align: right;">681.23</td>
<td style="text-align: right;">873.65</td>
<td style="text-align: right;">813.17</td>
</tr>
</tbody>
</table>

Vemos que **a melhor escola de S�o Paulo em reda��o � de Ribeir�o Preto**,
que teve �timos rendimentos nas outras provas tamb�m.  
Mais abaixo, vemos a escola *Liceu de Artes e Of�cios de S�o Paulo
Escola T�cnica*, em quinto lugar, onde eu estudei :D  
Eu n�o estudava l� ainda em 2015. Acho que se eu tivesse a escola n�o
estaria em quinto lugar :p  
Vemos muitas escolas do interior. Quantas s�o nas melhores?

    SP_melhores %>% 
      mutate(CAPITAL = ifelse(NO_MUNICIPIO_ESCOLA == "S�o Paulo",
                              "Capital", "Interior")) %>% 
      ggplot(aes(x = CAPITAL, fill = CAPITAL)) +
      geom_bar(show.legend = FALSE) +
      labs(title = "Quantidade de escolas dentre as melhores de SP",
           x = "Localiza��o", y = "Quantidade") +
      theme_bw()

![](a_files/figure-markdown_strict/capital-1.png)

H� mais escolas do interior dentre as melhores. Mas isso � esperado?
Como � a distribui��o para todas as escolas de S�o Paulo? Vejamos.

    enem2015_SP %>% 
      mutate(CAPITAL = ifelse(NO_MUNICIPIO_ESCOLA == "S�o Paulo",
                              "Capital", "Interior")) %>% 
      ggplot(aes(x = CAPITAL, fill = CAPITAL)) +
      geom_bar(show.legend = FALSE) +
      labs(title = "Quantidade de escolas em SP",
           x = "Localiza��o", y = "Quantidade") +
      theme_bw()

![](a_files/figure-markdown_strict/quantas%20no%20total%20s�o%20da%20capital-1.png)

Vemos que dentre todas as escolas de S�o Paulo, a propor��o de escolas
na capital diminui. O que evidencia que **as escolas da capital tem melhor
desempenho em reda��o.**

### 4.3 Sobre as p�blicas

Vejamos as melhores p�blicas, que n�o apareceram dentre as 5 melhores de
S�o Paulo.

    SP_publicas <- enem2015_SP %>% 
      filter(TP_DEPENDENCIA_ADM_ESCOLA != "Privada")
    kable(
      head(arrange(SP_publicas, desc(NU_MEDIA_MT)))
    )

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 9%" />
<col style="width: 23%" />
<col style="width: 12%" />
<col style="width: 10%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: right;">NU_ANO</th>
<th style="text-align: right;">CO_UF_ESCOLA</th>
<th style="text-align: left;">SG_UF_ESCOLA</th>
<th style="text-align: left;">NO_MUNICIPIO_ESCOLA</th>
<th style="text-align: left;">NO_ESCOLA_EDUCACENSO</th>
<th style="text-align: left;">TP_DEPENDENCIA_ADM_ESCOLA</th>
<th style="text-align: left;">TP_LOCALIZACAO_ESCOLA</th>
<th style="text-align: right;">NU_MEDIA_CN</th>
<th style="text-align: right;">NU_MEDIA_CH</th>
<th style="text-align: right;">NU_MEDIA_LP</th>
<th style="text-align: right;">NU_MEDIA_MT</th>
<th style="text-align: right;">NU_MEDIA_RED</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: right;">35</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">Campinas</td>
<td style="text-align: left;">CAMPINAS COLEGIO TECNICO DE - UNICAMP</td>
<td style="text-align: left;">Municipal</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">604.06</td>
<td style="text-align: right;">647.37</td>
<td style="text-align: right;">600.03</td>
<td style="text-align: right;">708.29</td>
<td style="text-align: right;">653.47</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: right;">35</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">Bauru</td>
<td style="text-align: left;">COL TEC INDUSTRIAL PROF ISAAC PORTAL ROLDAN UNESP</td>
<td style="text-align: left;">Municipal</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">618.94</td>
<td style="text-align: right;">665.28</td>
<td style="text-align: right;">614.48</td>
<td style="text-align: right;">702.57</td>
<td style="text-align: right;">683.25</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: right;">35</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">S�o Paulo</td>
<td style="text-align: left;">IFSP - CAMPUS SAO PAULO</td>
<td style="text-align: left;">Federal</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">605.28</td>
<td style="text-align: right;">662.32</td>
<td style="text-align: right;">610.49</td>
<td style="text-align: right;">702.40</td>
<td style="text-align: right;">647.54</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: right;">35</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">Guaratinguet�</td>
<td style="text-align: left;">CARLOS AUGUSTO PATRICIO AMORIM PROF CTIG UNESP</td>
<td style="text-align: left;">Municipal</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">591.39</td>
<td style="text-align: right;">639.62</td>
<td style="text-align: right;">596.07</td>
<td style="text-align: right;">702.13</td>
<td style="text-align: right;">675.10</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: right;">35</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">S�o Paulo</td>
<td style="text-align: left;">SAO PAULO ETEC DE</td>
<td style="text-align: left;">Municipal</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">617.86</td>
<td style="text-align: right;">677.17</td>
<td style="text-align: right;">623.83</td>
<td style="text-align: right;">691.92</td>
<td style="text-align: right;">707.27</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: right;">35</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">Limeira</td>
<td style="text-align: left;">LIMEIRA COLEGIO TECNICO DE UNICAMP</td>
<td style="text-align: left;">Municipal</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">573.85</td>
<td style="text-align: right;">637.98</td>
<td style="text-align: right;">590.29</td>
<td style="text-align: right;">669.67</td>
<td style="text-align: right;">661.99</td>
</tr>
</tbody>
</table>

Vemos o destaque daquelas do interior tamb�m. Por�m, h� algo comum a
**todas** elas: s�o col�gios t�cnicos ou federais. 

### 4.4. Sobre as escolas t�cnicas

Vamos analisar os col�gios t�cnicos - em S�o Paulo, h� escolas t�cnicas
estaduais, ou [ETEC's](https://www.cps.sp.gov.br/category/etec/).  
Adicionei uma coluna ao nosso *dataframe*, chamada de "Tecnica", que
indica se o nome da escola cont�m "TEC": vimos que algumas cont�m "ETEC"
enquanto outras "Col�gio T�cnico" ou "Escola T�cnica"

    SP_tecnicas <- SP_publicas %>% 
      mutate(Tecnica = ifelse(str_detect(NO_ESCOLA_EDUCACENSO, "TEC"), # ETEC ou TECNINO/TECNICA
                              "Escola T�cnica", "Escola N�o-t�cnica"))
    kable(
      head(SP_tecnicas %>% 
        select(NO_ESCOLA_EDUCACENSO, Tecnica) %>% 
        arrange(desc(Tecnica)))
    )

<table>
<thead>
<tr class="header">
<th style="text-align: left;">NO_ESCOLA_EDUCACENSO</th>
<th style="text-align: left;">Tecnica</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;">ALBERT EINSTEIN ETEC</td>
<td style="text-align: left;">Escola T�cnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">HORACIO AUGUSTO DA SILVEIRA PROF ETEC</td>
<td style="text-align: left;">Escola T�cnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CARLOS DE CAMPOS ETEC</td>
<td style="text-align: left;">Escola T�cnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CAMARGO ARANHA PROF ETEC</td>
<td style="text-align: left;">Escola T�cnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE ROCHA MENDES ETEC</td>
<td style="text-align: left;">Escola T�cnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARTIN LUTHER KING ETEC</td>
<td style="text-align: left;">Escola T�cnica</td>
</tr>
</tbody>
</table>

Vejamos a propor��o das escolas t�cnicas no estado.

    SP_tecnicas %>% 
      ggplot(aes(x = Tecnica, fill = Tecnica)) +
      geom_bar(show.legend = FALSE) +
      labs(title = "Tipo de escola p�blica em SP",
           x = NULL, y = "Quantidade") +
      theme_bw()

![](a_files/figure-markdown_strict/grafico%20tecnicas,%20propor��o-1.png)

Vemos que a exorbitante maioria � composta por col�gios n�o t�cnicos.
Por�m, dentro das melhores escolas de S�o Paulo, vemos que a
distribui��o � extremamente diferente. Considerei as melhoes escolas com
aquelas com desempenho em Matem�tica acima dos 600 pontos.

    SP_tecnicas %>% 
      filter(NU_MEDIA_MT > 600) %>% 
      ggplot(aes(x = Tecnica, fill = Tecnica)) +
      geom_bar(show.legend = FALSE) +
      labs(title = "Tipo de escola dentre as melhores p�blicas em SP",
           x = NULL, y = "Quantidade") +
      theme_bw()

![](a_files/figure-markdown_strict/Se%20tecnicas%20s�o%20melhores-1.png)

O que esses gr�ficos dizem pra voc�? O fato � que as escolas t�cnicas
foram melhores, em m�dia, que as escolas p�blicas n�o t�cnicas. Por
qu�?  
Assim como institutos federais, as escolas t�cnicas demandam um processo
seletivo para o ingresso do estudante em seu ambiente acad�mico. Dessa
forma, acaba inserindo-o em um meio intelectualmente mais rico, fazendo
com que - j� tendo passado por experci�ncias de sele��o - suas notas em
matem�tica tenham sido melhores do que aqueles que n�o fizeram um
col�gio t�cnico.  
Apesar das dificuldades e demandas de um ensino t�cnico integrado ao
ensino m�dio, os alunos de ETEC's se destacam.

***

## 5. Conclus�o

A educa��o no Brasil, de fato, n�o � democr�tica. Vimos que os estados
possuem desempenhos bem diferentes na maior prova do pa�s. Ademais, o
tipo administrativo tamb�m influencia no desempenho dos alunos.  

Por�m, o que acaba mais influenciando na nota de um aluno � o ambiente
em que est� inserido e o esfor�o do mesmo, visto que, col�gios p�blicos
que cont�m processos seletivos, e dessa forma, aumentam o n�vel
acad�mico que o aluno � exposto, possuem melhores rendimentos que
col�gios p�blicos convencionais, evidenciando como muitas vezes, n�o
depende apenas do estudante.  

Ademais, existem escolas p�blicas que foram melhores que particulares,
que, muitas vezes, possuem melhores infraestruturas.  

Espero que nossa an�lise te fa�a pensar um pouco sobre nosso sistema
educacional, e como ele impacta o futuro do nosso pa�s.  

Obrigado pela leitura!   
*Kenzo.*
