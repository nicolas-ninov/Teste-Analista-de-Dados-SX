import pandas as pd
from sqlalchemy import create_engine


# =====================================================
# CONFIGURAÇÕES
# =====================================================

DATA_PATH = "inputs/enem_2020_tratado.csv"

DB_USER = "root"
DB_PASSWORD = "root"
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "enem"

TABLE_NAME = "enem_2020_tratado"


# =====================================================
# LEITURA DO DATASET TRATADO
# =====================================================

print("Lendo dataset tratado...")

df = pd.read_csv(
    DATA_PATH,
    sep=";"
)

print(
    f"Dataset carregado: "
    f"{df.shape[0]} linhas e {df.shape[1]} colunas."
)


# =====================================================
# CONEXÃO COM O MYSQL
# =====================================================

print("Conectando ao MySQL...")

engine = create_engine(
    f"mysql+pymysql://"
    f"{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}"
    f"/{DB_NAME}"
)

print("Conexão criada com sucesso.")


# =====================================================
# CARGA DOS DADOS (LOAD)
# =====================================================

print("Iniciando carga no MySQL...")
print("Este processo pode levar alguns minutos.")


df.to_sql(
    TABLE_NAME,
    con=engine,
    if_exists="replace",
    index=False,
    chunksize=10000,
)


# =====================================================
# LOG FINAL
# =====================================================

print("Carga finalizada com sucesso!")

print(f"Tabela criada/substituída: {TABLE_NAME}")

print(f"Total de registros carregados: {len(df)}")