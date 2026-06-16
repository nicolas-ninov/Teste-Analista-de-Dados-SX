import pandas as pd


# =====================================================
# CONFIGURAÇÕES
# =====================================================

DATA_PATH = "inputs/enem_2020_tratado.csv"
OUTPUT_PATH = "outputs/indicadores.txt"


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


# =====================================================
# INDICADORES GERAIS
# =====================================================

total_inscritos = len(df)

percentual_ausentes = df["AUSENTE"].mean() * 100

media_geral = presentes["MEDIA_NOTAS"].mean()

maior_media = presentes["MEDIA_NOTAS"].max()

aluno_maior_media = presentes[
    presentes["MEDIA_NOTAS"] == maior_media
]


# =====================================================
# INDICADORES AGRUPADOS
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

media_por_sexo = (
    presentes
    .groupby("TP_SEXO")["MEDIA_NOTAS"]
    .mean()
    .sort_values(ascending=False)
)

media_por_etnia = (
    presentes
    .groupby("TP_COR_RACA")["MEDIA_NOTAS"]
    .mean()
    .sort_values(ascending=False)
)

media_por_municipio = (
    presentes
    .groupby("NO_MUNICIPIO_ESC")["MEDIA_NOTAS"]
    .mean()
    .sort_values(ascending=False)
)

melhor_municipio = media_por_municipio.index[0]
melhor_media_municipio = media_por_municipio.iloc[0]


# =====================================================
# FUNÇÃO DE REGISTRO
# =====================================================

linhas = []


def registrar(texto=""):
    print(texto)
    linhas.append(texto)


# =====================================================
# RESPOSTAS DO TESTE
# =====================================================

registrar("=" * 60)
registrar("RESPOSTAS DAS PERGUNTAS")
registrar("=" * 60)

registrar("\n1 - Escola com maior média:")
registrar(
    "OBS: A base oficial disponibilizada para o teste não possui "
    "identificador único ou nome da instituição de ensino "
    "(CO_ESCOLA ou NO_ESCOLA)."
)
registrar(
    "Por esse motivo, optou-se por não inferir uma resposta incorreta "
    "a partir dos dados disponíveis."
)
registrar(
    f"\nInformação complementar: Município com maior média: "
    f"{melhor_municipio} | Média: {melhor_media_municipio:.2f}"
)

registrar("\n2 - Aluno(s) com maior média:")

for inscricao, media in aluno_maior_media[
    ["NU_INSCRICAO", "MEDIA_NOTAS"]
].values:
    registrar(f"Inscrição: {int(inscricao)} | Média: {media:.2f}")

registrar("\n3 - Média geral:")
registrar(f"{media_geral:.2f}")

registrar("\n4 - Percentual de ausentes:")
registrar(f"{percentual_ausentes:.2f}%")

registrar("\n5 - Total de inscritos:")
registrar(str(total_inscritos))

registrar("\n6 - Média por disciplina:")

for disciplina, media in media_por_disciplina.items():
    registrar(f"{disciplina}: {media:.2f}")

registrar("\n7 - Média por sexo:")

for sexo, media in media_por_sexo.items():
    registrar(f"{sexo}: {media:.2f}")

registrar("\n8 - Média por etnia:")

for codigo, media in media_por_etnia.items():
    registrar(f"{mapa_etnia[codigo]}: {media:.2f}")


# =====================================================
# EXPORTAÇÃO DOS RESULTADOS
# =====================================================

with open(OUTPUT_PATH, "w", encoding="utf-8") as arquivo:
    arquivo.write("\n".join(linhas))