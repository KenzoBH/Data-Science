**Análise de Dados: Enem por escolas (2005 - 2015)**
====================================================

Introção, link:
<a href="https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem-por-escola" class="uri">https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem-por-escola</a>

    library(tidyverse)

    ## -- Attaching packages ---------------------------------------------------------- tidyverse 1.3.0 --

    ## v ggplot2 3.3.2     v purrr   0.3.4
    ## v tibble  3.0.2     v dplyr   1.0.0
    ## v tidyr   1.1.0     v stringr 1.4.0
    ## v readr   1.3.1     v forcats 0.5.0

    ## -- Conflicts ------------------------------------------------------------- tidyverse_conflicts() --
    ## x dplyr::filter() masks stats::filter()
    ## x dplyr::lag()    masks stats::lag()

    library(knitr)

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
