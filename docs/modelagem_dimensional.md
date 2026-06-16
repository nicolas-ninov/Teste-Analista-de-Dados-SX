# Modelagem Dimensional - ENEM 2020

## Objetivo

Organizar os dados tratados do ENEM 2020 em um modelo dimensional simples, separando os dados analíticos principais em uma tabela fato e tabelas dimensão.

## Tabela Fato

### fato_notas_enem

Representa o desempenho dos inscritos presentes no ENEM 2020.

Campos principais:

- id_inscricao
- nota_cn
- nota_ch
- nota_lc
- nota_mt
- nota_redacao
- nota_total
- media_notas
- id_sexo
- id_cor_raca
- id_municipio
- id_escola_tipo
- id_socioeconomico

## Dimensões

### dim_sexo

- id_sexo
- sexo

### dim_cor_raca

- id_cor_raca
- cor_raca

### dim_municipio_escola

- id_municipio
- municipio_escola
- uf_escola

### dim_escola_tipo

- id_escola_tipo
- tipo_escola

### dim_socioeconomico

- id_socioeconomico
- escolaridade_pai
- escolaridade_mae
- renda_familiar
- acesso_internet

## Observação sobre escola

A base oficial disponibilizada não contém identificador único ou nome da instituição de ensino, como CO_ESCOLA ou NO_ESCOLA. Por isso, não foi possível modelar uma dimensão de escola específica. Como alternativa, foi utilizada a dimensão de município da escola e tipo de escola.

## Desenho lógico

dim_sexo
    |
dim_cor_raca --- fato_notas_enem --- dim_municipio_escola
    |
dim_escola_tipo
    |
dim_socioeconomico