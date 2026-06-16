import pandas as pd


# =====================================================
# CONFIGURAÇÕES
# =====================================================

CSV_PATH = "dados/MICRODADOS_ENEM_2020.csv"


# =====================================================
# LEITURA DA BASE
# =====================================================

print("Lendo uma amostra da base do ENEM 2020...")

df = pd.read_csv(
    CSV_PATH,
    sep=";",
    encoding="latin1",
    nrows=1
)


# =====================================================
# EXPLORAÇÃO DA ESTRUTURA
# =====================================================

print("\nColunas encontradas na base:\n")

print("Total de colunas:", len(df.columns))

print("\nLista de colunas:\n")

for coluna in df.columns:
    print(coluna)