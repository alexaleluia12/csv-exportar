
```text

considerando um banco no Mysql quero exportar um csv para esse banco.

o csv deve ter dados de apenas uma tabela


as informacoes minimas que deve ser oferecias ao software:
    host, user, senha, nome_banco, tabela, arquivo_csv_com_dados

---------------------------------------
campos char dever ser cercados de ''



===== ambiente em python ==============

$ virtualenv env --python=python3
$ source env/bin/activate
$ pip install -r requirements.txt

(crie o banco local localhost conforme schema.sql)
 configuracao do banco esta em banco2.json

(ja esta no 60min.txt, caso queira preencher outros deve:
 trocar o valor de arquivo_work
 setar ta tabela corresponde em sql_topo
)
$ python main.py

```
