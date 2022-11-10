##################### CRIAR BASE DE DADOS EM SQLITE#####################
import sqlite3
from flask import jsonify

def criaBanco():
    banco = 'agenda.db'
    try: 
        con = sqlite3.connect(banco)
        print(f"Banco {banco} criado com sucesso! \n")
        con.close()
    except:
        return jsonify(f"Não foi possível realizar a criação do Banco de dados {banco}")

criaBanco()