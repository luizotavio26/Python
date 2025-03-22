import pandas as pd
from sqlalchemy.orm import Session

class CRUD:
    def __init__(self, tabela, session: Session):
        self.__tabela = tabela
        self.__session = session

    def create(self, **kwargs):
        try:   
            obj = self.__tabela(**kwargs)
            self.__session.add(obj)
            self.__session.commit()
            print(f"Registro criado")
        except Exception as e:
            print('Ocorreu um erro inesperado ao criar o objeto')
            print('informações do erro:', e)

    def read(self, as_dataframe=False, **filters):
        try:
            query = self.__session.query(self.__tabela)
            if filters:
                query = query.filter_by(**filters)

            results = query.all()

            if not results:
                return "Registro não encontrado"
            elif as_dataframe:
                data = [obj.__dict__ for obj in results]
                df = pd.DataFrame(data).drop("_sa_instance_state", axis=1, errors="ignore")
                return df
            else:
                return results
        
        except Exception as e:
            print('Ocorreu um erro inesperado ao criar o objeto')
            print('informações do erro:', e)

    def update(self, obj_id, **kwargs):
        try:
            obj = self.__session.get(self.__tabela, obj_id)
            if obj:
                for key, value in kwargs.items():
                    setattr(obj, key, value)
                self.__session.commit()
                print(f"Registro atualizado")
            else:
                print(f"Registro não encontrado.")

        except Exception as e:
            print('Ocorreu um erro inesperado ao criar o objeto')
            print('informações do erro:', e)
    
    def delete(self, obj_id):
        try:
            obj = self.__session.get(self.__tabela, obj_id)
            if obj:
                self.__session.delete(obj)
                self.__session.commit()
                print(f"Registro removido")
            else:
                print(f"Registro não encontrado.")
        except Exception as e:
            print('Ocorreu um erro inesperado ao criar o objeto')
            print('informações do erro:', e)