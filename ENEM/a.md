**Análise de Dados: Enem por escola**
=====================================

Introdução, link:
<a href="https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem-por-escola" class="uri">https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem-por-escola</a>

    library(tidyverse)
    library(knitr)

descrição do conjunto de dados

    enem <- read.csv("MICRODADOS_ENEM_ESCOLA.csv", sep=';')
    kable(head(enem))

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

    for (i in 1:length(enem)){
      prop_na = (sum(is.na(enem[i]))/length(enem[[i]])) * 100 # calculo da proporção
      if (prop_na > 70) { # vamos printar apenas aqueles em que a proporção supera os 70%
      print(str_c(names(enem)[i], " = ", (prop_na)))
    }
    }

    ## [1] "NU_PARTICIPANTES_NEC_ESP = 73.6774904965033"
    ## [1] "NU_MEDIA_OBJ = 88.8894692551"
    ## [1] "NU_MEDIA_TOT = 71.8673282841473"
    ## [1] "PC_FORMACAO_DOCENTE = 73.6978033138911"
    ## [1] "NU_TAXA_PERMANENCIA = 82.08119323293"

Assim, excluiremos certas colunas

    enem <- select(enem,
                   -CO_UF_ESCOLA, -CO_MUNICIPIO_ESCOLA, -CO_ESCOLA_EDUCACENSO,
                   -NU_PARTICIPANTES_NEC_ESP, -NU_MEDIA_OBJ, -NU_MEDIA_TOT,
                   -PC_FORMACAO_DOCENTE, -NU_TAXA_PERMANENCIA)
    kable(head(enem))

<table style="width:100%;">
<colgroup>
<col style="width: 2%" />
<col style="width: 4%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 4%" />
<col style="width: 1%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: right;">NU_ANO</th>
<th style="text-align: left;">SG_UF_ESCOLA</th>
<th style="text-align: left;">NO_MUNICIPIO_ESCOLA</th>
<th style="text-align: left;">NO_ESCOLA_EDUCACENSO</th>
<th style="text-align: right;">TP_DEPENDENCIA_ADM_ESCOLA</th>
<th style="text-align: right;">TP_LOCALIZACAO_ESCOLA</th>
<th style="text-align: right;">NU_MATRICULAS</th>
<th style="text-align: right;">NU_PARTICIPANTES</th>
<th style="text-align: right;">NU_TAXA_PARTICIPACAO</th>
<th style="text-align: right;">NU_MEDIA_CN</th>
<th style="text-align: right;">NU_MEDIA_CH</th>
<th style="text-align: right;">NU_MEDIA_LP</th>
<th style="text-align: right;">NU_MEDIA_MT</th>
<th style="text-align: right;">NU_MEDIA_RED</th>
<th style="text-align: left;">INSE</th>
<th style="text-align: right;">NU_TAXA_APROVACAO</th>
<th style="text-align: right;">NU_TAXA_REPROVACAO</th>
<th style="text-align: right;">NU_TAXA_ABANDONO</th>
<th style="text-align: left;">PORTE_ESCOLA</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: right;">2007</td>
<td style="text-align: left;">RO</td>
<td style="text-align: left;">Porto Velho</td>
<td style="text-align: left;">CENTRO DE ENSINO CLASSE A</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">144</td>
<td style="text-align: right;">140</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: left;"></td>
<td style="text-align: right;">91.9</td>
<td style="text-align: right;">8.1</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">Maior que 90 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2006</td>
<td style="text-align: left;">RO</td>
<td style="text-align: left;">Porto Velho</td>
<td style="text-align: left;">CENTRO DE ENSINO CLASSE A</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">184</td>
<td style="text-align: right;">139</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: left;"></td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: left;">Maior que 90 alunos</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2005</td>
<td style="text-align: left;">RO</td>
<td style="text-align: left;">Porto Velho</td>
<td style="text-align: left;">CENTRO DE ENSINO CLASSE A</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">220</td>
<td style="text-align: right;">145</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: left;"></td>
<td style="text-align: right;">86.5</td>
<td style="text-align: right;">12.4</td>
<td style="text-align: right;">1.1</td>
<td style="text-align: left;">Maior que 90 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2008</td>
<td style="text-align: left;">RO</td>
<td style="text-align: left;">Porto Velho</td>
<td style="text-align: left;">CENTRO DE ENSINO CLASSE A</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">186</td>
<td style="text-align: right;">171</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">72.16</td>
<td style="text-align: left;"></td>
<td style="text-align: right;">90.3</td>
<td style="text-align: right;">9.7</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">Maior que 90 alunos</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2007</td>
<td style="text-align: left;">RO</td>
<td style="text-align: left;">Porto Velho</td>
<td style="text-align: left;">CENTRO EDUCACIONAL MOJUCA</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">19</td>
<td style="text-align: right;">12</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: left;"></td>
<td style="text-align: right;">74.2</td>
<td style="text-align: right;">21.0</td>
<td style="text-align: right;">4.8</td>
<td style="text-align: left;">De 1 a 30 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2008</td>
<td style="text-align: left;">RO</td>
<td style="text-align: left;">Porto Velho</td>
<td style="text-align: left;">CENTRO EDUCACIONAL MOJUCA</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">33</td>
<td style="text-align: right;">13</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">NA</td>
<td style="text-align: right;">59.81</td>
<td style="text-align: left;"></td>
<td style="text-align: right;">79.1</td>
<td style="text-align: right;">17.9</td>
<td style="text-align: right;">3.0</td>
<td style="text-align: left;">De 31 a 60 alunos</td>
</tr>
</tbody>
</table>

**ENEM 2015**
-------------

Desejo fazer a análise apenas de 2015

    enem2015 <- filter(enem, NU_ANO == 2015)
    kable(head(enem2015))

<table>
<colgroup>
<col style="width: 1%" />
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 21%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 3%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 2%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: right;">NU_ANO</th>
<th style="text-align: left;">SG_UF_ESCOLA</th>
<th style="text-align: left;">NO_MUNICIPIO_ESCOLA</th>
<th style="text-align: left;">NO_ESCOLA_EDUCACENSO</th>
<th style="text-align: right;">TP_DEPENDENCIA_ADM_ESCOLA</th>
<th style="text-align: right;">TP_LOCALIZACAO_ESCOLA</th>
<th style="text-align: right;">NU_MATRICULAS</th>
<th style="text-align: right;">NU_PARTICIPANTES</th>
<th style="text-align: right;">NU_TAXA_PARTICIPACAO</th>
<th style="text-align: right;">NU_MEDIA_CN</th>
<th style="text-align: right;">NU_MEDIA_CH</th>
<th style="text-align: right;">NU_MEDIA_LP</th>
<th style="text-align: right;">NU_MEDIA_MT</th>
<th style="text-align: right;">NU_MEDIA_RED</th>
<th style="text-align: left;">INSE</th>
<th style="text-align: right;">NU_TAXA_APROVACAO</th>
<th style="text-align: right;">NU_TAXA_REPROVACAO</th>
<th style="text-align: right;">NU_TAXA_ABANDONO</th>
<th style="text-align: left;">PORTE_ESCOLA</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">RO</td>
<td style="text-align: left;">Porto Velho</td>
<td style="text-align: left;">CENTRO DE ENSINO CLASSE A</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">137</td>
<td style="text-align: right;">130</td>
<td style="text-align: right;">94.89</td>
<td style="text-align: right;">591.64</td>
<td style="text-align: right;">652.34</td>
<td style="text-align: right;">604.53</td>
<td style="text-align: right;">627.66</td>
<td style="text-align: right;">732.00</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">96.1</td>
<td style="text-align: right;">3.9</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">Maior que 90 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">RO</td>
<td style="text-align: left;">Porto Velho</td>
<td style="text-align: left;">CENTRO EDUCACIONAL MOJUCA</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">20</td>
<td style="text-align: right;">17</td>
<td style="text-align: right;">85.00</td>
<td style="text-align: right;">458.46</td>
<td style="text-align: right;">533.51</td>
<td style="text-align: right;">472.62</td>
<td style="text-align: right;">459.72</td>
<td style="text-align: right;">507.82</td>
<td style="text-align: left;">Grupo 4</td>
<td style="text-align: right;">94.6</td>
<td style="text-align: right;">5.4</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">De 1 a 30 alunos</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">RO</td>
<td style="text-align: left;">Porto Velho</td>
<td style="text-align: left;">CENTRO EDUCACIONAL OBJETIVO</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">39</td>
<td style="text-align: right;">37</td>
<td style="text-align: right;">94.87</td>
<td style="text-align: right;">529.05</td>
<td style="text-align: right;">583.87</td>
<td style="text-align: right;">547.11</td>
<td style="text-align: right;">507.22</td>
<td style="text-align: right;">652.43</td>
<td style="text-align: left;">Grupo 5</td>
<td style="text-align: right;">90.1</td>
<td style="text-align: right;">9.9</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">De 31 a 60 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">RO</td>
<td style="text-align: left;">Porto Velho</td>
<td style="text-align: left;">COLEGIO DOM BOSCO</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">55</td>
<td style="text-align: right;">49</td>
<td style="text-align: right;">89.09</td>
<td style="text-align: right;">508.74</td>
<td style="text-align: right;">586.45</td>
<td style="text-align: right;">531.35</td>
<td style="text-align: right;">529.87</td>
<td style="text-align: right;">591.84</td>
<td style="text-align: left;">Grupo 5</td>
<td style="text-align: right;">88.7</td>
<td style="text-align: right;">10.5</td>
<td style="text-align: right;">0.8</td>
<td style="text-align: left;">De 31 a 60 alunos</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">RO</td>
<td style="text-align: left;">Porto Velho</td>
<td style="text-align: left;">CENTRO EDUCACIONAL OBJETIVO - UNIDADE JARDIM AMERICA</td>
<td style="text-align: right;">4</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">26</td>
<td style="text-align: right;">23</td>
<td style="text-align: right;">88.46</td>
<td style="text-align: right;">523.38</td>
<td style="text-align: right;">591.66</td>
<td style="text-align: right;">563.45</td>
<td style="text-align: right;">528.93</td>
<td style="text-align: right;">583.48</td>
<td style="text-align: left;">Grupo 5</td>
<td style="text-align: right;">84.5</td>
<td style="text-align: right;">13.1</td>
<td style="text-align: right;">2.4</td>
<td style="text-align: left;">De 1 a 30 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">RO</td>
<td style="text-align: left;">Porto Velho</td>
<td style="text-align: left;">COLEGIO TIRADENTES DA POLICIA MILITAR DO ESTADO DE RONDONIA EEEFM TIRADENTES</td>
<td style="text-align: right;">2</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">97</td>
<td style="text-align: right;">96</td>
<td style="text-align: right;">98.97</td>
<td style="text-align: right;">505.77</td>
<td style="text-align: right;">582.16</td>
<td style="text-align: right;">527.39</td>
<td style="text-align: right;">492.85</td>
<td style="text-align: right;">580.83</td>
<td style="text-align: left;">Grupo 5</td>
<td style="text-align: right;">89.2</td>
<td style="text-align: right;">10.8</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">Maior que 90 alunos</td>
</tr>
</tbody>
</table>

Média nacional em Humanas por estado

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

### Tipo Adminitrativo

    kable(enem2015 %>% 
      group_by(TP_DEPENDENCIA_ADM_ESCOLA) %>% 
      summarise(N_ESCOLAS = n()))

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

conversão

    enem2015$TP_DEPENDENCIA_ADM_ESCOLA <- factor(enem2015$TP_DEPENDENCIA_ADM_ESCOLA)
    levels(enem2015$TP_DEPENDENCIA_ADM_ESCOLA) <- c("Federal","Municipal","Estadual","Privada")

    kable(enem2015 %>% 
      group_by(TP_DEPENDENCIA_ADM_ESCOLA) %>% 
      summarise(N_ESCOLAS = n()) %>% 
      arrange(N_ESCOLAS))

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

![](a_files/figure-markdown_strict/matemática%202015%20por%20tipo%20administrativo-1.png)

Conclusão sobre esse gráfico

### Sudeste

    enem2015_sud <- filter(enem2015, SG_UF_ESCOLA%in%c("ES", "MG", "RJ", "SP"))
    enem2015_sud %>% 
      ggplot(aes(x = SG_UF_ESCOLA,y = NU_MEDIA_RED, fill = SG_UF_ESCOLA)) +
      geom_boxplot(show.legend = FALSE) +
      labs(title = "Desempenho em Redação das Escolas do Sudeste, por Estado",
           x = "Estado", y = "Média da Escola em Redação") +
      theme_bw()

![](a_files/figure-markdown_strict/filtro%20sudeste-1.png)

CONCLUSÃO

    enem2015_sud %>% 
      group_by(SG_UF_ESCOLA, TP_DEPENDENCIA_ADM_ESCOLA) %>% 
      summarise(MED_RED = mean(NU_MEDIA_RED, na.rm = TRUE)) %>% 
      ggplot(aes(x = SG_UF_ESCOLA, y = MED_RED, fill = TP_DEPENDENCIA_ADM_ESCOLA)) +
      geom_col(position = "dodge") +
      labs(title = "Média em Redação por Estados do Sudeste e Tipo Administrativo",
           x = "Estado", y = "Média em Redação do ENEM", fill = "Tipo Administrativo") +
      theme_bw()

    ## `summarise()` regrouping output by 'SG_UF_ESCOLA' (override with `.groups` argument)

![](a_files/figure-markdown_strict/sudeste%20e%20tipo%20administrativo-1.png)

Conclusão não há estaduais no espirito santo!

    enem2015_ES <- enem2015 %>% 
      filter(SG_UF_ESCOLA == "ES") %>% 
      group_by(NU_MEDIA_RED)

    for (i in 1:length(enem2015_ES)){
      prop_na = (sum(is.na(enem2015_ES[i]))/length(enem2015_ES[[i]])) * 100
      print(str_c(names(enem2015_ES)[i], " = ", (prop_na)))
    }

    ## [1] "NU_ANO = 0"
    ## [1] "SG_UF_ESCOLA = 0"
    ## [1] "NO_MUNICIPIO_ESCOLA = 0"
    ## [1] "NO_ESCOLA_EDUCACENSO = 0"
    ## [1] "TP_DEPENDENCIA_ADM_ESCOLA = 0"
    ## [1] "TP_LOCALIZACAO_ESCOLA = 0"
    ## [1] "NU_MATRICULAS = 0"
    ## [1] "NU_PARTICIPANTES = 0"
    ## [1] "NU_TAXA_PARTICIPACAO = 0"
    ## [1] "NU_MEDIA_CN = 0"
    ## [1] "NU_MEDIA_CH = 0"
    ## [1] "NU_MEDIA_LP = 0"
    ## [1] "NU_MEDIA_MT = 0"
    ## [1] "NU_MEDIA_RED = 0"
    ## [1] "INSE = 0"
    ## [1] "NU_TAXA_APROVACAO = 0"
    ## [1] "NU_TAXA_REPROVACAO = 0"
    ## [1] "NU_TAXA_ABANDONO = 0"
    ## [1] "PORTE_ESCOLA = 0"

<a href="https://sedu.es.gov.br/rede-estadual-de-ensino" class="uri">https://sedu.es.gov.br/rede-estadual-de-ensino</a>

### São Paulo

    enem2015_SP <- filter(enem2015, SG_UF_ESCOLA == "SP")
    kable(
      head(enem2015_SP)
    )

