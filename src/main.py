from etl.load import conectar_db, inserir_dados_no_postgres
from etl.extract import ler_arquivo
from etl.transform import selecionar_colunas


def main():
    # Importar dados em CSV
    path = './data/hans.csv'

    dados = ler_arquivo(path, separador=';')

    # Selecionar variáveis
    variaveis = [
        'dt_notific',
        'sg_uf_not',
        'id_municip',
        'id_unidade',
        'dt_diag',
        'ano_nasc',
        'nu_idade_n',
        'cs_sexo',
        'cs_gestant',
        'cs_raca',
        'cs_escol_n',
        'sg_uf',
        'id_mn_resi',
        'id_ocupa_n',
        'nu_lesoes',
        'formaclini',
        'avalia_n',
        'classopera',
        'modoentr',
        'mododetect',
        'baciloscop',
        'dtinictrat',
        'esq_ini_n',
        'contreg',
        'nervosafet',
        'ufatual',
        'id_muni_at',
        'dt_noti_at',
        'ufresat',
        'muniresresat',
        'dtultcomp',
        'classatual',
        'aval_atu_n',
        'esq_atu_n',
        'dose_receb',
        'epis_racio',
        'dtmudesq',
        'contexam',
        'dtalta_n',
        'tpalta_n'
    ]

    dados = selecionar_colunas(dados, variaveis)

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
