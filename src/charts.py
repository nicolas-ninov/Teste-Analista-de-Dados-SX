import pandas as pd
import matplotlib.pyplot as plt


# =====================================================
# CONFIGURAÇÕES
# =====================================================

DATA_PATH = "inputs/enem_2020_tratado.csv"
CHARTS_PATH = "docs/images"


# =====================================================
# LEITURA DOS DADOS
# =====================================================

df = pd.read_csv(DATA_PATH, sep=";")

presentes = df[df["AUSENTE"] == False]


# =====================================================
# DICIONÁRIOS DE MAPEAMENTO
# =====================================================

mapa_etnia = {
    0: "Não declarado",
    1: "Branca",
    2: "Preta",
    3: "Parda",
    4: "Amarela",
    5: "Indígena",
}

mapa_renda = {
    "A": "Sem renda",
    "B": "Até 1.045",
    "C": "1.045-1.567",
    "D": "1.567-2.090",
    "E": "2.090-2.612",
    "F": "2.612-3.135",
    "G": "3.135-4.180",
    "H": "4.180-5.225",
    "I": "5.225-6.270",
    "J": "6.270-7.315",
    "K": "7.315-8.360",
    "L": "8.360-9.405",
    "M": "9.405-10.450",
    "N": "10.450-12.540",
    "O": "12.540-15.675",
    "P": "15.675-20.900",
    "Q": ">20.900",
}

mapa_escolaridade = {
    "A": "Nunca estudou",
    "B": "Fund. Incompleto",
    "C": "Fund. Parcial",
    "D": "Fund. Completo",
    "E": "Ens. Médio",
    "F": "Superior",
    "G": "Pós-graduação",
    "H": "Não sabe",
}

mapa_competencias_redacao = {
    "NU_NOTA_COMP1": "Comp. 1 - Norma culta",
    "NU_NOTA_COMP2": "Comp. 2 - Compreensão",
    "NU_NOTA_COMP3": "Comp. 3 - Argumentação",
    "NU_NOTA_COMP4": "Comp. 4 - Coesão",
    "NU_NOTA_COMP5": "Comp. 5 - Intervenção",
}


print("Gerando gráficos...")


# =====================================================
# GRÁFICO 1 - MÉDIA POR DISCIPLINA
# =====================================================

media_por_disciplina = presentes[
    [
        "NU_NOTA_CN",
        "NU_NOTA_CH",
        "NU_NOTA_LC",
        "NU_NOTA_MT",
        "NU_NOTA_REDACAO",
    ]
].mean(axis=0)

plt.figure(figsize=(10, 6))
media_por_disciplina.plot(kind="bar")
plt.title("Média por disciplina - ENEM 2020")
plt.xlabel("Disciplina")
plt.ylabel("Média")
plt.tight_layout()
plt.savefig(f"{CHARTS_PATH}/media_por_disciplina.png")
plt.close()


# =====================================================
# GRÁFICO 2 - MÉDIA POR SEXO
# =====================================================

media_por_sexo = (
    presentes
    .groupby("TP_SEXO")["MEDIA_NOTAS"]
    .mean()
)

plt.figure(figsize=(8, 5))
media_por_sexo.plot(kind="bar")
plt.title("Média por sexo - ENEM 2020")
plt.xlabel("Sexo")
plt.ylabel("Média das notas")
plt.tight_layout()
plt.savefig(f"{CHARTS_PATH}/media_por_sexo.png")
plt.close()


# =====================================================
# GRÁFICO 3 - MÉDIA POR ETNIA/COR-RAÇA
# =====================================================

media_por_etnia = (
    presentes
    .groupby("TP_COR_RACA")["MEDIA_NOTAS"]
    .mean()
)

media_por_etnia.index = media_por_etnia.index.map(mapa_etnia)

plt.figure(figsize=(8, 5))
media_por_etnia.plot(kind="bar")
plt.title("Média por etnia - ENEM 2020")
plt.xlabel("Etnia")
plt.ylabel("Média das notas")
plt.tight_layout()
plt.savefig(f"{CHARTS_PATH}/media_por_etnia.png")
plt.close()


# =====================================================
# GRÁFICO 4 - TOP 10 MUNICÍPIOS POR MÉDIA
# =====================================================

media_por_municipio = (
    presentes
    .groupby("NO_MUNICIPIO_ESC")["MEDIA_NOTAS"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 6))