<table style="width:100%;">
<colgroup>
<col style="width: 2%" />
<col style="width: 4%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 6%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 4%" />
<col style="width: 2%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: right;">NU_ANO</th>
<th style="text-align: left;">SG_UF_ESCOLA</th>
<th style="text-align: left;">NO_MUNICIPIO_ESCOLA</th>
<th style="text-align: left;">NO_ESCOLA_EDUCACENSO</th>
<th style="text-align: left;">TP_DEPENDENCIA_ADM_ESCOLA</th>
<th style="text-align: right;">TP_LOCALIZACAO_ESCOLA</th>
<th style="text-align: right;">NU_MATRICULAS</th>
<th style="text-align: right;">NU_PARTICIPANTES</th>
<th style="text-align: right;">NU_TAXA_PARTICIPACAO</th>
<th style="text-align: right;">NU_MEDIA_CN</th>
<th style="text-align: right;">NU_MEDIA_CH</th>
<th style="text-align: right;">NU_MEDIA_LP</th>
<th style="text-align: right;">NU_MEDIA_MT</th>
<th style="text-align: right;">NU_MEDIA_RED</th>
<th style="text-align: left;">INSE</th>
<th style="text-align: right;">NU_TAXA_APROVACAO</th>
<th style="text-align: right;">NU_TAXA_REPROVACAO</th>
<th style="text-align: right;">NU_TAXA_ABANDONO</th>
<th style="text-align: left;">PORTE_ESCOLA</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">São Paulo</td>
<td style="text-align: left;">MARIANO DE OLIVEIRA PROFESSOR</td>
<td style="text-align: left;">Municipal</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">263</td>
<td style="text-align: right;">142</td>
<td style="text-align: right;">53.99</td>
<td style="text-align: right;">459.60</td>
<td style="text-align: right;">546.20</td>
<td style="text-align: right;">506.89</td>
<td style="text-align: right;">440.49</td>
<td style="text-align: right;">521.83</td>
<td style="text-align: left;">Grupo 4</td>
<td style="text-align: right;">71.9</td>
<td style="text-align: right;">28.1</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">Maior que 90 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">São Paulo</td>
<td style="text-align: left;">SILVIO XAVIER ANTUNES PROFESSOR</td>
<td style="text-align: left;">Municipal</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">144</td>
<td style="text-align: right;">79</td>
<td style="text-align: right;">54.86</td>
<td style="text-align: right;">457.21</td>
<td style="text-align: right;">541.97</td>
<td style="text-align: right;">503.26</td>
<td style="text-align: right;">437.66</td>
<td style="text-align: right;">479.49</td>
<td style="text-align: left;">Grupo 4</td>
<td style="text-align: right;">85.5</td>
<td style="text-align: right;">14.1</td>
<td style="text-align: right;">0.4</td>
<td style="text-align: left;">Maior que 90 alunos</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">São Paulo</td>
<td style="text-align: left;">ERMANO MARCHETTI</td>
<td style="text-align: left;">Municipal</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">240</td>
<td style="text-align: right;">131</td>
<td style="text-align: right;">54.58</td>
<td style="text-align: right;">470.81</td>
<td style="text-align: right;">554.04</td>
<td style="text-align: right;">509.87</td>
<td style="text-align: right;">447.22</td>
<td style="text-align: right;">533.13</td>
<td style="text-align: left;">Grupo 4</td>
<td style="text-align: right;">89.0</td>
<td style="text-align: right;">10.7</td>
<td style="text-align: right;">0.3</td>
<td style="text-align: left;">Maior que 90 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">São Paulo</td>
<td style="text-align: left;">HUMBERTO DE SOUZA MELLO GENERAL</td>
<td style="text-align: left;">Municipal</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">288</td>
<td style="text-align: right;">146</td>
<td style="text-align: right;">50.69</td>
<td style="text-align: right;">466.08</td>
<td style="text-align: right;">536.28</td>
<td style="text-align: right;">502.71</td>
<td style="text-align: right;">439.73</td>
<td style="text-align: right;">535.07</td>
<td style="text-align: left;">Grupo 4</td>
<td style="text-align: right;">78.6</td>
<td style="text-align: right;">16.8</td>
<td style="text-align: right;">4.6</td>
<td style="text-align: left;">Maior que 90 alunos</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">São Paulo</td>
<td style="text-align: left;">MANUEL DA NOBREGA PADRE</td>
<td style="text-align: left;">Municipal</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">150</td>
<td style="text-align: right;">95</td>
<td style="text-align: right;">63.33</td>
<td style="text-align: right;">467.01</td>
<td style="text-align: right;">546.34</td>
<td style="text-align: right;">510.41</td>
<td style="text-align: right;">440.67</td>
<td style="text-align: right;">528.00</td>
<td style="text-align: left;">Grupo 4</td>
<td style="text-align: right;">72.4</td>
<td style="text-align: right;">27.6</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">Maior que 90 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">São Paulo</td>
<td style="text-align: left;">JOAQUIM SILVADO DOUTOR</td>
<td style="text-align: left;">Municipal</td>
<td style="text-align: right;">1</td>
<td style="text-align: right;">173</td>
<td style="text-align: right;">100</td>
<td style="text-align: right;">57.80</td>
<td style="text-align: right;">469.23</td>
<td style="text-align: right;">547.72</td>
<td style="text-align: right;">507.81</td>
<td style="text-align: right;">442.05</td>
<td style="text-align: right;">507.00</td>
<td style="text-align: left;">Grupo 4</td>
<td style="text-align: right;">80.1</td>
<td style="text-align: right;">17.9</td>
<td style="text-align: right;">2.0</td>
<td style="text-align: left;">Maior que 90 alunos</td>
</tr>
</tbody>
</table>

    enem2015_SP %>% 
      group_by(TP_LOCALIZACAO_ESCOLA) %>% 
      summarise(N_ESCOLAS = n())

    ## `summarise()` ungrouping output (override with `.groups` argument)

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

sadas

    enem2015_SP$TP_LOCALIZACAO_ESCOLA <- factor(enem2015_SP$TP_LOCALIZACAO_ESCOLA)
    levels(enem2015_SP$TP_LOCALIZACAO_ESCOLA) <- c("Urbana", "Rural")

    enem2015_SP %>% 
      group_by(TP_LOCALIZACAO_ESCOLA) %>% 
      summarise(MED_NAT = mean(NU_MEDIA_CN, na.rm = TRUE)) %>% 
      ggplot(aes(x = TP_LOCALIZACAO_ESCOLA, y = MED_NAT, fill = TP_LOCALIZACAO_ESCOLA)) + 
      geom_col(show.legend = FALSE) +
      labs(title = "Média das escolas de São Paulo em Ciências da Naturezapor localização",
           x = "Localização", y  = "Média em Ciências da Natureza (Biologia, Química e Física)") +
      theme_bw()

    ## `summarise()` ungrouping output (override with `.groups` argument)

![](a_files/figure-markdown_strict/por%20localização%20(rural/urbana)-1.png)

oia

    print(summary(enem2015_SP$NU_MEDIA_RED, na.rm = TRUE))

    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##   400.5   524.0   566.2   577.7   624.0   835.7

hmm

    SP_melhores <- enem2015_SP %>% 
      filter(NU_MEDIA_RED > 750)
    kable(
      arrange(SP_melhores, desc(NU_MEDIA_RED))
    )

