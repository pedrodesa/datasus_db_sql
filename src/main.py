from etl.load import conectar_db, inserir_dados_no_postgres
from etl.extract import ler_arquivo
from etl.transform import selecionar_colunas
# from etl.validation import DataFrameHans


def main():
    # Importar dados em CSV
    path = './data/output/hans.csv'

    dados = ler_arquivo(path, separador=';')

    # Selecionar variáveis
    variaveis = [
        'DT_NOTIFIC',
        'SG_UF_NOT',
        'ID_MUNICIP',
        'ID_UNIDADE',
        'DT_DIAG',
        'ANO_NASC',
        'NU_IDADE_N',
        'CS_SEXO',
        'CS_GESTANT',
        'CS_RACA',
        'CS_ESCOL_N',
        'SG_UF',
        'ID_MN_RESI',
        'ID_OCUPA_N',
        'NU_LESOES',
        'FORMACLINI',
        'AVALIA_N',
        'CLASSOPERA',
        'MODOENTR',
        'MODODETECT',
        'BACILOSCOP',
        'DTINICTRAT',
        'ESQ_INI_N',
        'CONTREG',
        'NERVOSAFET',
        'UFATUAL',
        'ID_MUNI_AT',
        'DT_NOTI_AT',
        'UFRESAT',
        'MUNIRESAT',
        'DTULTCOMP',
        'CLASSATUAL',
        'AVAL_ATU_N',
        'ESQ_ATU_N',
        'DOSE_RECEB',
        'EPIS_RACIO',
        'DTMUDESQ',
        'CONTEXAM',
        'DTALTA_N',
        'TPALTA_N'
    ]

    dados = selecionar_colunas(dados, variaveis)

    dados.columns = dados.columns.str.lower()

    # Validação de dados
    # dataframehans = DataFrameHans(**dados)
    # print(dataframehans.model_dump())

    # Carregameto de dados no PostgreSQL
    nome_tabela = 'tb_hans_sinan'

    # Consecta-se ao PostgreSQL
    conn = conectar_db()

    # Insere os dados do DataFrame na tabela do PostgreSQL
    if conn is not None:
        inserir_dados_no_postgres(conn, dados, nome_tabela)

        # Fecha a conexão
        conn.close()


if __name__ == '__main__':
    main()
