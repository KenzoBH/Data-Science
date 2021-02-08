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

    enem <- read.csv("MICRODADOS_ENEM_ESCOLA.csv", sep=';')
    head(enem)

    ##   NU_ANO CO_UF_ESCOLA SG_UF_ESCOLA CO_MUNICIPIO_ESCOLA NO_MUNICIPIO_ESCOLA
    ## 1   2007           11           RO             1100205         Porto Velho
    ## 2   2006           11           RO             1100205         Porto Velho
    ## 3   2005           11           RO             1100205         Porto Velho
    ## 4   2008           11           RO             1100205         Porto Velho
    ## 5   2007           11           RO             1100205         Porto Velho
    ## 6   2008           11           RO             1100205         Porto Velho
    ##   CO_ESCOLA_EDUCACENSO      NO_ESCOLA_EDUCACENSO TP_DEPENDENCIA_ADM_ESCOLA
    ## 1             11000058 CENTRO DE ENSINO CLASSE A                         4
    ## 2             11000058 CENTRO DE ENSINO CLASSE A                         4
    ## 3             11000058 CENTRO DE ENSINO CLASSE A                         4
    ## 4             11000058 CENTRO DE ENSINO CLASSE A                         4
    ## 5             11000171 CENTRO EDUCACIONAL MOJUCA                         4
    ## 6             11000171 CENTRO EDUCACIONAL MOJUCA                         4
    ##   TP_LOCALIZACAO_ESCOLA NU_MATRICULAS NU_PARTICIPANTES_NEC_ESP NU_PARTICIPANTES
    ## 1                     1           144                       NA              140
    ## 2                     1           184                       NA              139
    ## 3                     1           220                       NA              145
    ## 4                     1           186                       NA              171
    ## 5                     1            19                       NA               12
    ## 6                     1            33                       NA               13
    ##   NU_TAXA_PARTICIPACAO NU_MEDIA_CN NU_MEDIA_CH NU_MEDIA_LP NU_MEDIA_MT
    ## 1                   NA          NA          NA          NA          NA
    ## 2                   NA          NA          NA          NA          NA
    ## 3                   NA          NA          NA          NA          NA
    ## 4                   NA          NA          NA          NA          NA
    ## 5                   NA          NA          NA          NA          NA
    ## 6                   NA          NA          NA          NA          NA
    ##   NU_MEDIA_RED NU_MEDIA_OBJ NU_MEDIA_TOT INSE PC_FORMACAO_DOCENTE
    ## 1           NA           NA        69.03                       NA
    ## 2           NA           NA        57.82                       NA
    ## 3           NA           NA        64.83                       NA
    ## 4        72.16        60.02           NA                       NA
    ## 5           NA           NA        58.84                       NA
    ## 6        59.81        42.49           NA                       NA
    ##   NU_TAXA_PERMANENCIA NU_TAXA_APROVACAO NU_TAXA_REPROVACAO NU_TAXA_ABANDONO
    ## 1                  NA              91.9                8.1              0.0
    ## 2                  NA                NA                 NA               NA
    ## 3                  NA              86.5               12.4              1.1
    ## 4                  NA              90.3                9.7              0.0
    ## 5                  NA              74.2               21.0              4.8
    ## 6                  NA              79.1               17.9              3.0
    ##          PORTE_ESCOLA
    ## 1 Maior que 90 alunos
    ## 2 Maior que 90 alunos
    ## 3 Maior que 90 alunos
    ## 4 Maior que 90 alunos
    ## 5    De 1 a 30 alunos
    ## 6   De 31 a 60 alunos