<table style="width:100%;">
<colgroup>
<col style="width: 2%" />
<col style="width: 3%" />
<col style="width: 7%" />
<col style="width: 17%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 6%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 2%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: right;">NU_ANO</th>
<th style="text-align: left;">SG_UF_ESCOLA</th>
<th style="text-align: left;">NO_MUNICIPIO_ESCOLA</th>
<th style="text-align: left;">NO_ESCOLA_EDUCACENSO</th>
<th style="text-align: left;">TP_DEPENDENCIA_ADM_ESCOLA</th>
<th style="text-align: left;">TP_LOCALIZACAO_ESCOLA</th>
<th style="text-align: right;">NU_MATRICULAS</th>
<th style="text-align: right;">NU_PARTICIPANTES</th>
<th style="text-align: right;">NU_TAXA_PARTICIPACAO</th>
<th style="text-align: right;">NU_MEDIA_CN</th>
<th style="text-align: right;">NU_MEDIA_CH</th>
<th style="text-align: right;">NU_MEDIA_LP</th>
<th style="text-align: right;">NU_MEDIA_MT</th>
<th style="text-align: right;">NU_MEDIA_RED</th>
<th style="text-align: left;">INSE</th>
<th style="text-align: right;">NU_TAXA_APROVACAO</th>
<th style="text-align: right;">NU_TAXA_REPROVACAO</th>
<th style="text-align: right;">NU_TAXA_ABANDONO</th>
<th style="text-align: left;">PORTE_ESCOLA</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">Ribeirão Preto</td>
<td style="text-align: left;">SEB COC UNIDADE ALVARES CABRAL</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">44</td>
<td style="text-align: right;">42</td>
<td style="text-align: right;">95.45</td>
<td style="text-align: right;">676.02</td>
<td style="text-align: right;">683.77</td>
<td style="text-align: right;">632.48</td>
<td style="text-align: right;">719.44</td>
<td style="text-align: right;">835.71</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">100.0</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">De 31 a 60 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">São Paulo</td>
<td style="text-align: left;">VITAL BRAZIL COLEGIO</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">49</td>
<td style="text-align: right;">45</td>
<td style="text-align: right;">91.84</td>
<td style="text-align: right;">631.11</td>
<td style="text-align: right;">664.92</td>
<td style="text-align: right;">605.77</td>
<td style="text-align: right;">714.21</td>
<td style="text-align: right;">830.78</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">97.1</td>
<td style="text-align: right;">2.9</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">De 31 a 60 alunos</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">São Paulo</td>
<td style="text-align: left;">PENTAGONO COLEGIO UNIDADE CAIUBI</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">56</td>
<td style="text-align: right;">54</td>
<td style="text-align: right;">96.43</td>
<td style="text-align: right;">616.42</td>
<td style="text-align: right;">667.68</td>
<td style="text-align: right;">619.12</td>
<td style="text-align: right;">693.54</td>
<td style="text-align: right;">823.33</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">94.8</td>
<td style="text-align: right;">5.2</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">De 31 a 60 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">São Carlos</td>
<td style="text-align: left;">SAO CARLOS INSTITUTO EDUCACAO DE ENSINO FUNDAMENTAL E MEDIO</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">31</td>
<td style="text-align: right;">31</td>
<td style="text-align: right;">100.00</td>
<td style="text-align: right;">648.93</td>
<td style="text-align: right;">688.47</td>
<td style="text-align: right;">635.75</td>
<td style="text-align: right;">709.35</td>
<td style="text-align: right;">821.94</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">99.3</td>
<td style="text-align: right;">0.7</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">De 31 a 60 alunos</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">São Paulo</td>
<td style="text-align: left;">LICEU DE ARTES E OFICIOS DE SAO PAULO ESCOLA TECNICA</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">119</td>
<td style="text-align: right;">115</td>
<td style="text-align: right;">96.64</td>
<td style="text-align: right;">650.56</td>
<td style="text-align: right;">691.59</td>
<td style="text-align: right;">632.86</td>
<td style="text-align: right;">782.11</td>
<td style="text-align: right;">814.26</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">97.9</td>
<td style="text-align: right;">2.1</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">Maior que 90 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">São Paulo</td>
<td style="text-align: left;">OBJETIVO COLEGIO INTEGRADO</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">41</td>
<td style="text-align: right;">41</td>
<td style="text-align: right;">100.00</td>
<td style="text-align: right;">728.80</td>
<td style="text-align: right;">721.47</td>
<td style="text-align: right;">681.23</td>
<td style="text-align: right;">873.65</td>
<td style="text-align: right;">813.17</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">100.0</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">De 31 a 60 alunos</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">São Paulo</td>
<td style="text-align: left;">MOBILE COLEGIO</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">146</td>
<td style="text-align: right;">124</td>
<td style="text-align: right;">84.93</td>
<td style="text-align: right;">689.40</td>
<td style="text-align: right;">708.53</td>
<td style="text-align: right;">648.92</td>
<td style="text-align: right;">779.91</td>
<td style="text-align: right;">812.42</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">95.8</td>
<td style="text-align: right;">4.2</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">Maior que 90 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">Santos</td>
<td style="text-align: left;">OBJETIVO DO LITORAL CENTRO EDUCACIONAL</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">22</td>
<td style="text-align: right;">21</td>
<td style="text-align: right;">95.45</td>
<td style="text-align: right;">636.15</td>
<td style="text-align: right;">680.21</td>
<td style="text-align: right;">630.79</td>
<td style="text-align: right;">722.26</td>
<td style="text-align: right;">812.38</td>
<td style="text-align: left;">Grupo 5</td>
<td style="text-align: right;">99.7</td>
<td style="text-align: right;">0.3</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">De 1 a 30 alunos</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">Franca</td>
<td style="text-align: left;">NOVO COLEGIO</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">79</td>
<td style="text-align: right;">79</td>
<td style="text-align: right;">100.00</td>
<td style="text-align: right;">605.41</td>
<td style="text-align: right;">651.31</td>
<td style="text-align: right;">597.07</td>
<td style="text-align: right;">668.01</td>
<td style="text-align: right;">807.09</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">98.2</td>
<td style="text-align: right;">1.8</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">De 61 a 90 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">São José dos Campos</td>
<td style="text-align: left;">INSTITUTO EDUCACIONAL IGUATEMY ESCOLA DE EI EF E EM</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">18</td>
<td style="text-align: right;">16</td>
<td style="text-align: right;">88.89</td>
<td style="text-align: right;">605.94</td>
<td style="text-align: right;">647.89</td>
<td style="text-align: right;">584.69</td>
<td style="text-align: right;">654.88</td>
<td style="text-align: right;">806.25</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">94.2</td>
<td style="text-align: right;">4.3</td>
<td style="text-align: right;">1.5</td>
<td style="text-align: left;">De 1 a 30 alunos</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">Amparo</td>
<td style="text-align: left;">VILLA LOBOS COLEGIO</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">47</td>
<td style="text-align: right;">46</td>
<td style="text-align: right;">97.87</td>
<td style="text-align: right;">616.73</td>
<td style="text-align: right;">661.19</td>
<td style="text-align: right;">596.27</td>
<td style="text-align: right;">670.22</td>
<td style="text-align: right;">804.78</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">95.8</td>
<td style="text-align: right;">4.2</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">De 31 a 60 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">São Caetano do Sul</td>
<td style="text-align: left;">VILLARE COLEGIO</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">28</td>
<td style="text-align: right;">26</td>
<td style="text-align: right;">92.86</td>
<td style="text-align: right;">646.87</td>
<td style="text-align: right;">687.91</td>
<td style="text-align: right;">624.96</td>
<td style="text-align: right;">758.27</td>
<td style="text-align: right;">800.77</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">92.4</td>
<td style="text-align: right;">7.6</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">De 1 a 30 alunos</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">Taubaté</td>
<td style="text-align: left;">PROGRESSAO COLEGIO</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">55</td>
<td style="text-align: right;">52</td>
<td style="text-align: right;">94.55</td>
<td style="text-align: right;">609.83</td>
<td style="text-align: right;">656.01</td>
<td style="text-align: right;">597.01</td>
<td style="text-align: right;">650.42</td>
<td style="text-align: right;">796.92</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">98.1</td>
<td style="text-align: right;">1.4</td>
<td style="text-align: right;">0.5</td>
<td style="text-align: left;">De 31 a 60 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">Campinas</td>
<td style="text-align: left;">PROGRESSO CAMPINEIRO COLEGIO</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">46</td>
<td style="text-align: right;">46</td>
<td style="text-align: right;">100.00</td>
<td style="text-align: right;">642.22</td>
<td style="text-align: right;">684.77</td>
<td style="text-align: right;">622.98</td>
<td style="text-align: right;">725.40</td>
<td style="text-align: right;">796.52</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">93.5</td>
<td style="text-align: right;">6.5</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">De 31 a 60 alunos</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">Mogi das Cruzes</td>
<td style="text-align: left;">OBJETIVO INTEGRADO DE MOGI DAS CRUZES COLEGIO</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">50</td>
<td style="text-align: right;">50</td>
<td style="text-align: right;">100.00</td>
<td style="text-align: right;">652.47</td>
<td style="text-align: right;">685.18</td>
<td style="text-align: right;">632.47</td>
<td style="text-align: right;">793.29</td>
<td style="text-align: right;">795.60</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">100.0</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">De 31 a 60 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">Valinhos</td>
<td style="text-align: left;">PORTO SEGURO VISCONDE COLEGIO UNIDADE II</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">139</td>
<td style="text-align: right;">122</td>
<td style="text-align: right;">87.77</td>
<td style="text-align: right;">639.46</td>
<td style="text-align: right;">684.72</td>
<td style="text-align: right;">629.99</td>
<td style="text-align: right;">736.72</td>
<td style="text-align: right;">794.59</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">96.1</td>
<td style="text-align: right;">3.9</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">Maior que 90 alunos</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">São José dos Campos</td>
<td style="text-align: left;">EMBRAER JUAREZ WANDERLEY COLEGIO</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">160</td>
<td style="text-align: right;">160</td>
<td style="text-align: right;">100.00</td>
<td style="text-align: right;">647.86</td>
<td style="text-align: right;">669.53</td>
<td style="text-align: right;">615.98</td>
<td style="text-align: right;">772.01</td>
<td style="text-align: right;">792.75</td>
<td style="text-align: left;">Grupo 5</td>
<td style="text-align: right;">99.8</td>
<td style="text-align: right;">0.2</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">Maior que 90 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">Sorocaba</td>
<td style="text-align: left;">UIRAPURU COLEGIO</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">77</td>
<td style="text-align: right;">70</td>
<td style="text-align: right;">90.91</td>
<td style="text-align: right;">650.46</td>
<td style="text-align: right;">679.07</td>
<td style="text-align: right;">614.50</td>
<td style="text-align: right;">731.58</td>
<td style="text-align: right;">784.86</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">96.1</td>
<td style="text-align: right;">3.9</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">De 61 a 90 alunos</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">São Paulo</td>
<td style="text-align: left;">ETAPA III COLEGIO</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">35</td>
<td style="text-align: right;">32</td>
<td style="text-align: right;">91.43</td>
<td style="text-align: right;">730.51</td>
<td style="text-align: right;">705.41</td>
<td style="text-align: right;">650.68</td>
<td style="text-align: right;">858.77</td>
<td style="text-align: right;">783.75</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">100.0</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">De 31 a 60 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">Guarulhos</td>
<td style="text-align: left;">MATER AMABILIS COLEGIO</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">98</td>
<td style="text-align: right;">95</td>
<td style="text-align: right;">96.94</td>
<td style="text-align: right;">638.61</td>
<td style="text-align: right;">680.49</td>
<td style="text-align: right;">627.09</td>
<td style="text-align: right;">744.37</td>
<td style="text-align: right;">783.58</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">98.4</td>
<td style="text-align: right;">1.6</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">Maior que 90 alunos</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">Americana</td>
<td style="text-align: left;">ANTARES COLEGIO</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">50</td>
<td style="text-align: right;">49</td>
<td style="text-align: right;">98.00</td>
<td style="text-align: right;">619.00</td>
<td style="text-align: right;">662.10</td>
<td style="text-align: right;">607.89</td>
<td style="text-align: right;">691.87</td>
<td style="text-align: right;">782.45</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">98.6</td>
<td style="text-align: right;">1.4</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">De 31 a 60 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">Botucatu</td>
<td style="text-align: left;">LA SALLE COLEGIO</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">33</td>
<td style="text-align: right;">30</td>
<td style="text-align: right;">90.91</td>
<td style="text-align: right;">545.21</td>
<td style="text-align: right;">643.32</td>
<td style="text-align: right;">593.71</td>
<td style="text-align: right;">580.40</td>
<td style="text-align: right;">782.00</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">97.8</td>
<td style="text-align: right;">2.2</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">De 31 a 60 alunos</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">São Paulo</td>
<td style="text-align: left;">VERTICE COLEGIO UNIDADE II</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">77</td>
<td style="text-align: right;">75</td>
<td style="text-align: right;">97.40</td>
<td style="text-align: right;">698.02</td>
<td style="text-align: right;">702.69</td>
<td style="text-align: right;">649.93</td>
<td style="text-align: right;">792.06</td>
<td style="text-align: right;">778.13</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">98.8</td>
<td style="text-align: right;">1.2</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">De 61 a 90 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">Marília</td>
<td style="text-align: left;">CRIATIVO COLEGIO</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">76</td>
<td style="text-align: right;">70</td>
<td style="text-align: right;">92.11</td>
<td style="text-align: right;">603.67</td>
<td style="text-align: right;">654.30</td>
<td style="text-align: right;">598.02</td>
<td style="text-align: right;">625.05</td>
<td style="text-align: right;">774.29</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">97.6</td>
<td style="text-align: right;">2.4</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">De 61 a 90 alunos</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">São Paulo</td>
<td style="text-align: left;">SAO JOSE COLEGIO AGOSTINIANO</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">124</td>
<td style="text-align: right;">122</td>
<td style="text-align: right;">98.39</td>
<td style="text-align: right;">611.02</td>
<td style="text-align: right;">659.11</td>
<td style="text-align: right;">603.89</td>
<td style="text-align: right;">680.89</td>
<td style="text-align: right;">773.11</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">97.3</td>
<td style="text-align: right;">2.7</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">Maior que 90 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">Santo André</td>
<td style="text-align: left;">LICEU JARDIM</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">97</td>
<td style="text-align: right;">93</td>
<td style="text-align: right;">95.88</td>
<td style="text-align: right;">656.97</td>
<td style="text-align: right;">684.90</td>
<td style="text-align: right;">631.33</td>
<td style="text-align: right;">736.92</td>
<td style="text-align: right;">772.69</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">88.7</td>
<td style="text-align: right;">11.3</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">Maior que 90 alunos</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">São Paulo</td>
<td style="text-align: left;">ALBERT SABIN COLEGIO</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">134</td>
<td style="text-align: right;">125</td>
<td style="text-align: right;">93.28</td>
<td style="text-align: right;">649.94</td>
<td style="text-align: right;">680.01</td>
<td style="text-align: right;">622.18</td>
<td style="text-align: right;">747.35</td>
<td style="text-align: right;">772.00</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">92.7</td>
<td style="text-align: right;">7.3</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">Maior que 90 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">Espírito Santo do Pinhal</td>
<td style="text-align: left;">ESPIRITO SANTO DO PINHAL COLEGIO</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">12</td>
<td style="text-align: right;">11</td>
<td style="text-align: right;">91.67</td>
<td style="text-align: right;">546.01</td>
<td style="text-align: right;">606.58</td>
<td style="text-align: right;">574.17</td>
<td style="text-align: right;">621.73</td>
<td style="text-align: right;">769.09</td>
<td style="text-align: left;">Grupo 5</td>
<td style="text-align: right;">98.3</td>
<td style="text-align: right;">1.7</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">De 1 a 30 alunos</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">Osasco</td>
<td style="text-align: left;">LEONARDO DA VINCI COLEGIO ANGLO</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">16</td>
<td style="text-align: right;">14</td>
<td style="text-align: right;">87.50</td>
<td style="text-align: right;">653.81</td>
<td style="text-align: right;">670.01</td>
<td style="text-align: right;">623.69</td>
<td style="text-align: right;">667.16</td>
<td style="text-align: right;">767.14</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">93.8</td>
<td style="text-align: right;">6.2</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">De 1 a 30 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">Bauru</td>
<td style="text-align: left;">FOUR C BILINGUAL ACADEMY</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">12</td>
<td style="text-align: right;">12</td>
<td style="text-align: right;">100.00</td>
<td style="text-align: right;">552.40</td>
<td style="text-align: right;">655.59</td>
<td style="text-align: right;">595.04</td>
<td style="text-align: right;">535.95</td>
<td style="text-align: right;">766.67</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">100.0</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">De 1 a 30 alunos</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">Cotia</td>
<td style="text-align: left;">SIDARTA COLEGIO</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">16</td>
<td style="text-align: right;">13</td>
<td style="text-align: right;">81.25</td>
<td style="text-align: right;">639.20</td>
<td style="text-align: right;">678.03</td>
<td style="text-align: right;">649.89</td>
<td style="text-align: right;">706.43</td>
<td style="text-align: right;">764.62</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">98.3</td>
<td style="text-align: right;">1.7</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">De 1 a 30 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">São Paulo</td>
<td style="text-align: left;">BEIT YAACOV ESCOLA</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">33</td>
<td style="text-align: right;">24</td>
<td style="text-align: right;">72.73</td>
<td style="text-align: right;">580.72</td>
<td style="text-align: right;">667.38</td>
<td style="text-align: right;">623.50</td>
<td style="text-align: right;">702.26</td>
<td style="text-align: right;">764.17</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">100.0</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">De 31 a 60 alunos</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">Santana de Parnaíba</td>
<td style="text-align: left;">PENTAGONO COLEGIO UNIDADE ALPHAVILLE</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">40</td>
<td style="text-align: right;">35</td>
<td style="text-align: right;">87.50</td>
<td style="text-align: right;">574.77</td>
<td style="text-align: right;">636.41</td>
<td style="text-align: right;">586.09</td>
<td style="text-align: right;">674.92</td>
<td style="text-align: right;">762.86</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">97.5</td>
<td style="text-align: right;">2.5</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">De 31 a 60 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">São Manuel</td>
<td style="text-align: left;">LUMA CAROLINA COLEGIO</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">22</td>
<td style="text-align: right;">21</td>
<td style="text-align: right;">95.45</td>
<td style="text-align: right;">553.32</td>
<td style="text-align: right;">626.13</td>
<td style="text-align: right;">567.43</td>
<td style="text-align: right;">558.07</td>
<td style="text-align: right;">762.86</td>
<td style="text-align: left;">Grupo 5</td>
<td style="text-align: right;">100.0</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">De 1 a 30 alunos</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">São Paulo</td>
<td style="text-align: left;">COLEGIO PENTAGONO LDTA</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">40</td>
<td style="text-align: right;">38</td>
<td style="text-align: right;">95.00</td>
<td style="text-align: right;">608.03</td>
<td style="text-align: right;">664.32</td>
<td style="text-align: right;">606.66</td>
<td style="text-align: right;">693.86</td>
<td style="text-align: right;">760.00</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">90.1</td>
<td style="text-align: right;">9.9</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">De 31 a 60 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">Campinas</td>
<td style="text-align: left;">ASTHER COLEGIO</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">20</td>
<td style="text-align: right;">19</td>
<td style="text-align: right;">95.00</td>
<td style="text-align: right;">585.48</td>
<td style="text-align: right;">641.17</td>
<td style="text-align: right;">600.56</td>
<td style="text-align: right;">604.38</td>
<td style="text-align: right;">760.00</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">93.9</td>
<td style="text-align: right;">6.1</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">De 1 a 30 alunos</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">São José dos Campos</td>
<td style="text-align: left;">POLIEDRO COLEGIO</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">452</td>
<td style="text-align: right;">413</td>
<td style="text-align: right;">91.37</td>
<td style="text-align: right;">640.42</td>
<td style="text-align: right;">672.05</td>
<td style="text-align: right;">617.47</td>
<td style="text-align: right;">714.33</td>
<td style="text-align: right;">757.87</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">98.2</td>
<td style="text-align: right;">1.8</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">Maior que 90 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">São Carlos</td>
<td style="text-align: left;">EDUCATIVA INSTITUTO DE EDUCACAO E CULTURA</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">57</td>
<td style="text-align: right;">55</td>
<td style="text-align: right;">96.49</td>
<td style="text-align: right;">606.52</td>
<td style="text-align: right;">658.62</td>
<td style="text-align: right;">599.27</td>
<td style="text-align: right;">670.54</td>
<td style="text-align: right;">756.00</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">97.8</td>
<td style="text-align: right;">2.2</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">De 31 a 60 alunos</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">São José do Rio Pardo</td>
<td style="text-align: left;">UNIGRAU COLEGIO</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">24</td>
<td style="text-align: right;">22</td>
<td style="text-align: right;">91.67</td>
<td style="text-align: right;">588.22</td>
<td style="text-align: right;">631.24</td>
<td style="text-align: right;">595.56</td>
<td style="text-align: right;">636.99</td>
<td style="text-align: right;">754.55</td>
<td style="text-align: left;">Grupo 5</td>
<td style="text-align: right;">88.6</td>
<td style="text-align: right;">11.4</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">De 1 a 30 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">São Paulo</td>
<td style="text-align: left;">SANTA AMALIA COLEGIO</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">23</td>
<td style="text-align: right;">23</td>
<td style="text-align: right;">100.00</td>
<td style="text-align: right;">611.67</td>
<td style="text-align: right;">645.06</td>
<td style="text-align: right;">604.41</td>
<td style="text-align: right;">655.28</td>
<td style="text-align: right;">754.35</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">91.7</td>
<td style="text-align: right;">8.3</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">De 1 a 30 alunos</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">São Paulo</td>
<td style="text-align: left;">GERMINARE ESCOLA</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">72</td>
<td style="text-align: right;">68</td>
<td style="text-align: right;">94.44</td>
<td style="text-align: right;">617.97</td>
<td style="text-align: right;">668.95</td>
<td style="text-align: right;">621.39</td>
<td style="text-align: right;">743.58</td>
<td style="text-align: right;">753.82</td>
<td style="text-align: left;">Grupo 5</td>
<td style="text-align: right;">97.7</td>
<td style="text-align: right;">2.3</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">De 61 a 90 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">Campinas</td>
<td style="text-align: left;">INTEGRAL COLEGIO DE EDUC BASICA</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">50</td>
<td style="text-align: right;">45</td>
<td style="text-align: right;">90.00</td>
<td style="text-align: right;">605.94</td>
<td style="text-align: right;">647.27</td>
<td style="text-align: right;">583.68</td>
<td style="text-align: right;">657.09</td>
<td style="text-align: right;">753.78</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">95.3</td>
<td style="text-align: right;">4.7</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">De 31 a 60 alunos</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">São Paulo</td>
<td style="text-align: left;">POLIEDRO COLEGIO</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">130</td>
<td style="text-align: right;">120</td>
<td style="text-align: right;">92.31</td>
<td style="text-align: right;">626.42</td>
<td style="text-align: right;">666.28</td>
<td style="text-align: right;">609.36</td>
<td style="text-align: right;">688.82</td>
<td style="text-align: right;">752.50</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">98.6</td>
<td style="text-align: right;">1.4</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">Maior que 90 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">Atibaia</td>
<td style="text-align: left;">ATIBAIA COLEGIO INTEGRADO DE</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">57</td>
<td style="text-align: right;">54</td>
<td style="text-align: right;">94.74</td>
<td style="text-align: right;">601.37</td>
<td style="text-align: right;">647.09</td>
<td style="text-align: right;">597.43</td>
<td style="text-align: right;">656.47</td>
<td style="text-align: right;">751.11</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">95.7</td>
<td style="text-align: right;">4.3</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">De 31 a 60 alunos</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">Pindamonhangaba</td>
<td style="text-align: left;">PROGRESSAO COLEGIO</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">37</td>
<td style="text-align: right;">36</td>
<td style="text-align: right;">97.30</td>
<td style="text-align: right;">595.30</td>
<td style="text-align: right;">647.33</td>
<td style="text-align: right;">594.86</td>
<td style="text-align: right;">616.44</td>
<td style="text-align: right;">751.11</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">99.1</td>
<td style="text-align: right;">0.9</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">De 31 a 60 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">Taubaté</td>
<td style="text-align: left;">OBJETIVO JUNIOR COLEGIO</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">20</td>
<td style="text-align: right;">20</td>
<td style="text-align: right;">100.00</td>
<td style="text-align: right;">649.16</td>
<td style="text-align: right;">680.15</td>
<td style="text-align: right;">625.10</td>
<td style="text-align: right;">724.78</td>
<td style="text-align: right;">751.00</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">97.9</td>
<td style="text-align: right;">2.1</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">De 1 a 30 alunos</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">Pindamonhangaba</td>
<td style="text-align: left;">MAGISTRA COLEGIO</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">12</td>
<td style="text-align: right;">11</td>
<td style="text-align: right;">91.67</td>
<td style="text-align: right;">545.45</td>
<td style="text-align: right;">622.42</td>
<td style="text-align: right;">596.30</td>
<td style="text-align: right;">639.45</td>
<td style="text-align: right;">750.91</td>
<td style="text-align: left;">Grupo 5</td>
<td style="text-align: right;">100.0</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">De 1 a 30 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">Caçapava</td>
<td style="text-align: left;">CECILIA CACAPAVA CONDE COLEGIO EIPSG</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">11</td>
<td style="text-align: right;">11</td>
<td style="text-align: right;">100.00</td>
<td style="text-align: right;">545.88</td>
<td style="text-align: right;">635.12</td>
<td style="text-align: right;">586.85</td>
<td style="text-align: right;">636.35</td>
<td style="text-align: right;">750.91</td>
<td style="text-align: left;">Grupo 5</td>
<td style="text-align: right;">94.0</td>
<td style="text-align: right;">6.0</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">De 1 a 30 alunos</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">Marília</td>
<td style="text-align: left;">CRISTO REI COLEGIO</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">103</td>
<td style="text-align: right;">93</td>
<td style="text-align: right;">90.29</td>
<td style="text-align: right;">581.93</td>
<td style="text-align: right;">632.64</td>
<td style="text-align: right;">585.18</td>
<td style="text-align: right;">600.60</td>
<td style="text-align: right;">750.54</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">97.6</td>
<td style="text-align: right;">2.4</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">Maior que 90 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">São José do Rio Preto</td>
<td style="text-align: left;">LONDON COLEGIO</td>
<td style="text-align: left;">Privada</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">131</td>
<td style="text-align: right;">116</td>
<td style="text-align: right;">88.55</td>
<td style="text-align: right;">607.21</td>
<td style="text-align: right;">639.11</td>
<td style="text-align: right;">590.89</td>
<td style="text-align: right;">659.18</td>
<td style="text-align: right;">750.52</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">100.0</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">Maior que 90 alunos</td>
</tr>
</tbody>
</table>