media_por_municipio.plot(kind="bar")
plt.title("Top 10 municípios por média - ENEM 2020")
plt.xlabel("Município")
plt.ylabel("Média das notas")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(f"{CHARTS_PATH}/media_por_municipio.png")
plt.close()


# =====================================================
# GRÁFICO 5 - MÉDIA POR RENDA FAMILIAR
# =====================================================

media_por_renda = (
    presentes
    .groupby("Q006")["MEDIA_NOTAS"]
    .mean()
)

media_por_renda.index = media_por_renda.index.map(mapa_renda)

plt.figure(figsize=(12, 6))
media_por_renda.plot(kind="bar")
plt.title("Média das notas por renda familiar - ENEM 2020")
plt.xlabel("Faixa de renda familiar")
plt.ylabel("Média das notas")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(f"{CHARTS_PATH}/media_por_renda.png")
plt.close()


# =====================================================
# GRÁFICO 6 - MÉDIA POR ESCOLARIDADE DA MÃE
# =====================================================

media_por_mae = (
    presentes
    .groupby("Q002")["MEDIA_NOTAS"]
    .mean()
)

media_por_mae.index = media_por_mae.index.map(mapa_escolaridade)

plt.figure(figsize=(12, 6))
media_por_mae.plot(kind="bar")
plt.title("Média das notas por escolaridade da mãe - ENEM 2020")
plt.xlabel("Escolaridade da mãe")
plt.ylabel("Média das notas")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(f"{CHARTS_PATH}/media_por_mae.png")
plt.close()


# =====================================================
# GRÁFICO 7 - MÉDIA POR ESCOLARIDADE DO PAI
# =====================================================

media_por_pai = (
    presentes
    .groupby("Q001")["MEDIA_NOTAS"]
    .mean()
)

media_por_pai.index = media_por_pai.index.map(mapa_escolaridade)

plt.figure(figsize=(12, 6))
media_por_pai.plot(kind="bar")
plt.title("Média das notas por escolaridade do pai - ENEM 2020")
plt.xlabel("Escolaridade do pai")
plt.ylabel("Média das notas")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(f"{CHARTS_PATH}/media_por_pai.png")
plt.close()


# =====================================================
# GRÁFICO 8 - MÉDIA POR COMPETÊNCIA DA REDAÇÃO
# =====================================================

media_por_competencia_redacao = presentes[
    [
        "NU_NOTA_COMP1",
        "NU_NOTA_COMP2",
        "NU_NOTA_COMP3",
        "NU_NOTA_COMP4",
        "NU_NOTA_COMP5",
    ]
].mean(axis=0)

media_por_competencia_redacao.index = media_por_competencia_redacao.index.map(
    mapa_competencias_redacao
)

plt.figure(figsize=(12, 6))
media_por_competencia_redacao.plot(kind="bar")
plt.title("Média por competência da redação - ENEM 2020")
plt.xlabel("Competência da redação")
plt.ylabel("Média")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(f"{CHARTS_PATH}/media_competencias_redacao.png")
plt.close()


# =====================================================
# GRÁFICO 9 - MATRIZ DE CORRELAÇÃO ENTRE NOTAS
# =====================================================

colunas_notas = [
    "NU_NOTA_CN",
    "NU_NOTA_CH",
    "NU_NOTA_LC",
    "NU_NOTA_MT",
    "NU_NOTA_REDACAO",
]

nomes_notas = [
    "CN",
    "CH",
    "LC",
    "MT",
    "Redação",
]

correlacao_notas = presentes[colunas_notas].corr()

plt.figure(figsize=(8, 6))
plt.imshow(correlacao_notas)
plt.title("Matriz de correlação entre notas - ENEM 2020")
plt.xticks(
    ticks=range(len(nomes_notas)),
    labels=nomes_notas
)
plt.yticks(
    ticks=range(len(nomes_notas)),
    labels=nomes_notas
)
plt.colorbar(label="Correlação")

for i in range(len(nomes_notas)):
    for j in range(len(nomes_notas)):
        plt.text(
            j,
            i,
            f"{correlacao_notas.iloc[i, j]:.2f}",
            ha="center",
            va="center"
        )

plt.tight_layout()
plt.savefig(f"{CHARTS_PATH}/matriz_correlacao_notas.png")
plt.close()


print("Todos os gráficos foram gerados com sucesso!")

