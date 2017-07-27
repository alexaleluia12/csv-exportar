
import json

import pymysql


formato_br = "%d/%m/%Y"
formato_us = "%Y-%m-%d"
formato_serasa = "%Y%m%d"
formato_full = "[%Y-%m-%d %H:%M:%S]"
formato_fulldb = "%Y-%m-%d %H:%M:%S"




def get_config(file_name):
    """
    Dicionario com as chave valor do arquivo
    """
    resultado = None
    with open(file_name + ".json") as f:
        resultado = json.load(f)

    return resultado


def get_db_conn():
    dbconf = get_config('banco2')

    conn = pymysql.connect(
        host=dbconf['host'], user=dbconf['user'], password=dbconf['password'],
        db=dbconf['database']
    )
    return conn