sad

    SP_melhores %>% 
      mutate(CAPITAL = ifelse(NO_MUNICIPIO_ESCOLA == "São Paulo",
                              "Capital", "Interior")) %>% 
      ggplot(aes(x = CAPITAL)) +
      geom_bar()

![](a_files/figure-markdown_strict/Quantão%20são%20da%20capital-1.png)

dsa

    enem2015_SP %>% 
      mutate(CAPITAL = ifelse(NO_MUNICIPIO_ESCOLA == "São Paulo",
                              "Capital", "Interior")) %>% 
      group_by(CAPITAL) %>% 
      summarise(N_ESCOLAS = n()) %>% 
      ggplot(aes(x = CAPITAL, y = N_ESCOLAS)) +
      geom_col()

    ## `summarise()` ungrouping output (override with `.groups` argument)

![](a_files/figure-markdown_strict/quantas%20no%20total%20são%20da%20capital-1.png)

sa

    SP_publicas <- enem2015_SP %>% 
      filter(TP_DEPENDENCIA_ADM_ESCOLA != "Privada")
    kable(
      head(arrange(SP_publicas, desc(NU_MEDIA_MT)))
    )

<table style="width:100%;">
<colgroup>
<col style="width: 2%" />
<col style="width: 3%" />
<col style="width: 6%" />
<col style="width: 15%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 2%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: right;">NU_ANO</th>
<th style="text-align: left;">SG_UF_ESCOLA</th>
<th style="text-align: left;">NO_MUNICIPIO_ESCOLA</th>
<th style="text-align: left;">NO_ESCOLA_EDUCACENSO</th>
<th style="text-align: left;">TP_DEPENDENCIA_ADM_ESCOLA</th>
<th style="text-align: left;">TP_LOCALIZACAO_ESCOLA</th>
<th style="text-align: right;">NU_MATRICULAS</th>
<th style="text-align: right;">NU_PARTICIPANTES</th>
<th style="text-align: right;">NU_TAXA_PARTICIPACAO</th>
<th style="text-align: right;">NU_MEDIA_CN</th>
<th style="text-align: right;">NU_MEDIA_CH</th>
<th style="text-align: right;">NU_MEDIA_LP</th>
<th style="text-align: right;">NU_MEDIA_MT</th>
<th style="text-align: right;">NU_MEDIA_RED</th>
<th style="text-align: left;">INSE</th>
<th style="text-align: right;">NU_TAXA_APROVACAO</th>
<th style="text-align: right;">NU_TAXA_REPROVACAO</th>
<th style="text-align: right;">NU_TAXA_ABANDONO</th>
<th style="text-align: left;">PORTE_ESCOLA</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">Campinas</td>
<td style="text-align: left;">CAMPINAS COLEGIO TECNICO DE - UNICAMP</td>
<td style="text-align: left;">Municipal</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">296</td>
<td style="text-align: right;">251</td>
<td style="text-align: right;">84.80</td>
<td style="text-align: right;">604.06</td>
<td style="text-align: right;">647.37</td>
<td style="text-align: right;">600.03</td>
<td style="text-align: right;">708.29</td>
<td style="text-align: right;">653.47</td>
<td style="text-align: left;">Grupo 5</td>
<td style="text-align: right;">76.0</td>
<td style="text-align: right;">23.4</td>
<td style="text-align: right;">0.6</td>
<td style="text-align: left;">Maior que 90 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">Bauru</td>
<td style="text-align: left;">COL TEC INDUSTRIAL PROF ISAAC PORTAL ROLDAN UNESP</td>
<td style="text-align: left;">Municipal</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">126</td>
<td style="text-align: right;">123</td>
<td style="text-align: right;">97.62</td>
<td style="text-align: right;">618.94</td>
<td style="text-align: right;">665.28</td>
<td style="text-align: right;">614.48</td>
<td style="text-align: right;">702.57</td>
<td style="text-align: right;">683.25</td>
<td style="text-align: left;">Grupo 6</td>
<td style="text-align: right;">97.9</td>
<td style="text-align: right;">1.6</td>
<td style="text-align: right;">0.5</td>
<td style="text-align: left;">Maior que 90 alunos</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">São Paulo</td>
<td style="text-align: left;">IFSP - CAMPUS SAO PAULO</td>
<td style="text-align: left;">Federal</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">132</td>
<td style="text-align: right;">122</td>
<td style="text-align: right;">92.42</td>
<td style="text-align: right;">605.28</td>
<td style="text-align: right;">662.32</td>
<td style="text-align: right;">610.49</td>
<td style="text-align: right;">702.40</td>
<td style="text-align: right;">647.54</td>
<td style="text-align: left;">Grupo 5</td>
<td style="text-align: right;">90.0</td>
<td style="text-align: right;">9.1</td>
<td style="text-align: right;">0.9</td>
<td style="text-align: left;">Maior que 90 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">Guaratinguetá</td>
<td style="text-align: left;">CARLOS AUGUSTO PATRICIO AMORIM PROF CTIG UNESP</td>
<td style="text-align: left;">Municipal</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">107</td>
<td style="text-align: right;">98</td>
<td style="text-align: right;">91.59</td>
<td style="text-align: right;">591.39</td>
<td style="text-align: right;">639.62</td>
<td style="text-align: right;">596.07</td>
<td style="text-align: right;">702.13</td>
<td style="text-align: right;">675.10</td>
<td style="text-align: left;">Grupo 5</td>
<td style="text-align: right;">92.7</td>
<td style="text-align: right;">7.3</td>
<td style="text-align: right;">0.0</td>
<td style="text-align: left;">Maior que 90 alunos</td>
</tr>
<tr class="odd">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">São Paulo</td>
<td style="text-align: left;">SAO PAULO ETEC DE</td>
<td style="text-align: left;">Municipal</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">193</td>
<td style="text-align: right;">187</td>
<td style="text-align: right;">96.89</td>
<td style="text-align: right;">617.86</td>
<td style="text-align: right;">677.17</td>
<td style="text-align: right;">623.83</td>
<td style="text-align: right;">691.92</td>
<td style="text-align: right;">707.27</td>
<td style="text-align: left;">Grupo 5</td>
<td style="text-align: right;">95.2</td>
<td style="text-align: right;">2.9</td>
<td style="text-align: right;">1.9</td>
<td style="text-align: left;">Maior que 90 alunos</td>
</tr>
<tr class="even">
<td style="text-align: right;">2015</td>
<td style="text-align: left;">SP</td>
<td style="text-align: left;">Limeira</td>
<td style="text-align: left;">LIMEIRA COLEGIO TECNICO DE UNICAMP</td>
<td style="text-align: left;">Municipal</td>
<td style="text-align: left;">Urbana</td>
<td style="text-align: right;">293</td>
<td style="text-align: right;">271</td>
<td style="text-align: right;">92.49</td>
<td style="text-align: right;">573.85</td>
<td style="text-align: right;">637.98</td>
<td style="text-align: right;">590.29</td>
<td style="text-align: right;">669.67</td>
<td style="text-align: right;">661.99</td>
<td style="text-align: left;">Grupo 5</td>
<td style="text-align: right;">94.2</td>
<td style="text-align: right;">5.7</td>
<td style="text-align: right;">0.1</td>
<td style="text-align: left;">Maior que 90 alunos</td>
</tr>
</tbody>
</table>

etecs

    SP_tecnicas <- SP_publicas %>% 
      mutate(Tecnica = ifelse(str_detect(NO_ESCOLA_EDUCACENSO, "TEC"), # ETEC ou TECNINO/TECNICA
                              "Escola Técnica", "Escola Não-técnica"))
    kable(
      SP_tecnicas %>% 
        select(NO_ESCOLA_EDUCACENSO, Tecnica) %>% 
        arrange(desc(Tecnica))
    )

