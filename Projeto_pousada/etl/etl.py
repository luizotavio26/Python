from etl.abstract_etl import AbstractETL
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from modelos.Cliente import Cliente
from modelos.Data import Data
from modelos.Quarto import Quarto
from modelos.Reserva import Reserva
from modelos.Status import Status


class ETL(AbstractETL):
    def __init__(self, origem, destino):
        super().__init__(origem, destino)
    
    def extract(self):
        # TODO: lê os dados a serem inseridos a partir do caminho do arquivo (origem)

        try:
            self._dados_extraidos = {}
            self._dados_extraidos['Cliente'] = pd.read_excel(self.origem, sheet_name='Cliente')
            self._dados_extraidos['Reserva'] = pd.read_excel(self.origem, sheet_name='Reserva')
            self._dados_extraidos['Quarto'] = pd.read_excel(self.origem, sheet_name='Quarto')
            self._dados_extraidos['Data'] = pd.read_excel(self.origem, sheet_name='Data')
            self._dados_extraidos['Status'] = pd.read_excel(self.origem, sheet_name='Status')
            print("Dados extraídos com sucesso!")
            print(self._dados_extraidos)

        except FileNotFoundError:
            print('Arquivo não encontrado!')

        except Exception as e:
            print(f'Erro ao extrair os dados: {e}')
        
        
    def transform(self):
        # TODO: transforma os dados extraídos em um formato mais adequado para inserção
                
        if self._dados_extraidos == None:
            print("Não há dados para serem transformados.")
            self._dados_transformados == None
        else:    
            try:
                self._dados_transformados = {}
                for chave, valor in self._dados_extraidos.items():
                    if chave == 'Cliente':
                        self._dados_transformados[chave] = Cliente.from_dataframe(valor)
                    elif chave == 'Reserva':
                        self._dados_transformados[chave] = Reserva.from_dataframe(valor)
                    elif chave == 'Quarto':
                        self._dados_transformados[chave] = Quarto.from_dataframe(valor)
                    elif chave == 'Data':
                        self._dados_transformados[chave] = Data.from_dataframe(valor)
                    elif chave == 'Status':
                        self._dados_transformados[chave] = Status.from_dataframe(valor)
                print("Transformação concluída!")
                print(self._dados_transformados)

            except AttributeError as e:
                print(f'Erro. Atributo não encontrado. Mais detalhes: {e}')

            except Exception as e:
                print(f'Erro ao transformar os dados: {e}')
            

    def load(self):
            
        if self._dados_transformados == None:
            print("Não há dados para serem carregados.")

        else: 
            try:
                # Criação da engine e sessão
                engine = create_engine(self.destino)
                Session = sessionmaker(bind=engine)
                session = Session()

                if 'Quarto' in self._dados_transformados:
                    session.add_all(self._dados_transformados['Quarto'])
                    session.flush()  

                if 'Status' in self._dados_transformados:
                    session.add_all(self._dados_transformados['Status'])
                    session.flush()  

                if 'Data' in self._dados_transformados:
                    session.add_all(self._dados_transformados['Data'])
                    session.flush()  

            
                if 'Reserva' in self._dados_transformados:
                    session.add_all(self._dados_transformados['Reserva'])

                
                if 'Cliente' in self._dados_transformados:
                    session.add_all(self._dados_transformados['Cliente'])
                    session.flush()  

                # Commit das transações
                session.commit()
                print('Dados carregados com sucesso!')

            except SQLAlchemyError as e:
                session.rollback()  # Faz rollback em caso de erro
                print(f'Erro ao carregar os dados no banco: {e}')

            except Exception as e:
                print(f'Erro inesperado: {e}')
                session.rollback()

            finally:
                session.close()  # Fecha a sessão
                print("Sessão fechada.")

