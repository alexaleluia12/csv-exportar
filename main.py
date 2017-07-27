"""
Expor clientes do RL para banco de dados ja com todos as relacoes prontas
"""

import csv



import utils
import nomes




def insert(sql_insert, lst_to_insert):
    passo = 700
    sucess = True
    conn = utils.get_db_conn()
    # sql_update = "UPDATE `retorno_diario` SET `qtde_consultas` = {0} WHERE `id` = {1};"
    sql_topo = sql_insert
    contador = 0
    try:
        with conn.cursor() as cursor:

            sub_list = []
            for e in lst_to_insert:
                sub_list.append(e)
                contador += 1

                if contador == passo:  # chegou ao maximo
                    sql = sql_topo + ", \n".join(sub_list)
                    cursor.execute(sql)
                    # print(sql + "\n")
                    sub_list.clear()  # limpa a lista para inserir mais dados
                    contador = 0

            # insera a sobra da lista antes de passo
            if len(sub_list) > 0:
                sql = sql_topo + ", \n".join(sub_list)
                cursor.execute(sql)
                # print(sql + "\n")


    except Exception as e:
        traceback.print_exc()
        sucess = False
        conn.rollback()
    else:
        conn.commit()
    finally:
        conn.close()

    return sucess



def trade_forex():
    """
    1. pegar linhas
    2. criar lista de insert insert ('')
    3. chamar insert
    """
    modea = "XXBTZUSD"
    arquivo_work = "60min.txt"
    
    lst_saida = []
    primeiro = 0
    # //data,open,hight,low,close,volume
    #    0    1    2     3   4      5
    data = 0
    open_ = 1
    height = 2
    low = 3
    close = 4
    volume = 5
    template = "('{}', '{}', {}, {}, {}, {}, {})"
    with open(arquivo_work) as f:
        csv_arquivo = csv.reader(f)
        for linha in csv_arquivo:
            if primeiro == 0:
                primeiro = 1
                continue
            to_insert = template.format(modea, linha[data], linha[open_], linha[height],
                linha[low], linha[close], linha[volume]
            )
            lst_saida.append(to_insert)
     
    sql_topo = "INSERT INTO `sessenta` (`currency`, `date`, `open`, `high`, `low`, `close`, `volume`) VALUES "

    r = insert(sql_topo, lst_saida)
    print("sucesso: ", r)
    # print(lst_saida)

if __name__ == '__main__':
    trade_forex()
