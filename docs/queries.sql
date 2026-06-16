-- =====================================================
-- CONSULTAS SQL - ENEM 2020
-- Banco: enem
-- Tabela: enem_2020_tratado
-- =====================================================

USE enem;


-- =====================================================
-- 1. Total de inscritos
-- =====================================================

SELECT
    COUNT(*) AS total_inscritos
FROM enem_2020_tratado;


-- =====================================================
-- 2. Total de alunos presentes
-- =====================================================

SELECT
    COUNT(*) AS total_presentes
FROM enem_2020_tratado
WHERE AUSENTE = FALSE;


-- =====================================================
-- 3. Total de alunos ausentes
-- =====================================================

SELECT
    COUNT(*) AS total_ausentes
FROM enem_2020_tratado
WHERE AUSENTE = TRUE;


-- =====================================================
-- 4. Média geral dos alunos presentes
-- =====================================================

SELECT
    AVG(MEDIA_NOTAS) AS media_geral_presentes
FROM enem_2020_tratado
WHERE AUSENTE = FALSE;


-- =====================================================
-- 5. Aluno com maior média
-- =====================================================

SELECT
    NU_INSCRICAO,
    MEDIA_NOTAS
FROM enem_2020_tratado
WHERE AUSENTE = FALSE
ORDER BY MEDIA_NOTAS DESC
LIMIT 1;


-- =====================================================
-- 6. Média por sexo
-- =====================================================

SELECT
    TP_SEXO,
    AVG(MEDIA_NOTAS) AS media_por_sexo
FROM enem_2020_tratado
WHERE AUSENTE = FALSE
GROUP BY TP_SEXO
ORDER BY media_por_sexo DESC;


-- =====================================================
-- 7. Média por etnia/cor-raça
-- =====================================================

SELECT
    TP_COR_RACA,
    AVG(MEDIA_NOTAS) AS media_por_etnia
FROM enem_2020_tratado
WHERE AUSENTE = FALSE
GROUP BY TP_COR_RACA
ORDER BY media_por_etnia DESC;


-- =====================================================
-- 8. Média por disciplina
-- =====================================================

SELECT
    AVG(NU_NOTA_CN) AS media_cn,
    AVG(NU_NOTA_CH) AS media_ch,
    AVG(NU_NOTA_LC) AS media_lc,
    AVG(NU_NOTA_MT) AS media_mt,
    AVG(NU_NOTA_REDACAO) AS media_redacao
FROM enem_2020_tratado
WHERE AUSENTE = FALSE;


-- =====================================================
-- 9. Top 10 municípios por média
-- Observação: a base não possui CO_ESCOLA ou NO_ESCOLA.
-- Por isso, esta consulta é uma visão complementar por município.
-- =====================================================

SELECT
    NO_MUNICIPIO_ESC,
    AVG(MEDIA_NOTAS) AS media_municipio
FROM enem_2020_tratado
WHERE AUSENTE = FALSE
  AND NO_MUNICIPIO_ESC IS NOT NULL
GROUP BY NO_MUNICIPIO_ESC
ORDER BY media_municipio DESC
LIMIT 10;


-- =====================================================
-- 10. Média por sexo e etnia
-- =====================================================

SELECT
    TP_SEXO,
    TP_COR_RACA,
    AVG(MEDIA_NOTAS) AS media
FROM enem_2020_tratado
WHERE AUSENTE = FALSE
GROUP BY TP_SEXO, TP_COR_RACA
ORDER BY TP_SEXO, media DESC;


-- =====================================================
-- 11. Média por renda familiar
-- Q006 representa a faixa de renda familiar.
-- =====================================================

SELECT
    Q006,
    AVG(MEDIA_NOTAS) AS media_por_renda
FROM enem_2020_tratado
WHERE AUSENTE = FALSE
  AND Q006 IS NOT NULL
GROUP BY Q006
ORDER BY Q006;


-- =====================================================
-- 12. Média por escolaridade da mãe
-- Q002 representa a escolaridade da mãe.
-- =====================================================

SELECT
    Q002,
    AVG(MEDIA_NOTAS) AS media_por_escolaridade_mae
FROM enem_2020_tratado
WHERE AUSENTE = FALSE
  AND Q002 IS NOT NULL
GROUP BY Q002
ORDER BY Q002;


-- =====================================================
-- 13. Média por escolaridade do pai
-- Q001 representa a escolaridade do pai.
-- =====================================================

SELECT
    Q001,
    AVG(MEDIA_NOTAS) AS media_por_escolaridade_pai
FROM enem_2020_tratado
WHERE AUSENTE = FALSE
  AND Q001 IS NOT NULL
GROUP BY Q001
ORDER BY Q001;


-- =====================================================
-- 14. Média por acesso à internet
-- Q025 representa se o candidato possui acesso à internet.
-- =====================================================

SELECT
    Q025,
    AVG(MEDIA_NOTAS) AS media_por_acesso_internet
FROM enem_2020_tratado
WHERE AUSENTE = FALSE
  AND Q025 IS NOT NULL
GROUP BY Q025
ORDER BY Q025;


-- =====================================================
-- 15. Média das competências da redação
-- =====================================================

SELECT
    AVG(NU_NOTA_COMP1) AS media_comp1,
    AVG(NU_NOTA_COMP2) AS media_comp2,
    AVG(NU_NOTA_COMP3) AS media_comp3,
    AVG(NU_NOTA_COMP4) AS media_comp4,
    AVG(NU_NOTA_COMP5) AS media_comp5
FROM enem_2020_tratado
WHERE AUSENTE = FALSE;