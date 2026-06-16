import pandas as pd


# =====================================================
# CONFIGURAÇÕES
# =====================================================

CSV_PATH = "dados/MICRODADOS_ENEM_2020.csv"
OUTPUT_PATH = "inputs/enem_2020_tratado.csv"


# =====================================================
# COLUNAS UTILIZADAS NA ANÁLISE
# =====================================================

COLUNAS = [
    "NU_INSCRICAO",
    "TP_SEXO",
    "TP_COR_RACA",
    "TP_ESCOLA",
    "NO_MUNICIPIO_ESC",
    "SG_UF_ESC",
    "TP_PRESENCA_CN",
    "TP_PRESENCA_CH",
    "TP_PRESENCA_LC",
    "TP_PRESENCA_MT",
    "NU_NOTA_CN",
    "NU_NOTA_CH",
    "NU_NOTA_LC",
    "NU_NOTA_MT",
    "NU_NOTA_COMP1",
    "NU_NOTA_COMP2",
    "NU_NOTA_COMP3",
    "NU_NOTA_COMP4",
    "NU_NOTA_COMP5",
    "NU_NOTA_REDACAO",
    "Q001",
    "Q002",
    "Q006",
    "Q025",
]

COLUNAS_NOTAS = [
    "NU_NOTA_CN",
    "NU_NOTA_CH",
    "NU_NOTA_LC",
    "NU_NOTA_MT",
    "NU_NOTA_REDACAO",
]

COLUNAS_PRESENCA = [
    "TP_PRESENCA_CN",
    "TP_PRESENCA_CH",
    "TP_PRESENCA_LC",
    "TP_PRESENCA_MT",
]


# =====================================================
# LEITURA DA BASE ORIGINAL
# =====================================================

print("Lendo base original do ENEM 2020...")

df = pd.read_csv(
    CSV_PATH,
    sep=";",
    encoding="latin1",
    usecols=COLUNAS
)

print(f"Base carregada: {df.shape[0]} linhas e {df.shape[1]} colunas.")


# =====================================================
# CRIAÇÃO DE VARIÁVEIS DERIVADAS
# =====================================================

print("Criando colunas derivadas...")

df["NOTA_TOTAL"] = df[COLUNAS_NOTAS].sum(axis=1, skipna=False)

df["MEDIA_NOTAS"] = df[COLUNAS_NOTAS].mean(axis=1, skipna=False)

df["AUSENTE"] = (
    (df["TP_PRESENCA_CN"] != 1) |
    (df["TP_PRESENCA_CH"] != 1) |
    (df["TP_PRESENCA_LC"] != 1) |
    (df["TP_PRESENCA_MT"] != 1)
)


# =====================================================
# EXPORTAÇÃO DA BASE TRATADA
# =====================================================

print("Salvando dataset tratado...")

df.to_csv(
    OUTPUT_PATH,
    index=False,
    sep=";",
    encoding="utf-8"
)


# =====================================================
# LOG FINAL
# =====================================================

print("Dataset tratado criado com sucesso!")
print(f"Arquivo gerado: {OUTPUT_PATH}")
print(f"Linhas e colunas finais: {df.shape}")
print("Colunas finais:")
print(df.columns.tolist())