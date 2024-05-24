import os
from functools import wraps
import psycopg2
from dotenv import load_dotenv
from sqlalchemy import create_engine


def acessar_dotenv(func):
    """Carrega arquivo dotenv."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        load_dotenv()
        return func(*args, **kwargs)

    return wrapper


@acessar_dotenv
def conectar_db():
    """Conecat ao PostgreSQL."""
    try:
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            database=os.getenv('POSTGRES_DB'),
            user=os.getenv('POSTGRES_USER'),
            password=os.getenv('POSTGRES_PASSWORD'),
            port=os.getenv('DB_PORT')
        )

        print('Conexão com o PostgreSQL bem sucedida!')

        return conn

    except Exception as error:
        print(f'Erro ao conectar ao PostgreSQL: {error}')


@acessar_dotenv
def inserir_dados_no_postgres(conn, data, nome_tabela):
    """
    Insere os dados de um arquivo CSV na
    na tabela do PostgreSQL.

    conn.close(): Fecha a conexão.
    """
    try:
        engine = create_engine(
            f'postgresql://{os.getenv("POSTGRES_USER")}:{os.getenv("POSTGRES_PASSWORD")}@{os.getenv("DB_HOST")}/{os.getenv("DATABASE")}'
        )
        data.to_sql(nome_tabela, engine, if_existis='replace', index=False)
        print('Dados inseridos na tabela com sucesso!')
    except Exception as error:
        print(f'Erro ao inserir os dados no PostgreSQL: {error}')