<table>
<colgroup>
<col style="width: 77%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">NO_ESCOLA_EDUCACENSO</th>
<th style="text-align: left;">Tecnica</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;">ALBERT EINSTEIN ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">HORACIO AUGUSTO DA SILVEIRA PROF ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CARLOS DE CAMPOS ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CAMARGO ARANHA PROF ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE ROCHA MENDES ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARTIN LUTHER KING ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">APRIGIO GONZAGA PROF ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">BASILIDES DE GODOY PROF ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">GUARACY SILVEIRA ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">GETULIO VARGAS ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PRESIDENTE VARGAS ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JULIO DE MESQUITA ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE SANT ANA DE CASTRO PROF ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ALFREDO DE BARROS SANTOS PROF ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOAO GOMES DE ARAUJO ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE BENTO CONEGO ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MACHADO DE ASSIS ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE ESTEVES PREFEITO ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">DOMINGOS MINICUCCI FILHO DR ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">SEBASTIANA DE BARROS DONA ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">EDSON GALVAO PROF ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">DARIO PACHECO PEDROSO DR ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">DEMETRIO AZEVEDO JUNIOR DR ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARTINHO DI CIERO ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">FERNANDO PRESTES ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">RUBENS DE FARIA E SOUZA ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">SALES GOMES ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOAO BELARMINO ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">BENTO QUIRINO ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">FRANCISCO NOGUEIRA DE LIMA DR ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">FRANCISCO GARCIA ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ROSA PERRONE SCAVONE ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">BENEDITO STORANI ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ALBERTO FERES PREFEITO ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">TRAJANO CAMARGO ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CAROLINO DA MOTTA E SILVA DR ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PEDRO FERREIRA ALVES ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">FERNANDO FEBELIANO DA COSTA CEL ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE COURY DR ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ARMANDO BAYEUX DA SILVA PROF ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANNA DE OLIVEIRA FERRAZ PROFA ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">RAPHAEL BRANDAO CEL ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JULIO CARDOSO DR ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANTONIO DE PADUA CARDOSO ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CARMELINO CORREA JR PROF ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANTONIO JUNQUEIRA DA VEIGA ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">LAURINDO ALVES QUEIROZ ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE MARTIMIANO DA SILVA ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">FRANCISCO DOS SANTOS PROF ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MANOEL DOS REIS ARAUJO ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PAULINO BOTELHO ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">PEDRO BADRAN ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ALCIDIO DE SOUZA PRADO PROF ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ASTOR DE MATTOS CARVALHO ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOAQUIM FERREIRA DO AMARAL ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">HELCY MOREIRA MARTINS AGUIAR PROFA ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ELIAS NECHAR ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MATHEUS LEITE DE ABREU PROF ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PHILADELPHO GOUVEA NETTO ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ARNALDO MARIA DE ITAPORANGA FREI ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">EUDECIO LUIZ VICENTE PROF ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">HERVAL BELLUSCI ENGENHEIRO ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CARMELINA BARBOSA PROFA ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANTONIO EUFRASIO DE TOLEDO PROF DR ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">FRANCISCO FRANCO DEPUTADO ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">LUIZ PIRES BARBOSA PROF ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PEDRO D ARCADIA NETO ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">AUGUSTO TORTOLERO ARAUJO ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">LUIZ CESAR COUTO DR ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANTONIO MAGLIANO MONSENHOR ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PAULO ORNELLAS CARVALHO DE BARROS DEP ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANTONIO DEVISATE ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PAULO GUERREIRO FRANCO ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JACINTO FERREIRA DE SA ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PEDRO LEME BRISOLLA SOBRINHO PROF ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ORLANDO QUAGLIATO ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">NARCISO DE MEDEIROS ENG AGRONOMO ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE NUNES DIAS PADRE ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ARISTOTELES FERREIRA ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANTONIO PRADO CONSELHEIRO ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CAMPINAS COLEGIO TECNICO DE - UNICAMP</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">LIMEIRA COLEGIO TECNICO DE UNICAMP</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">POLIVALENTE DE AMERICANA ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOAO BAPTISTA DE LIMA FIGUEIREDO ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">VASCO ANTONIO VENCHIARUTTI ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">COLEGIO TECNICO AGRICOLA JOSE BONIFACIO UNESP CAMPUS JABOTICABAL</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">LAURO GOMES ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JORGE STREET ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">GUAIANAZES ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">SAO FRANCISCO DE ASSIS ESCOLA TECNICA AGROPECUARIA MUNICIPAL</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PAULINIA ESCOLA TECNICA DE</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">RENATO CORDEIRO DOUTOR ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CELSO CHARURI DR ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">GERALDO JOSE RODRIGUES ALCKMIN DR ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CARMINE BIAGIO TUNDISI PROF ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MASSUYUKI KAWANO ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">TEREZINHA MONTEIRO DOS SANTOS PROFA ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">EMILIO HERNANDEZ AGUILAR DR ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">GUSTAVO KLUG TENENTE AVIADOR ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">RODRIGUES DE ABREU ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ZONA SUL ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">FAUSTO MAZZOLA PROF ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">FERNANDOPOLIS ETEC DE</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">RIBEIRAO PIRES ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">LINS ETEC DE</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">IDIO ZUCCHI PROFESSOR ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">SAO JOSE DO RIO PARDO ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ALBERTO SANTOS DUMONT ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANDRE BOGASIAN PROFESSOR ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">NAIR LUCCAS RIBEIRO ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ITANHAEM ETEC DE</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARIA AUGUSTA SARAIVA DRA ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PARQUE DA JUVENTUDE ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">BRASILIO FLORES DE AZEVEDO INSTITUTO TECNICO DE BARUERI</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MUNIR JOSE PROFESSOR INSTITUTO TECNICO DE BARUERI</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARIO ANTONIO VERZA PROF ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">WALDYR DURON JUNIOR ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ARACATUBA ETEC DE</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JUSCELINO KUBITSCHEK DE OLIVEIRA ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ITAQUERA ETEC DE</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">FERRAZ DE VASCONCELOS ETEC DE</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">SAPOPEMBA ETEC DE</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CUBATAO ETEC DE</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">VARGEM GRANDE DO SUL ETEC DE</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ARY DE CAMARGO PEDROSO ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ELIAS MIGUEL JUNIOR PROFESSOR ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">RUTH CARDOSO DOUTORA ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">GINO REZAGHI ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">VILA FORMOSA ETEC DE</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">TEREZA APARECIDA CARDOSO NUNES DE OLIVEIRA ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ERMELINDA GIANNINI TEIXEIRA PROFA ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">SAO JOSE DOS CAMPOS ETEC DE</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">SUZANO ETEC DE</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">SAO SEBASTIAO ETEC DE</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MONTE MOR ETEC DE</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CIDADE TIRADENTES ETEC DE</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PIEDADE ETEC DE</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">TAKASHI MORITA ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JADYR SALLES PROFESSOR ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CAMPO LIMPO PAULISTA ETEC DE</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ADHEMAR BATISTA HEMERITAS PROF ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">TIQUATIRA ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">POA ETEC DE</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">EURO ALBINO DE SOUZA ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ARNALDO PEREIRA CHEREGATTI ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOAO MARIA STEVANATTO ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CARAGUATATUBA ETEC DE</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARINES TEODORO DE FREITAS ALMEIDA PROFA ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">HELIOPOLIS ESCOLA TECNICA ESTADUAL</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">COTIA ESCOLA TECNICA ESTADUAL DE</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">SAO MATEUS ESCOLA TECNICA ESTADUAL</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">UIRAPURU ESCOLA TECNICA ESTADUAL</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JARDIM ANGELA ESCOLA TECNICA ESTADUAL</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">SANTA ISABEL ESCOLA TECNICA ESTADUAL DE</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JARAGUA ESCOLA TECNICA ESTADUAL</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">RAPOSO TAVARES ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PAULISTANO ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">PARQUE BELEM ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">GILDO MARCAL BEZERRA BRANDAO ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">FRANCISCO MORATO ETEC DE</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">OLIMPIA ETEC DE</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ABDIAS DO NASCIMENTO ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">NOVA ODESSA ETEC DE</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">HERCULES ALVES DE OLIVEIRA PROF INSTITUTO TECNICO DE BARUERI</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE IGNACIO AZEVEDO FILHO ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">GUSTAVO TEIXEIRA ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">SANTA ROSA DE VITERBO ETEC DE</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MAIRINQUE ETEC DE</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANTONIO ARANTES FILHO PROFESSOR INSTITUTO TECNICO DE BARUERI</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">REGISTRO ETEC DE</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ITARARE ETEC DE</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">OSASCO II ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CARLOS LEONCIO DA SILVA PADRE ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">IRMA AGOSTINA ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">NELSON ALVES VIANNA DR ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CERQUILHO ETEC DE</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CIDADE DO LIVRO ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ITAQUAQUECETUBA ETEC DE</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">EMBU ETEC DE</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MANDAQUI ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">BARUERI ETEC DE</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">DOROTI QUIOMI KANASHIRO TOYOHARA DRA PROF ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ALCIDES CESTARI ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">BENTO CARLOS BOTELHO DO AMARAL ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">DARCY PEREIRA DE MORAES ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">BRAZ PASCHOALIN PREFEITO ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MILTON GAZZETTI PROFESSOR ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">SYLVIO DE MATTOS CARVALHO PROF DR ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">SAO PAULO ETEC DE</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ADAIL NUNES DA SILVA DR ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">SALIM SEDEH DEPUTADO ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">SEBASTIANA AUGUSTA DE MORAES ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE LUIZ VIANA COUTINHO DR ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARCOS UCHOAS DOS SANTOS PENCHEL PROF ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">AMIM JUNDI ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOAO RAYS COMENDADOR ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ILHA SOLTEIRA ETEC DE</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ADOLPHO BEREZIN ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">COLEGIO TECNICO DE LORENA</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">COL TEC INDUSTRIAL PROF ISAAC PORTAL ROLDAN UNESP</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ZONA LESTE ETEC DA</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE DAGNONI DR PROF ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">HORTOLANDIA ETEC</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">SAO ROQUE ETEC DE</td>
<td style="text-align: left;">Escola Técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIANO DE OLIVEIRA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">SILVIO XAVIER ANTUNES PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ERMANO MARCHETTI</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">HUMBERTO DE SOUZA MELLO GENERAL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MANUEL DA NOBREGA PADRE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOAQUIM SILVADO DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JACOMO STAVALE PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANTONIO EMILIO SOUZA PENNA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ROMULO PERO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">PAULO EGYDIO DE OLIVEIRA CARVALHO SENADOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">NARBAL FONTES PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOAQUIM LEME DO PRADO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CASTRO ALVES</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CARLOS DE LAET PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANTONIO LISBOA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANTONIO VIEIRA PADRE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">HOMEM DE MELLO BARAO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">BUENOS AIRES</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CASIMIRO DE ABREU</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">SEBASTIAO DE SOUZA BUENO PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">SILVA JARDIM</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ALFREDO INACIO TRINDADE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">RUY BARBOSA CONSELHEIRO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOAO LIGABUE CONEGO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">AMENAIDE BRAGA DE QUEIROZ PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">SAO PAULO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">LOUREIRO JUNIOR PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">BENEDITO MATARAZZO DEPUTADO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">OSWALDO CRUZ</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">PLINIO BARRETO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">WOLNY CARVALHO RAMOS PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MMDC</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIO CASASSANTA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARIO MARQUES DE OLIVEIRA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">STEFAN ZWEIG</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">BRISABELLA ALMEIDA NOBRE PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE HEITOR CARUSI PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">AMERICO DE MOURA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE CHEDIAK</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JULIA MACEDO PANTOJA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MOACYR CAMPOS PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOAO DIAS DA SILVEIRA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">AMELIA DE ARAUJO DONA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">PAULO NOVAES DE CARVALHO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOAO BORGES PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">IRENE DE LIMA PAIVA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE MARQUES DA CRUZ PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ASCENDINO REIS PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">OSWALDO CATALANO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">GABRIEL ORTIZ PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JAMIL PEDRO SAWAYA PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOAO MARIA OGNO OSB DOM</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">NOSSA SENHORA DA PENHA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ADELAIDE FERRAZ DE OLIVEIRA PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA DE CARVALHO SENNE PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">INFANTE DOM HENRIQUE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE PEREIRA DE QUEIROZ DR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">VITAL FOGACA DE ALMEIDA DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">SILVA PRADO DEPUTADO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MIGUEL DE CERVANTES Y SAAVEDRA DOM</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIO KOZEL FILHO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ESTELA BORGES MORATO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CARLOS GOMES</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">DOM PEDRO I</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">DARIO DE QUEIROZ PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">DIOGO DE FARIA DR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ADHEMAR ANTONIO PRADO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ROMEU DE MORAES</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANHANGUERA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">PEREIRA BARRETO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CANUTO DO VAL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ZULEIKA DE BARROS MARTINS FERREIRA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE MONTEIRO BOANOVA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MAURO DE OLIVEIRA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MISS BROWNE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MANUEL CIRIDIAO BUARQUE PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">EMILIANO AUGUSTO CAVALCANTI DE ALBUQUERQUE E MELO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ALEXANDRE VON HUMBOLDT</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">FIDELINO FIGUEIREDO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">FERNAO DIAS PAES</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANTONIO ALVES CRUZ PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ARCY MAJOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">COSTA MANSO MINISTRO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">FABIANO LOZANO MAESTRO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">GODOFREDO FURTADO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CAETANO DE CAMPOS CONSOLACAO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARTIM FRANCISCO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ARISTIDES DE CASTRO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">NAPOLEAO DE CARVALHO FREIRE PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">OSWALDO ARANHA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">EMYGDIO DE BARROS PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ALBERTO LEVY PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ALBERTO TORRES</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANA ROSA DE ARAUJO DONA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ADOLFO GORDO SENADOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">VIRGILIA RODRIGUES ALVES DE CARVALHO PINTO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PEDRO FONSECA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MURTINHO NOBRE DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ITAUNA VISCONDE DE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ROOSEVELT PRESIDENTE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ALEXANDRE DE GUSMAO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">TEOTONIO ALVES PEREIRA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">RAUL FONSECA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARIA RIBEIRO GUIMARAES BUENO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CARLOS AUGUSTO DE FREITAS VILLALVA JUNIOR DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOAO AMOS COMENIUS</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">BRASILIO MACHADO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">DOMINGOS QUIRINO FERREIRA CORONEL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">RUI BLOEM</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">NEYDE APPARECIDA SOLLITTO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA PETRONILA LIMEIRA DOS MILAGRES MONTEIRO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">LEOPOLDO SANTANA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ZULMIRA CAVALHEIRO FAUSTINO DONA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ALBERTO CONTE PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">KENNEDY PRESIDENTE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ISALTINO DE MELLO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">SABOIA DE MEDEIROS PADRE EE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ALBERTO SALOTTI PROF EE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PAULINO NUNES ESPOSO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">DUARTE LEOPOLDO E SILVA DOM</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE VIEIRA DE MORAES PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ALFREDO VIANELLO GREGORIO COMENDADOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">VICENTE LEPORACE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOAO BATISTA DE CARVALHO MONSENHOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">BELEM DA SERRA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">WALTER RIBAS DE ANDRADE PROF EE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">OTTO WEISZFLOG</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">WALTHER WEISZFLOG</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">NIDE ZAIM CARDOSO PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CRISPINIANO CONSELHEIRO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">BRASILIA CASTANHO DE OLIVEIRA DONA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE ALVES DE CERQUEIRA CESAR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA LEONI</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANTONIO DE RE VEREADOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">FREDERICO DE BARROS BROTERO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JUVENAL RAMOS BARBOSA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PAULO ROLIM LOUREIRO DOM</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">FRANCISCO ANTUNES FILHO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ALICE CHUERY PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">HOMERO RUBENS DE SA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANTONIO VIANA DE SOUZA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">WASHINGTON LUIZ PEREIRA DE SOUZA DR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOAO CAVALHEIRO SALEM PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">AMADEU RODRIGUES NORTE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA SANTOS BAIRAO PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ADHEMAR BOLINA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">SENTARO TAKAOKA DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">PEDRO MALOZZE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">GABRIEL PEREIRA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">FRANCISCO FERREIRA LOPES</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">OLGA CHAKUR FARAH PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ELISIARIO PINTO DE MORAIS VEREADOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA RODRIGUES GONCALVES PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">WASHINGTON LUIZ DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">RAUL BRASIL PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">EE PROGRAMA DE ENSINO INTEGRAL EUSTAQUIO PADRE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ODILA LEITE DOS SANTOS PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">GERALDO JUSTINIANO DE REZENDE SILVA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CARLINDO REIS</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">SIMON SWITZAR PADRE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANTONIO BRANCO RODRIGUES JUNIOR PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">FILINTO MULLER SENADOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">FABIO EDUARDO RAMOS ESQUIVEL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">THEREZINHA SARTORI PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANTONIO MESSIAS SZYMANSKI PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">LUIS WASHINGTON VITA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">RUTH NEVES SANT ANNA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARILENE DE OLIVEIRA ACETTO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MAUA VISCONDE DE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">LEICO AKAISHI PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE GASPAR DOM</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ALVARO DE SOUZA VIEIRA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CELSO GAMA DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">LUIZ LOBO NETO DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PAULO VI PAPA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CARLOS DE CAMPOS DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">GENEROSO ALVES DE SIQUEIRA DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">NADIR LESSA TOGNINI PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">AMERICO BRASILIENSE DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">SERGIO MILLIET DA COSTA E SILVA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOAO GALEAO CARVALHAL SENADOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE CALVITTI FILHO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ONDINA RIVERA MIRANDA CINTRA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">WANDA BENTO GONCALVES PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOAO PAULO I PAPA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">AMARAL WAGNER</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CARLINA CACAPAVA DE MELLO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ADAMASTOR DE CARVALHO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">TAUNAY VISCONDE DE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">OSCAVO DE PAULA E SILVA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ARISTIDES GREVE PADRE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ESTHER MEDINA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">INAH DE MELLO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">FRANCISCO EMYGDIO PEREIRA NETO DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">FAUSTO CARDOSO FIGUEIRA DE MELLO DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">LAUDO FERREIRA DE CAMARGO MINISTRO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOAO FIRMINO CORREIA DE ARAUJO DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ROBERT KENNEDY SENADOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">FRANCISCO PRESTES MAIA ENGENHEIRO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ADAIL LUIZ MILLER DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">SANTA OLIMPIA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANTONIO NASCIMENTO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">BAETA NEVES DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE FORNARI DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MAURICIO ANTUNES FERRAZ PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">AMADEU OLIVERIO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA IRACEMA MUNHOZ</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOAO RAMALHO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">20 DE AGOSTO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">WALLACE COCKRANE SIMONSEN</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANESIA LOUREIRO GAMA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CYNIRA PIRES DOS SANTOS PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA TRUJILO TORLONI</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOANA MOTTA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">LAURA LOPES</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ALFREDO BURKART PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ALEXANDRE GRIGOLLI PADRE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">YOLANDA ASCENCIO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA DA CONCEICAO MOURA BRANCO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">BONIFACIO DE CARVALHO CORONEL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">IDALINA MACEDO COSTA SODRE DONA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">TOUFIC JOULIAN</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">VICTORIO FORNASARO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">WILLIAN RODRIGUES REBUA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PORCINO RODRIGUES PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MATILDE MARIA CREMM</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIANINHA QUEIROZ PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ODETTE DE SOUZA CARVALHO MADRE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PAULO CHAGAS NOGUEIRA ENGENHEIRO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">EULALIA MALTA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA AUXILIADORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">IRIA KUNZ IRMA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOAO CALY PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANTONIO INACIO MACIEL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ALMIR PEREIRA BAHIA REVERENDO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">PASCHOAL CARLOS MAGNO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ZEICY APPARECIDA NOGUEIRA BAPTISTA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">WANDYCK FREITAS JORNALISTA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">VICENTE THEMUDO LESSA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CLARO CAMARGO RIBEIRO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">VINICIUS DE MORAES</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CARLOS FERREIRA DE MORAES PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ORLANDO ELLERO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ZACARIAS ANTONIO DA SILVA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE BARRETO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">PAULO SOARES DA SILVA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE NEYDE CESAR LESSA DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ERNESTO THENN DE BARROS PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE MARIA RODRIGUES LEITE PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE LIBERATTI PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOAO BAPTISTA DE BRITO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ALICE VELHO TEIXEIRA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">GLORIA AZEDIA BONETTI PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">TELMO COELHO FILHO MAJOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANTONIO RAPOSO TAVARES</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">WALKIR VERGANI</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">EDUARDO CORREA DA COSTA JUNIOR DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">THOMAZ RIBEIRO DE LIMA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ALCIDES DE CASTRO GALVAO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MAISA THEODORO DA SILVA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">NAIR FERREIRA NEVES PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">RAQUEL DE CASTRO FERREIRA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">VICENTE DE CARVALHO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ARMANDO BELLEGARD PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">EDUARDO GOMES MARECHAL DO AR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE DA COSTA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">SAO LEOPOLDO VISCONDE DE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">LUIZA MACUCO DONA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">SUETONIO BITTENCOURT JUNIOR PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">FERNANDO DE AZEVEDO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PRIMO FERREIRA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CANADA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANTONIO ABLAS FILHO DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARQUES DE SAO VICENTE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">BENEDITO CALIXTO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JON TEODORESCO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ZULMIRA DE ALMEIDA LAMBERT PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JARDIM BOPEVA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">AUGUSTO PAES D AVILA REVERENDO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARTIM AFONSO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA PACHECO NOBRE PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">REYNALDO KUNTZ BUSCH DR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">VIRGILIO ANTUNES PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARIO DA SILVA PINTO DR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">AMERICO ALVES</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">PAULO VIRGINIO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PAULINA CARDOSO PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANDRE BROCA PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CHICO PADRE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANTONIO DA CRUZ PAYAO PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">FLAMINIO LESSA DR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">GABRIEL PRESTES</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JUCA PADRE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOAO MARTINS DE ALMEIDA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">THEODORO CORREA CINTRA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">RYOITI YASSUDA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ALFREDO PUJOL DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">AFFONSO DE CARVALHO DESEMBARGADOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ALCEU MAYNARD ARAUJO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ILZA IRMA MOELLER COPPIO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE VIEIRA MACEDO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANA CANDIDA DE BARROS MOLINA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOAQUIM FRANCO DE ALMEIDA CORONEL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CARLOS PORTO CORONEL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">POMPILIO MERCADANTE DR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE MARIOTTO FERREIRA MAJOR AVIADOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">EDUARDO JOSE DE CAMARGO CORONEL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">FRANCISCO PEREIRA DA SILVA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOAO CURSINO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CERQUEIRA CESAR DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CESAR COSTA DEPUTADO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOAO ALVES MONSENHOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOAO GONCALVES BARBOSA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JACQUES FELIX</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">AMALIA GARCIA RIBEIRO PATTO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">BERNARDINO QUERIDO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MONTEIRO LOBATO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">URBANO ALVES DE SOUZA PEREIRA ENGENHEIRO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANTONIO MAGALHAES BASTOS</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARIO CARDOSO FRANCO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">NEWTON CAMARA LEAL BARROS</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">NASCIMENTO SATIRO DA SILVA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOAO ANTUNES ALEXANDRE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ELIAS LAGES DE MAGALHAES PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">REGINA DIAS ANTUNES DA SILVA PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">LUIZ DARLY GOMES DE ARAUJO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANTONIO LUIZ DUARTE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">PAULO ARAUJO NOVAES DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANTONIO TONON</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE LEITE PINHEIRO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE PENNA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">HOLAMBRA II</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MATILDE VIEIRA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">PEDRO TORRES PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ATILIO INNOCENTI PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">IVENS VIEIRA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PEIXOTO GOMIDE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">FERNANDO PRESTES CEL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ADHERBAL DE PAULA FERREIRA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ARLINDO VIEIRA PADRE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">FLORA PRESTES CESAR PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">LAZARO SOARES PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">EPAMINONDAS FERREIRA LOBO DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">HERCULANO PIMENTEL DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">NICOTA SOARES PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE VASQUES FERRARI PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ZULMIRA DE OLIVEIRA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">SANDRA REGINA PIRES PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CICERO SIQUEIRA CAMPOS PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANTONIO BERRETA PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">REGENTE FEIJO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">TANCREDO DO AMARAL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">VITORIO TOGNI CAPITAO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">HORACIO MANLEY LANE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">FREDERICO MARCICANO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">GERMANO NEGRINI PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">LURDES PENNA CARMELO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE ODIN DE ARRUDA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">GENESIO MACHADO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">EZEQUIEL MACHADO NASCIMENTO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">VERGUEIRO SENADOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JULIO PRESTES DE ALBUQUERQUE DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">FRANCISCO EUPHRASIO MONTEIRO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOAO CLIMACO DE CAMARGO PIRES</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">BRIGADEIRO TOBIAS</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ARTHUR CYRILLO FREIRE DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">AGGEO PEREIRA DO AMARAL PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE REGINATO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JULIO BIERRENBACH LIMA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">LUIZ GONZAGA DE CAMARGO FLEURY PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">OSSIS SALVESTRINI MENDES PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANTONIO MIGUEL PEREIRA JUNIOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">LUIZ NOGUEIRA MARTINS SENADOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">FRANCISCO COCCARO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANTONIO PADILHA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">PLINIO RODRIGUES DE MORAIS</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ALTINA MAYNARDES ARAUJO PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ALDO ANGELINI</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">LUIZ CAMPACCI</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">RENATO ANGELINI PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANTONIETA FERRARESE PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE ERMIRIO DE MORAES SENADOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ODILON BATISTA JORDAO VEREADOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANCHIETA PADRE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">DANIEL VERANO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">AFONSO VERGUEIRO DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JAYME DE BARROS CAMARA DOM</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ULISSES DE OLIVEIRA VALENTE PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">LUIZ ALVES CEL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ARY MENEGATTO PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOAO XXIII</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">EMILIO ROMI COMENDADOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOAO THIENNE DR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">FRANCISCO TOZZI DR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOAO PEDRO DE GODOY MOREIRA CEL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CLODOVEU BARBOSA PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PEDRO DE TOLEDO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">IBRANTINA CARDONA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">FRANCISCO DA SILVEIRA FRANCO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">LUIZ LEITE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANTONIO CAIO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">VICENTE RIZZO DR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CELSO HENRIQUE TOZZI PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSEPHINA GALVAO DE FRANCA ANDREUCCI PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">NARCISO PIERONI</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE FRANCO CRAVEIRO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PAULO SILVA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOAO ERNESTO FIGUEIREDO CORONEL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOAO APOCALIPSE PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">FRANCISCO DEROSA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ALCINDO BUENO DE ASSIS MINISTRO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">FRANCISCO DE AGUIAR PECANHA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE ALVIM</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANTONIO ALVES ARANHA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">LUIS GONZAGA DE MOURA MONSENHOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">AMERICO BELLUOMINI PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CYRO DE BARROS REZENDE PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE VILAGELIN NETO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOAO LOURENCO RODRIGUES PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ADALBERTO PRADO E SILVA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ADALBERTO NASCIMENTO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOAO NERY DOM</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CARLOS GOMES</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANIBAL DE FREITAS PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CULTO A CIENCIA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">OROSIMBO MAIA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">LAIS BERTONI PEREIRA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">LUIZ GONZAGA DA COSTA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">GERALDO DE REZENDE BARAO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE MARIA MATOSINHO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JULIO MESQUITA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOAQUIM PEDROSO DE ALVARENGA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">HELENA DE CAMPOS CAMARGO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANTONIO VILELA JUNIOR PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ATALIBA NOGUEIRA BARAO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">DOM BARRETO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">FELIPE CANTUSIO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">HELIO CERQUEIRA LEITE PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE CARLOS NOGUEIRA REVERENDO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">FRANCISCO ALVARES PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">VITOR MEIRELLES</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">GILBERTO GIRALDI</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ALEXANDRE FLEMING</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">BARAO DE MONTE SANTO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">OSCAR VILLARES</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">EDUARDO VICENTE NASSER DEPUTADO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">FERNANDO MAGALHAES PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">FRANCISCO NAPOLEAO MAIA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">RAFAEL DE OLIVEIRA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">NATHANAEL SILVA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">GABRIEL PAULINO BUENO COUTO BISPO DOM</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANTENOR SOARES GANDRA DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ALBERTO FERREIRA REZENDE PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MANOEL JOSE DA FONSECA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE POLLI</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MANUEL EUCLIDES DE BRITO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CONDE DO PARNAIBA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ADONIRO LADEIRA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ELOY DE MIRANDA CHAVES DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">QUINZE DE OUTUBRO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ALBERTINA FORTAREL PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">DIOGENES DUARTE PAES</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JERONIMO DE CAMARGO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CESARIO COIMBRA DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PAULO DE ALMEIDA NOGUEIRA DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">VICENTE FERREIRA DOS SANTOS PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">FRANCISCO GRAZIANO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANTONIO PERCHES LORDELLO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANTONIO DE QUEIROZ PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">LAZARO DUARTE DO PATEO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ELY DE ALMEIDA CAMPOS PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">GABRIEL POZZI PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ARMANI PADRE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">LUIZ MARTINI</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">LEME CARDEAL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">AGENOR DE CARVALHO CAPITAO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">BENEDITO NASCIMENTO ROSAS PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">TIMOTHEO SILVA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ORESTES LADEIRA PE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">OSCAR RODRIGUES ALVES DR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CRISTIANO OSORIO DE OLIVEIRA CORONEL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">DOMINGOS THEODORO DE OLIVEIRA AZEVEDO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">TEOFILO DE ANDRADE DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">EGLE LUPORINI COSTA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA JANUARIA VAZ TUCCORI PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">FABIANO JOSE MOREIRA CAMARGO PADRE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ELIAS DE MELLO AYRES PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANTONIO DE MELLO COTRIM PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MANOEL FERRAZ PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">PEDRO DE MELLO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">RIO BRANCO BARAO DO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">PEDRO MORAES CAVALCANTI</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">OLIVIA BIANCO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">SUD MENNUCCI</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MANOEL DA COSTA NEVES PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JORGE COURY DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">SAMUEL DE CASTRO NEVES DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">PEDRO CREM FILHO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANGELO FRANZIN</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">NOSSA SENHORA DE LORETO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PIRASSUNUNGA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARIA JOAQUINA DE ARRUDA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">LAURO BARREIRA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">PEDRO RAPHAEL DA ROCHA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JANIO QUADROS GOVERNADOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARCIANO DE TOLEDO PIZA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOAO BATISTA LEME PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">LAZARO FRANCO DE MORAES</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MICHEL ANTONIO ALEM PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ODILON CORREA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">RAUL FERNANDES CHANCELER</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE LEVY CORONEL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JAMIL ABRAHAO SAAD</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">DINAH LUCIA BALESTRERO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARCELINO BRAGA CEL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">VICTOR LACORTE PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PEDRO JOSE NETO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ABDALLA MIGUEL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">LETICIA DE GODOY BUENO DE CARVALHO LOPES PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">BENEDITO PEREIRA CARDOSO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ENOCH GARCIA LEAL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ALMEIDA PINTO CORONEL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ALEXANDRE DE AVILA BORGES</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">GALDINO DE CASTRO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ALICE FONTOURA DE ARAUJO DONA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ZEZINHO PORTUGAL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MACEDO SOARES EMBAIXADOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARIA FALCONI DE FELICIO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">BENEDITO ORTIZ CORONEL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ABILIO MANOEL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ORMINDA GUIMARAES COTRIM</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ELISIO DE CASTRO DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">DOMINGOS PARO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">NENA GIANNASI BUCK PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PARAISO CAVALCANTI DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOAO MARCIANO DE ALMEIDA DR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CARMEM MUNHOZ COELHO PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANA MARIA JUNQUEIRA PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOAO DE FARIA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANTONIO BARREIROS PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">DAVID CARNEIRO EWBANK</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">WASHINGTON LUIZ DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MACARIO DE ALMEIDA CONEGO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">TORQUATO CALEIRO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">OLIVIO PEIXOTO PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE RIBEIRO DE BARROS PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIO D ELIA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">FABIO JOSE DE ARAUJO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANTONIO JUSTINO FALLEIROS CAPITAO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ESTEVAM FERRI PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOAQUIM BATISTA DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">BRUNO PIERONI PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">WINSTON CHURCHILL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE LUIZ DE SIQUEIRA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANTONIO FURLAN JUNIOR DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JEREMIAS DE PAULA EDUARDO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ROSA MARI DE SOUZA SIMIELLI PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">BARROS CONEGO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE ALEIXO DA SILVA PASSOS CORONEL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ALBERTO SANTOS DUMONT</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">WALTER FERREIRA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ALBERTO JOSE GONCALVES DOM</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIO LINS DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE COSTA DEPUTADO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">FRANCISCO DA CUNHA JUNQUEIRA DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">GUIMARAES JUNIOR DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">SEBASTIAO FERNANDES PALMA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CID DE OLIVEIRA LEITE PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">OTONIEL MOTA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">TOMAS ALBERTO WHATELLY DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MESSIAS DA FONSECA DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">VIRGILIO GARCIA CAPITAO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">FRANCISCO GOMES PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">NELSON FERNANDES</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">FRANCISCO MATARAZZO CONDE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">AGENOR MEDEIROS PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ABEL DOS REIS</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">SEBASTIAO DE OLIVEIRA ROCHA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JESUINO DE ARRUDA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE JULIANO NETO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ALVARO GUIAO DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ARLINDO BITTENCOURT PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA CAROLINA DE LIMA DONA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MANOEL GOUVEIA DE LIMA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">FRANCISCO SALES DE ALMEIDA LEITE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">GASTAO LIBERAL PINTO DOM</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANTONIO MORAES BARROS DR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE INOCENCIO DA COSTA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">VICTOR MAIDA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANGELO MARTINO PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOAO CAETANO DA ROCHA PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">VALENTIM GENTIL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JORGE MATTAR PADRE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CELIA PRIMO CALIL PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">EDUARDO VELHO FILHO PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">SEBASTIAO INOC ASSUMPCAO PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MORAIS PACHECO PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CAROLINA LOPES DE ALMEIDA PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE APARECIDO GUEDES DE AZEVEDO PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOAQUIM RODRIGUES MADUREIRA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CHRISTINO CABRAL PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANCHIETA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">NEUSA CESTARI FABRI PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">IDALINA VIANNA FERRO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">EDIR HELEN SGAVIOLI FACCIOLI PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ERASTO CASTANHO DE ANDRADE PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">DOMINGOS DE MAGALHAES DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">LOPES RODRIGUES DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">EPHIGENIA CARDOSO MACHADO FORTUNATO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">LEONINA ALVES CONEGLIAN PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PAULO ZILLO DR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">GERALDO PEREIRA DE BARROS DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ARACY SANTINHO BARBERI PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOAO BATISTA RIBEIRO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">FERNANDO VALEZI</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ORLANDO DONDA PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">FERNANDO COSTA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">OCTACILIO SANT ANNA PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ALFREDO PUJOL DR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">HENRIQUE MOURAO DOM</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">21 DE ABRIL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">PASCHOAL FLAMINO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ELZIRA GARBINO PAGANI PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE EGEA PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">NESTOR SAMPAIO BITTENCOURT DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANTONIO MAXIMIANO RODRIGUES</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ALFREDO MINERVINO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">NICOLA MASTROCOLA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PAULO DE LIMA CORREA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOAQUIM ANTONIO PEREIRA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE BRANDINI</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CARLOS BAROZZI</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARILENE DE LURDES LISBOA SINGH PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">AFONSO CAFARO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">SILVIO MIOTTO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">DATHAN CERVO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PASCHOAL CASTREQUINI PREFEITO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">LIBERO DE ALMEIDA SILVARES</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">DONATO MARCELO BALBO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">BAPTISTA DOLCI</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">LESBINO DE SOUZA ALKIMIN</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">EUPHLY JALLES DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE RIBEIRO PREFEITO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ARTUR HORSTHUIS DOM</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">AKIO SATORU PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE DOS SANTOS</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JUVENAL GIRALDELLI</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">SEVERINO REINO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">GABRIEL COZZETTO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOAO BAPTISTA TEIXEIRA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANTONIO TEIXEIRA DOS SANTOS</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">NICOTA DE SOUZA DONA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PEDRO BRANDAO DOS REIS</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">GENTILA GUIZZI PINATTI</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PORFIRIO PIMENTEL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">NOVA LUZITANIA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE ZANOVELLI</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE FLORENCIO DO AMARAL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PEDRO PEDROSA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">GUINES AFFONSO MORALES PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANTONIO MARIN</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">DESOLINA BETTI GREGORIN PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">BENTO DE SIQUEIRA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">SHIRLEY CAMARGO VON ZUBEN PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIO FLORENCE PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANITA COSTA DONA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA UBALDINA DE BARROS FURQUIM PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE ANTONIO SANTANA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">HORACIO ANTONIO DO NASCIMENTO CAPITAO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ELMIRA GOULART PEREIRA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA DAS DORES FERREIRA DA ROCHA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE JOAQUIM DOS SANTOS PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANTONIO MARIN CRUZ</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CORIPHEU DE AZEVEDO MARQUES</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">EDMUR NEVES PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ALBERTO ANDALO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">AUREA DE OLIVEIRA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">GONCALVES MONSENHOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PIO X</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">VICTOR BRITTO BASTOS PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">LEME CARDEAL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">AMIRA HOMSI CHALELLA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">GENARO DOMARCO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">PEDRO ELIAS PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CARMO TURANO VOLUNTARIO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JUSTINO JERRY FARIA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JAMIL KHAUAN PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE FELICIO MIZIARA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">GERALDO ALVES MACHADO PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE ABRAO MELHEM</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CICERO BARBOSA LIMA JUNIOR PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JARDIM RIVIERA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">UZENIR COELHO ZEITUNE PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CECILIA MEIRELES</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">NOEMIA DIAS PEROTTI DONA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">AUGUSTO MARIANI DR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">EDGAR RAIMUNDO DA COSTA DR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CESARE TOPPINO PADRE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PAULO GRASSI BONILHA DR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JUVENTINO NOGUEIRA RAMOS</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ARMEL MIRANDA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOAO BREMBATTI CALVOSO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARILENA SANTANA CORREA FERNANDES PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">LUIZ GAMA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">LICOLINA VILLELA REIS ALVES PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CLOVIS DE ARRUDA CAMPOS DR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">NILCE MAIA SOUTO MELO PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE AUGUSTO LOPES BORGES PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MANOEL BENTO DA CRUZ</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">VITOR ANTONIO TRINDADE PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOAO BATISTA BOTELHO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">PURCINA ELISA DE ALMEIDA PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JORGE CORREA PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">GENESIO DE ASSIS PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOAO ARRUDA BRASIL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">STELIO MACHADO LOUREIRO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ALVARO ALVIM</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">OSWALDO JANUZZI PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PIO ANTUNES DE FIGUEIREDO DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANTONIO KASSAWARA KATUTOK</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ENZO BRUNO CARRAMASCHI PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">OCTAVIANO CARDOSO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CARLOS SAMPAIO FILHO DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">DIOGO GARCIA MARTINS EXPEDICIONARIO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA EUNICE MARTINS FERREIRA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">YONE DIAS DE AGUIAR PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE CARLOS DA SILVA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">FRANCISCO ANTONINO PREFEITO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CINELZIA LORENCI MARONI PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE FLORENTINO DE SOUZA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MANOEL DOS SANTOS</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MITSUSADA UMETANI DR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">DECIO PRATA PREFEITO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARIA PEREIRA DE BRITO BENETOLI PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">TEREZA VALVERDE CARDOSO TIRAPELE PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">TONICO BARAO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CICERO CASTILHO CUNHA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOANITA BIANCHI BONSEGNO CARVALHO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">VANIR FERRERO MORAES PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">FRANCISCO SCHMIDT CEL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE EDSON MOYSES PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">GUILHERME BUZINARO PREFEITO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOEL AGUIAR PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">FLEURIDES CAVALLINI MENECHINO PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JULIETA GUEDES MENDONCA PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">9 DE JULHO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">OSCAR PEDROSO HORTA MINISTRO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOAO BRASIO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">SALVADOR RAMOS DE MOURA PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">TUPI PAULISTA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">IDENE RODRIGUES DOS SANTOS PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">OSVALDO MARTINS</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">FERNANDO COSTA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARIA LUIZA FORMOZINHO RIBEIRO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CELESTINA DE CAMPOS TOLEDO TEIXEIRA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">FILOMENA SCATENA CHRISTOFANO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MIGUEL OMAR BARRETO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">HUGO MIELE PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANGELICA DE OLIVEIRA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">PEDRO TOFANO VEREADOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">TANNEL ABBUD COMENDADOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE FOZ DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIETTA FERRAZ DE ASSUMPCAO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">FLORIVALDO LEAL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">SARRION MONSENHOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ROSA FRANCISCA MANO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE SANCHES POSTIGO DEPUTADO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANTONIO MARINHO DE CARVALHO FILHO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ISABEL CAMPOS DOUTORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">18 DE JUNHO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANTONIO DE CARVALHO LEITAO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ALFREDO MARCONDES CABRAL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">SHIGUETOSHI YOSHIHARA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARABA PAULISTA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">SALVADOR MORENO MUNHOZ</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOAO PEREZ SANTOS</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ALBERTO SANTOS DUMONT</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOAO GOMES MARTINS CORONEL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANTONIO DE ALMEIDA PRADO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">OLGA YASUKO YAMASHITA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">GILDASIO SILVA LIMA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MOACYR TEIXEIRA DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA ERNESTINA NATIVIDADE ANTUNES PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">FRANCISCO WHITACKER CORONEL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">IVO LIBONI PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">LIRIA YURICO SUMIDA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">LUCIA SILVA DE ASSUMPCAO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARIA JOSE BARBOSA CASTRO TOLEDO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">TAKAKO SUZUKI PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">FELICIO TARABAY DEPUTADO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CARLOS BERNARDES STAUT</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">HEMILSON CARLOS MAGRINI PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ALFREDO WESTIN JUNIOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">KOSUKE ENDO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ALICE MACIEL SANCHES PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE QUIRINO CAVALCANTE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">OSWALDO RANAZZI PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ZULENKA RAPCHAN PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANTONIO FONTANA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CLAUDIO DE SOUZA DR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE GONCALVES DE MENDONCA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">RACHID JABUR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOAQUIM GONCALVES DE OLIVEIRA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANTONIO DE BENEDICTIS PROF DR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">TEOFILO ELIAS PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANTONIO JOSE DOS SANTOS DOM</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA MAGDALENA DE OLIVEIRA DONA COTA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CAROLINA FRANCINI BURALI DONA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CLEOPHANIA GALVAO DA SILVA PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">LOURDES PEREIRA PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CLYBAS PINTO FERRAZ DR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CARLOS ALBERTO DE OLIVEIRA PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ISIDORO BAPTISTA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ERMELINDA CLARICE SANCHES PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">EDUARDO DE SOUZA PORTO CEL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">AMILCARE MATTEI PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANTONIO AUGUSTO NETTO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">BALTAZAR DE GODOY MOREIRA PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE JOAQUIM BITTENCOURT CEL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">HORACIO SOARES</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">FRANCISCO DUARTE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARIO BRIATORE PADRE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ESMERALDA SOARES FERRAZ PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARIA DO CARMO ARRUDA DA SILVA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JUSTINA DE OLIVEIRA GONCALVES PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">THEODORICO DE OLIVEIRA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">NICOLA MARTINS ROMEIRA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE AUGUSTO DE OLIVEIRA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOAO GOBBO SOBRINHO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">LEONIDAS DO AMARAL VIEIRA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CALVINO BARBOSA FERRAZ</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOAQUIM GUILHERME MOREIRA PORTO DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">QUINZINHO CAMARGO PREFEITO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE TROMBI MONSENHOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARCOS RIBEIRO CORONEL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MIGUEL MARVULLO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ATALIBA LEONEL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">GENESIO BOAMORTE DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">AUDA MALTA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">INDIA VANUIRE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">AGUIA DE HAIA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JEREMIAS JUNIOR CORONEL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ITARIRI</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ARMANDO GONCALVES PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ALICE RODRIGUES MOTTA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">RUY PRADO DE MENDONCA FILHO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">KOKI KITAJIMA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">PLACIDO DE PAULA E SILVA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">YOLANDA ARAUJO SILVA PAIVA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANTONIO FIGUEIREDO NAVAS COMENDADOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA DOLORES VERISSIMO MADUREIRA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOAQUIM ANDRADE MEIRELLES PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JUVENAL MACHADO DE ARAUJO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ALEXANDRE RODRIGUES NOGUEIRA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">BATISTA RENZI</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">OCTALLES MARCONDES FERREIRA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA HILDA ORNELAS DE OLIVEIRA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">AURELIANO MENDONCA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA LUIZA FERREIRA ZAMBELLO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">LONGINO VASTBINDER PADRE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">NUCLEO HABITACIONAL JOSE PAULINO NOGUEIRA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">EUCLIDES MIRANDA VEREADOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">DEOLINDA COPELLI DE SOUZA LIMA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">URUBUPUNGA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PERCIO PUCCINI PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">EULALIA SILVA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ADAIL MALMEGRIM GONCALVES PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">HONORINO FABBRI DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">DIOGENES ALMEIDA MARINS PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">LEONARDO SOARES RODRIGUES</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ARY BOUZAN PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">BRANCA CASTRO CANTO E MELO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">TADAKIYO SAKAI</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">LAERTE RAMOS DE CARVALHO PROF DR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANA SIQUEIRA DA SILVA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MILTON DA SILVA RODRIGUES PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">LUCIANO GUIDOTTI COMENDADOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">TEREZINHA MARIANO MAGNANI PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">AUGUSTO DO AMARAL DEPUTADO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE MARIA WHITAKER DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE LINS DO REGO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">IVAN BRASIL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ERVIN HORVATH DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOAO PAULO II</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA CRISTINA SCHMIDT MIRANDA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE GERALDO VIEIRA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">DOMINGOS DE SOUZA PREFEITO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOAO PEDRO DO NASCIMENTO PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA IZABEL CRUZ PIMENTEL DONA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">SADAMITA IVASSAKI</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANTONIO DOS SANTOS PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">PEDRO NUNES ROCHA PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ELVIRA SILVA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">IBRAHIM NOBRE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">VLADIMIR HERZOG JORNALISTA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">FRANCISCO LOPES DE AZEVEDO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">IZABEL RODRIGUES GALVAO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">WILSON PRESTES MIRAMONTES PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">DORTI ZAMBELLO CALIL PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARIA NEIVA ABDELMASSIH JUSTO PROFESSORAA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOAO GUIDOTTI</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">NESTOR DE CAMARGO PREFEITO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">LEONICE DE AQUINO OLIVEIRA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">DOMINGOS MIGNONI</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">NEUZA DE OLIVEIRA PREVIDE PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOCENY VILLELA CURADO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ALLYRIO DE FIGUEIREDO BRASIL PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CLEOBULO AMAZONAS DUARTE PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARLENE CAMARGO RIBEIRO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JUAREZ TAVORA MARECHAL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">SANTA DALMOLIN DEMARCHI</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARIA CATHARINA COMINO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CARMEN MIRANDA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">BALNEARIO DAS PALMEIRAS</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE PINTO MARCONDES PESTANA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">NELSON DO NASCIMENTO MONTEIRO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ROQUE PASSARELLI PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">PERY GUARANY BLACKMAN PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">LUIZ CAMPO DALL ORTO SOBRINHO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">VITO CARMINE CERBASI PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE PIRES ALVIM</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">AUGUSTA DO AMARAL PECANHA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">SEBASTIAO RAMOS NOGUEIRA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ALZIRA DIAS DE TOLEDO PIZA PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CONDE DO PINHAL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ARMELINDO FERRARI</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">LYDIA HELENA FRANDSEN STUHR PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ESTER EUNICE ALMEIDA FARIA DE OLIVEIRA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CLOTILDE VEIGA DE BARROS PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANTONIO REGINATO PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE DA CONCEICAO HOLTZ PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">GERSON DE BARROS MARGARIDO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">OROZIMBO SOSTENA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">AZARIAS LEITE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PORTO PRIMAVERA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">AMACIO MAZZAROPI</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA APARECIDA DOS SANTOS FRANCO PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">DAVID NASSER JORNALISTA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">EURIPEDES SIMOES DE PAULA PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">OSWALDO MOREIRA DA SILVA PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA AUDENIR DE CARVALHO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">BAIRRO DAS PALMEIRAS</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MYRTHES THEREZINHA ASSAD VILLELA PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE CARLOS DA SILVA JUNIOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA APARECIDA DAMO FERREIRA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">DINORAH SILVA DOS SANTOS PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ROGERIO LAZARO TOCCHETON PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CLEMENTINO VIEIRA CORDEIRO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">FRANCISCO DE PAULA SANTOS PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">WALDEMAR SALGADO PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">NEUZA MARIA NAZATTO DE CARVALHO PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ROBERTO RODRIGUES DE AZEVEDO PASTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">AMELIA MASSARO PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ISRAEL SCHOBA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ORLANDO SIGNORELLI</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CARLOS AUGUSTO PATRICIO AMORIM PROF CTIG UNESP</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ESCOLA DE APLICACAO DA FACULDADE DE EDUCACAO DA USP</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">OLGA CURY</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">TERCIO MORAES PEREIRA REV</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">REPUBLICA DOMINICANA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ISMAEL DA SILVA JUNIOR PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">DULCE CESAR TAVARES PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">SEBASTIANA COSTA BITTENCOURT PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CESIDIO AMBROGI PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MASSANORI KARAZAWA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ELVIRA DE PARDO MEO MURARO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CELIO RODRIGUES ALVES</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOAO OMETTO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ARY LEITE PEREIRA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">LYSANIAS DE OLIVEIRA CAMPOS PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">HELIO PALERMO PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">DJANIRA VELHO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CLODONIL CARDOSO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ARY DE OLIVEIRA GARCIA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA CECILIA FERRAZ DE FREITAS PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">AYR PICANCO BARBOSA DE ALMEIDA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">DARCY SILVEIRA VAZ PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ELIAS ALVES DA COSTA BACHAREL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANTONIO PINTO DE ALMEIDA FERRAZ DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOANNA SPOSITO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ARLINDO SILVESTRE PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">COLONIA DOS PESCADORES</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">IZABEL DE ALMEIDA MARIN PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOAQUIM MENDES FELIZ</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">TANCREDO NEVES PRESIDENTE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">PEREIRA DE MATTOS DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOAO CRUZ PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARIA FRANCISCA DEOCLECIO ARRIVABENE PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CHRISTIANO MARQUES BONILHA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARIA DE OLIVEIRA LELLIS ITO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE SCALVI DE OLIVEIRA PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ADONIRAN BARBOSA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA APPARECIDA PINTO DA CUNHA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANTONIO DUTRA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANNA PASSAMONTI BALARDIN</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">FARID FAYAD PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">VERA BRAGA FRANCO GIACOMINI PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">SUELI DA SILVEIRA MARIN BATISTA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">DALVA VIEIRA ITAVO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MIRELLA PESCE DESIDERE PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MONICA BERNABE GARROTE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">BAIRRO BARRA DO AZEITE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JULIO CESAR D ELIA PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ALCINA DANTAS FEIJAO PROFA ESCOLA MUNICIPAL DE ENSINO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">EMEFM LINNEU PRESTES PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE EZEQUIEL SOUZA PROF EMEFM</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ACHILLES DE ALMEIDA DR EM</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">GETULIO VARGAS DR EM</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOAO SALTO EM</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">LEANDRO FRANCESCHINI DOUTOR ESCOLA MUNICIPAL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE DE ANCHIETA ESCOLA MUNICIPAL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JARDIM MONTESANO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIO BORELLI THOMAZ EMEFM</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">NICOLAU SAAD DR EM</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA AMALIA VOLPON DE FIGUEIREDO PROFA EM</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE JABUR PROFESSOR EM</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">LUIZ PARIDE SINELLI PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">LEONOR PINTO THOMAZ EM</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">FLAVIO DE SOUZA NOGUEIRA PROF EM</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">AGOSTINHO LIMA DE VILHENA PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">EMEFM DERVILLE ALLEGRETTI PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">TANCREDO DE ALMEIDA NEVES PRESIDENTE EM</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">HELIO DEL CISTIA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">SUELI APARECIDA SE ROSA PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">OSMAR PASSARELLI SILVEIRA PROFESSOR CEMEP</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ADELINO BORDIGNON EM</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANDRE FRANCO MONTORO GOVERNADOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">AMANCIA DIAS SAMPAIO PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIVALDO CARLOS DEGAN PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">FUNDACAO EDUCACIONAL DE SAO JOSE DO RIO PARDO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ESCOLA DE ENSINO MEDIO EDUCACAO PROFISSIONAL DA FUMEP COTIP</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">IRENE CAPORALI DE SOUZA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">NELSON ANTONIO DO NASCIMENTO JUNIOR PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JARDIM PRIMAVERA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARINA AMARANTE RIBEIRO VASQUES SANCHES PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">EMEFM GUIOMAR CABRAL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">EMEFM ANTONIO SAMPAIO VER</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">EMEFM DARCY RIBEIRO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA FERNANDES MACHADO DE OLIVEIRA COLEGIO MUNICIPAL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MANOEL JACOB CREMM COLEGIO MUNICIPAL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CID CHIARELLI PROF DA FUNDACAO EDUCACAO GUACUANA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">RICARDA DOS SANTOS BRANCO PROFA COLEGIO MUNICIPAL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ABELARDO MARQUES DA SILVA COLEGIO MUNICIPAL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">GASPAR DE GODOI COLACO TTE GAL COLEGIO MUNICIPAL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">VICENTE BASTOS PROF EM</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANACLETO DE CAMARGO PADRE COLEGIO MUNICIPAL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">REINALDO ASCENCIO SANTOS FERREIRA VER COLEGIO MUNICIPAL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">DIADEMA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">LOUIS BRAILLE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">TOM JOBIM COLEGIO MUNICIPAL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA THEODORA PEDREIRA DE FREITAS PROFA EEFMT</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">INSTITUTO FEDERAL DE SAO PAULO CAMPUS - BRAGANCA PAULISTA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">INSTITUTO FEDERAL DE SAO PAULO CAMPUS - SALTO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">IFSP - CAMPUS SAO JOAO DA BOA VISTA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">NEUSA MARIA DO BEM PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">VICENTE MINICUCCI PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">BAIRRO CRUZEIRO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">TERUKO UEDA YAMAGUTI PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA SYLVIA CHALUPPE MELLO PROFA ITB</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">IFSP - CAMPUS SAO ROQUE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">BRUNO FLORENZANO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JARDIM SAN DIEGO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">DINORATH DO VALLE PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">BAIRRO ENGENHEIRO MAIA II</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">NAIR OLEGARIO CAJUEIRO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">VILA ALBERTINA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MOACYR DOMINGOS SAVIO VERONEZI PROF ITB</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">DAGMAR RIBAS TRINDADE PROFESSORA EEFMT</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARLENE APARECIDA MAIA OLBERG PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">IFSP - CAMPUS VOTUPORANGA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">INSTITUTO FEDERAL DE SAO PAULO CAMPUS - CATANDUVA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">FEITICO DA VILA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOAQUIM PINTO MACHADO JUNIOR PROFESSOR MACHADINHO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">PRISCILA FERNANDES DA ROCHA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">SUELY MARIA CACAO AMBIEL BATISTA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">OSCAR NIEMEYER ARQUITETO EMEFM</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">BAIRRO DO EDEN</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">URIAS BRAGA COSTA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">IFSP - CAMPUS REGISTRO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANA FRANCO DA ROCHA BRANDO PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">AROLDO DONIZETTI LEITE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ADELMO FRANCISCO DA SILVA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JARDIM BUSCARDI</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">DOMINGOS BAUER LEITE POETA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA LEDA FERNANDES BRIGO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARIA APARECIDA RODRIGUES PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">SYLVIA DE PAULA LEITE BAUER</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">GUIOMAR CAMOLESI SOUZA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">GUALBERTO MOREIRA DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">DIMAS MOZART E SILVA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PAULINA ROSA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE PINHEIRO DE LACERDA CAPITAO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">SUELY MACHADO DA SILVA PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOAO PALMA GUIAO DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MIGUEL JORGE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOAO JORGE MARMORATO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">DAVID JOSE LUZ PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANTONIO GUEDES DE AZEVEDO PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CARLOTA FERNANDES DE SOUZA RODINI</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARIA JULIETA DE GODOI CARTEZANI PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">NEWTON OPPERMANN DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">OSCARLINA DE ARAUJO OLIVEIRA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ODILON LEITE FERRAZ</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">GENTIL DE CAMARGO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MASSAKO OSAWA HIRABAYASHI PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">IRENE MACHADO DE LIMA DONA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANTONIO PRATICI PREFEITO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ILSON GOMES PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">LUIS DOS SANTOS METALURGICO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANTONIO BRAZ GAMBARINI DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">IRMA CHARLITA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">BAIRRO DO ITAIM</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">RUTH COUTINHO SOBREIRO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">FRANCISCO PARENTE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CALHIM MANOEL ABUD</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">RUBENS PAIVA DEPUTADO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MIQUELINA CARTOLANO PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ESCOLA ESTADUAL ABILIO RAPOSO FERRAZ JUNIOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ORESTES ORIS DE ALBUQUERQUE PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARIA TEREZA DE SOUZA FALCARELI PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE PINTO DO AMARAL PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE PASCHOALICK PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JUDITH SANT ANA DIEGUES PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MOACYR SANTOS DE CAMPOS PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA ROSA NUCCI PACIFICO HOMEM PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MAGDALENA SANSEVERINO GROSSO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ZILDA COMEGNO MONTI PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ORIGENES LESSA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">DELCIO DE SOUZA CUNHA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">FRANCISCO CRISTIANO LIMA DE FREITAS</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">LIONS CLUBE CENTRO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">PAULO DE ARRUDA PENTEADO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA APARECIDA VERISSIMO MADUREIRA RAMOS PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">COTA LEONEL DONA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOAO RODRIGUES BUENO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARIA JOSE DE AGUIAR ZEPPELINI PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANA MARIA PAGIOSSI</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">EVARISTO FABRICIO PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">GABRIEL FELIX DO AMARAL PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARIA APARECIDA GALHARINI DOS SANTOS PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">LUCIA DE CASTRO BUENO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">FRANCISCO D AMICO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">EDGARD FRANCISCO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">DIB AUDI</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">WALKER DA COSTA BARBOSA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">VILA DO LAGO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA GONCALVES DA MOTTA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ISABEL CRISTINA FAVARO PALMA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">OLIMPIA FALCI DONA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARIO FRANCISCON</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">AFRANIO DE OLIVEIRA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">AIMONE SALA PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE NANTALA BADUE PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">AUGUSTO DE SOUZA SARDINHA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIO AVESANI PREFEITO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MIGUEL MALUHY COMENDADOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ALBERTO ALVES ROLLO DR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">FABIO JUNQUEIRA FRANCO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANDRE DONATONI</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">IGNEZ GIARETTA SGUERRA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">LUDGERO BRAGA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE BELUCIO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JURACI LIMA LUPO PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MAUD SA DE MIRANDA MONTEIRO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">SIDRONIA NUNES PIRES</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ODETE MARIA DE FREITAS</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">NEUSA FIGUEIREDO MARCAL PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARIA AUXILIADORA MARQUES PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PAULO COELHO DA SILVA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ITAJAHY FEITOSA MARTINS PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE STOROPOLI DEPUTADO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE NICOLAU PIRAGINE PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA JOSE MORAES SALLES PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">SILVIO DE CARVALHO PINTO JUNIOR DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">IVETE SALA DE QUEIROZ PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARIA APARECIDA PINTO DE ABREU MAGNO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">VILA TUPI</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">OSWALDO DOS SANTOS SOARES PROFESSOR DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">BAIRRO DOS PAES</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">GUIDO DIAS DE ALMEIDA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">VERA LUCIA TORRES RODRIGUES AFFONSO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">FARID EID</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">RIOLANDO CANNO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARIA VERA LOMBARDI SIQUEIRA PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ARTHUR RICCI MONSENHOR DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CONCEICAO DA COSTA NEVES DEPUTADA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">VICTOR GERALDO SIMONSEN</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CLARICE DE MAGALHAES CASTRO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">DINAH DE MORAES E SEIXAS PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ADELINA PASQUINO CASSIS PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JARDIM SAO JOAO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOAQUIM DE MOURA CANDELARIA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">IRIA BARBIERI VITA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">COMUNIDADE NOSSA SENHORA APARECIDA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">FABIO HACL PINOLA PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ROMEU ALBERTI DOM</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">SILES COLI PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">INALDO MANTA DESPORTISTA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CLELIA DE BARROS LEITE DA SILVA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CARMELA CHIARA GINEFRA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE LOPES VEREADOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">PAULINA DE MORAIS PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">OMAR DAIBERT REVERENDO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARIA APARECIDA FELIX PORTO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ESMERALDA MILANO MARONI PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">DEOLINDA MANEIRA SEVERO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANNA CALVO DE GODOY PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">AUGUSTO MELEGA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">LAURA DE MELLO FRANCO PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">BASILIO RODRIGUES DA SILVA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">BAIRRO CARMO MESSIAS</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">EURICO DA SILVA BASTOS DOUTOR PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">SAVINO CAMPIGLI</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ORLANDO PEREZ PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE MARCATO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CELIO LUIZ NEGRINI PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ALBERTO VELLONE PADRE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARIA PIA SILVA CASTRO PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA APARECIDA SALES MANREZA PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MIGUEL PIRES GODINHO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">FERNAO DIAS PAES LEME</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARIA REGINA DEMARCHI FANANI</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA DE LOURDES NASCIMENTO GUERREIRO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">GERACINA DE MENEZES SANCHES PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ESMERALDA LEONOR FURLANI CALAF PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE DINI</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">DISNEI FRANCISCO SCORNAIENCHI DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ZITA DE GODOY CAMARGO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">LENY BARROS DA SILVA PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANNA DE MELLO CASTRIANI PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ELISA DE CAMPOS LIMA NOVELLI DONA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANA CECILIA MARTINS PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ASA BRANCA DA SERRA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">LEONOR MENDES DE BARROS</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARCIA APARECIDA DA SILVA FARIA RIES PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOANA HELENA DE CASTILHO MARQUES PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ATTILIO DEXTRO PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">DUILIO MAZIERO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ARMANDO FALCONE PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JURACY NEVES DE MELLO FERRACCIU PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">VICENTE LUIS GROSSO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">BAIRRO JAGUARI</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA VIRGINIA MANSUR BIAGI PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARIA NIVEA COSTA PINTO FREITAS PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ZILAH FERREIRA VIAGI PASSARELLI DE CAMPOS PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANTONIO VIEIRA CAMPOS</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">OSMAR FRANCISCO DA CONCEICAO DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">FLAVIO DE CARVALHO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA DO CARMO RICCI VON ZUBEN PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CAROLINA MENDES THAME PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA ISABEL NEVES BASTOS PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">AYRTON SENNA DA SILVA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ANCHIETA PADRE</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ELISIO DE OLIVEIRA NEVES VEREADOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">NELSON MONTEIRO PALMA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">WILSON CAMARGO PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">MARIA ELISA DE OLIVEIRA PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">FRANCISCO PESSOA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ODECIO LUCKE PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE AYLTON FALCAO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">EDITH SILVEIRA DALMASO PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARCO ANTONIO PRUDENTE DE TOLEDO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">LUZIA BARUQUE KIRCHE PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">EDSON VIANEI ALVES PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">NICIA FABIOLA ZANUTTO GIRALDI PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">DEOCLES VIEIRA DE CAMARGO PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">IFSP - CAMPUS CUBATAO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JAIR TOLEDO XAVIER PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSEPHA PINTO CHIAVELLI PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">ANTONIO LUCAS</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">LUIZA HIDAKA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">HEITOR VILLA LOBOS MAESTRO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">CARAN APPARECIDO GONCALVES PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARIO COVAS JUNIOR GOVERNADOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">IFSP - CAMPUS SERTAOZINHO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CELIA RIBEIRO LANDIM PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ADENILSON DOS SANTOS FRANCO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">SERGIO VIEIRA DE MELLO DIPLOMATA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PARQUE PIRATININGA II</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CLAUDINEI GARCIA PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE CELSO DE MELLO PROF</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">JOSE PIRES DE CARVALHO DOUTOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JARDIM CANAA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">RITA DE CASSIA DA SILVA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">JOSE APPARECIDO MUNHOZ PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">CRISTIANE CHAVES MOREIRA BRAGA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">LEDA FELICE FERREIRA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">PARQUE MARAJOARA II</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">ROQUE IELO PROFESSOR</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">SONIA MARIA MASCHIO BAPTISTA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">PARQUE PAYOL</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">MARIA APPARECIDA MENDES SILVA LACERDA PROFESSORA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">DARCI LOPES PROFA</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="even">
<td style="text-align: left;">BAIRRO TURVO DOS ALMEIDAS</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
<tr class="odd">
<td style="text-align: left;">IFSP - CAMPUS SAO PAULO</td>
<td style="text-align: left;">Escola Não-técnica</td>
</tr>
</tbody>
</table>

s

    SP_tecnicas %>% 
      ggplot(aes(x = Tecnica)) +
      geom_bar()

![](a_files/figure-markdown_strict/grafico%20tecnicas,%20proporção-1.png)

omg

    SP_tecnicas %>% 
      filter(NU_MEDIA_MT > 600) %>% 
      ggplot(aes(x = Tecnica)) +
      geom_bar()

![](a_files/figure-markdown_strict/Se%20tecnicas%20são%20melhores-1.png)
