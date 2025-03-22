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
url = f"mssql+pyodbc://{host}/{banco_de_dados}?driver=ODBC+Driver+17+for+SQL+Server"
engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()

livro_crud = CRUD(Livro, session)
print("Conexão com o banco de dados foi bem sucedida.")


# %%
# Criar registro
def test_create():
    # TODO: Este teste deve criar um novo livro no banco de dados com os dados fornecidos
    # e, em seguida, verificar se o livro foi realmente adicionado verificando seu ISBN.
    livro_crud.create(
        isbn="9788521630814",
        titulo="Introdução à Computação Usando Python",
        autor="PERKOVIC, L.",
        ano_publicacao=2016,
        genero="Programação",
    )

    livro_encontrado = livro_crud.read(isbn="9788521630814")
    assert livro_encontrado is not None, "O livro não foi encontrado no Banco de Dados"

test_create()


# %%
# Ler como lista
def test_read_as_list():
    # TODO: Este teste deve ler os livros do banco de dados como uma lista de objetos Livro
    # e verificar se o ISBN do primeiro livro retornado é igual a "9788521630814".
    livros_lista: list[Livro] = livro_crud.read()
    print('Lista de livros:')
    for livro in livros_lista:
        print(livro.to_string())

    if len(livros_lista) > 0:
        primeiro_livro = livros_lista[0]
        print(f"ISBN do primeiro livro: {primeiro_livro.isbn}")
        assert primeiro_livro.isbn == "9788521630814", "O ISBN existente não corresponde ao ISBN do primeiro livro cadastrado "
    else: 
        assert False, "A lista de livros está vazia"

test_read_as_list()


# %%
# Ler como dataframe
def test_read_as_dataframe():
    # TODO: Este teste deve ler os livros do banco de dados como um DataFrame
    # e verificar se o ISBN do primeiro livro no DataFrame é igual a "9788521630814".
    livros_df = livro_crud.read(as_dataframe=True)
    isbn_primeiro_livro = livros_df["isbn"].iloc[0]
    print(f"ISBN do primeiro livro: {isbn_primeiro_livro}")
    assert isbn_primeiro_livro == "9788521630814"

test_read_as_dataframe()


# %%
# Atualizar registro
def test_update():
    # TODO: Este teste deve atualizar o título do livro com ISBN "9788521630814"
    # para "Introdução à Computação Usando Python - Um Foco no Desenvolvimento de Aplicações"
    # e, em seguida, verificar se a atualização foi bem-sucedida, confirmando que o título
    # do livro foi alterado.
    livro_crud.update(
        obj_id="9788521630814",
        titulo="Introdução à Computação Usando Python - Um Foco no Desenvolvimento de Aplicações",
        ano_publicacao=2021,
    )

    livro_atualizado_read = livro_crud.read(isbn="9788521630814")
    livro_atualizado = livro_atualizado_read[0]

    assert livro_atualizado.titulo == "Introdução à Computação Usando Python - Um Foco no Desenvolvimento de Aplicações", "Livro não atualizado corretamente"

test_update()


# %% 
# Deletar registro
def test_delete():
    # TODO: Este teste deve deletar do banco de dados o livro criado no test_create
    # e, em seguida, verificar se ele foi realmente removido, confirmando que não
    # existem mais livros com esse ISBN no banco.   
    livro_crud.delete(obj_id="9788521630814")
    verificar_delete = livro_crud.read(isbn="9788521630814")
    todos_livros = livro_crud.read()
    assert "9788521630814" not in todos_livros, "Livro ainda está na lista"

test_delete()

# %%
