##################### Criar a tabela contatos (id, nome, empresa, telefone, email) #####################
import sqlite3
from flask import jsonify

def criaTabelaContatos():
    banco = "agenda.db"
    tabela = "contatos"
    
    con = sqlite3.connect(banco)
    print(f"Conexao ao banco {banco} realizada com sucesso! \n")
    cursor = con.cursor()
    
    cursor.execute(
    f"""CREATE TABLE {tabela}(
      id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
      nome TEXT NOT NULL, 
      empresa TEXT NOT NULL, 
      telefone TEXT NOT NULL, 
      email TEXT NOT NULL)""")
    print(f'Tabela {tabela} criada com sucesso.\n')

criaTabelaContatos()