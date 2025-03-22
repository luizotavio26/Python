# %%
# imports
import os
from dotenv import load_dotenv
from etl.etl import ETL

load_dotenv()

# %%
# conexão com o banco de dados
host = os.getenv("HOST")
banco_de_dados = os.getenv("BANCO_DE_DADOS")

# %%
# testando o ETL
origem = "Pousada.xlsx"
destino = f"mssql+pyodbc://{host}/{banco_de_dados}?driver=ODBC+Driver+17+for+SQL+Server"

etlClass = ETL(origem, destino)

# %%
# extrair dados
etlClass.extract()

# %%
# transformar dados
etlClass.transform()

# %%
# carregar dados
etlClass.load()


# %%
