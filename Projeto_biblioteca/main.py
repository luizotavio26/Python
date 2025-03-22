# %%
# imports
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from crud import CRUD
from relacoes import Livro

load_dotenv()

# %%
# Conexão com o banco de dados
host = os.getenv("HOST")
banco_de_dados = os.getenv("BANCO_DE_DADOS")


url = (f"mssql+pyodbc://{host}/{banco_de_dados}?driver=ODBC+Driver+17+for+SQL+Server")
engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()

livro_crud = CRUD(Livro, session)

# %%
# criando livros
livro_crud.create(
    isbn="9788521630814",
    titulo="Introdução à Computação Usando Python",
    autor="PERKOVIC, L.",
    ano_publicacao=2016,
    genero="Programação",
)

# %%
# Lendo registros como lista de objetos
livros_lista: list[Livro] = livro_crud.read()
for livro in livros_lista:
    print(livro.to_string())
# %%
# Lendo registros como dataframe e exportando para csv
livros_df = livro_crud.read(as_dataframe=True)
print(livros_df)
livros_df.to_csv("livros.csv")
# %%
# Filtrando pelo ISBN
livro_desejado: Livro = livro_crud.read(as_dataframe=False, isbn="9788521630814")[0]
print(livro_desejado.to_string())
# %%
# atualizando um registro
livro_crud.update(
    obj_id="9788521630814",
    titulo="Introdução à Computação Usando Python - Um Foco no Desenvolvimento de Aplicações",
    ano_publicacao=2021,
)
# %%
# removendo um registro
livro_crud.delete(obj_id="9788521630814")

# %%
# encerrando a sessão com o banco de dados
session.close()

####