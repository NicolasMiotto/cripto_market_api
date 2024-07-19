from sqlalchemy import create_engine
from env import DATABASE_URL
import pandas as pd
import os


def create_db_connection():
    db_url = DATABASE_URL   
    try:
        # Criar a conexão
        engine = create_engine(db_url)
        
        print("Conexão estabelecida com sucesso.")
    except Exception as e:
        print(f'Erro na conexão com o banco de dados: {e}')
        engine = None

    return engine

def insert_crypto_data(df, table_name):
    connect = create_db_connection()

    try:
        df.to_sql(table_name, connect, if_exists='append', index=False)
        
        print(f"Dados inseridos com sucesso na tabela {table_name}.")
    except Exception as e:
        print(f"Erro ao inserir dados na tabela {table_name}: {e}")

