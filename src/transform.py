from datetime import datetime
from pydantic import BaseModel


class DataFrameHans(BaseModel):
    dt_notific: datetime
    sg_uf_not: int
    id_municip: int
    id_unidade: int
    dt_diag: datetime
    ano_nasc: int
    nu_idade_n: int
    cs_sexo: str
    cs_gestant: int
    cs_raca: int
    cs_escol_n: int
    sg_uf: int
    id_mn_resi: int
    id_ocupa_n: int
    nu_lesoes: int
    formaclini: int
    avalia_n: int
    classopera: int
    modoentr: int
    mododetect: int
    baciloscop: int
    dtinictrat: datetime
    esq_ini_n: int
    contreg: int
    nervosafet: int
    ufatual: str
    id_muni_at: int
    dt_noti_at: datetime
    ufresat: int
    muniresresat: int
    dtultcomp: datetime
    classatual: int
    aval_atu_n: int
    esq_atu_n: int
    dose_receb: int
    epis_racio: int
    dtmudesq: datetime
    contexam: int
    dtalta_n: datetime
    tpalta_n: int


def selecionar_colunas(data, var_list):
    """
    Selecionar colunas de um DataFrame.
    """
    data = data[var_list]

    return data
