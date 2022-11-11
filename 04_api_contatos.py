#Construir uma APIRestful (utilizando flask) para controlar uma agenda de contatos:

#################### BIBLIOTECAS UTILIZADAS #################### 
import json
import sqlite3
from flask import Flask
from flask import render_template
from flask import jsonify, redirect
from flask import request

#################### APLICAÇÃO FLASK #################### 
app = Flask(__name__)

#################### PAGINA INICIAL #################### 
@app.route('/')
def hello_world():
    return """
    <h1>Bem-vindo a API de agenda</h1>
    <p>Essa APIRestful permite que você controle uma agenda de contatos.</p>
    <h3>Endpoints:</h3>
    <ul>
        <li>localhost/contatos | Método POST | Adiciona um novo contato na agenda</li>
        <li>localhost/contatos | Método GET | Consulta todos os contatos da agenda</li>
        <li>localhost/contatos/<id> | Método GET | Consultar contato por id</li>
        <li>localhost/contatos/<id> | Método PUT | Edita um contato da agenda</li>
        <li>localhost/contatos/<id> | Método DELETE | Exclui um contato da agenda</li>
        <li>localhost/contatos/nomes/<nome> | Método GET | Obtem contatos por nome</li>
        <li>localhost/contatos/empresas/<empresa> | Método GET | Obtem contatos por empresa</li>
        <li>localhost/contatos/email/<empresa> | Método GET | Obtem contatos por email</li>
        <li>localhost/contatos/empresas | Método GET | Obtem contatos agrupados por empresa</li>
    </ul>
    """
    
#################### CRIAR CONTATO #################### 
@app.route('/contatos', methods=["POST"])
def insereContato():
    try:
        con = sqlite3.connect("agenda.db")
        cursor = con.cursor()
        
        novo_contato = request.get_json()
        print(novo_contato) #RETORNO DE UM JSON
        
        nome = novo_contato.get('nome')
        empresa = novo_contato.get('empresa')
        telefone = novo_contato.get('telefone')
        email = novo_contato.get('email')
        
        comando_sql = f"""
        INSERT INTO contatos (nome, empresa, telefone, email)
        VALUES ("{nome}", "{empresa}", "{telefone}", "{email}")
            """
        cursor.execute(comando_sql)
        con.commit()
        
        return jsonify("SUCESSO! Contato adicionado ao banco de dados."), 200
    
    except sqlite3.OperationalError:
        return jsonify("ERRO NA EXECUÇÃO DA QUERY!"), 404


#################### VISUALIZAR CONTATO #################### 
@app.route('/contatos', methods=["GET"])
def listaContatos():
    try:
        con = sqlite3.connect("agenda.db")
        cursor = con.cursor()
        
        comando_sql ="SELECT * FROM contatos"
        cursor.execute(comando_sql)
        contatos = cursor.fetchall()
        
        return jsonify(contatos)
    except sqlite3.OperationalError:
        return jsonify("ERRO NA EXECUÇÃO DA QUERY!"), 404
    
#################### VISUALIZAR CONTATO POR ID #################### 
@app.route('/contatos/<string:id>', methods=["GET"])
def listaContato(id):
    try:
        con = sqlite3.connect("agenda.db")
        cursor = con.cursor()
        
        comando_sql ="SELECT * FROM contatos WHERE id=" + id
        cursor.execute(comando_sql)
        contato = cursor.fetchall()
        
        return jsonify(contato)
    except sqlite3.OperationalError:
        return jsonify("ERRO NA EXECUÇÃO DA QUERY!"), 404

#################### ATUALIZA CONTATO #################### 
@app.route('/contatos/<int:id>', methods=["PUT"])
def atualizaContatos(id):
    try:
        con = sqlite3.connect("agenda.db")
        cursor = con.cursor()  
             
        contato_atualizado = request.get_json()
        print(contato_atualizado)
        
        id_contato = str(id)      
        nome = contato_atualizado.get('nome')
        empresa = contato_atualizado.get('empresa')
        telefone = contato_atualizado.get('telefone')
        email = contato_atualizado.get('email')
        
        comando_sql = f"""
            UPDATE contatos 
            SET  
                nome =  "{nome}", 
                empresa = "{empresa}", 
                telefone =  "{telefone}", 
                email = "{email}"
            WHERE id = "{id_contato}" """
            
        cursor.execute(comando_sql)
        con.commit()
        
        return jsonify("SUCESSO! Contato atualizado!"), 200
    except sqlite3.OperationalError:
        return jsonify("ERRO NA EXECUÇÃO DA QUERY!"), 404

#################### DELETA CONTATO #################### 

@app.route('/contatos/<int:id>', methods=["DELETE"])
def deletaContatos(id):
    try:
        con = sqlite3.connect("agenda.db")
        cursor = con.cursor()
               
        comando_sql = f"DELETE FROM contatos WHERE id = {id}"
        cursor.execute(comando_sql)
        con.commit()
        
        return jsonify("SUCESSO! Contato deletado do banco de dados"), 200
    except sqlite3.OperationalError:
        return jsonify("Erro de execução de query!"), 404
    
    

#Implementar ao menos as seguintes consultas:
    #por nome
    #por empresa
    #por email
    #OBS: As consultas devem ser feitas de forma que seja possível consultar por coincidência exata ou parcial  

@app.route('/contatos/nomes/<string:nome>', methods=["GET"])
def exibirPorNome(nome):
    try:
        con = sqlite3.connect("agenda.db")
        cursor = con.cursor()
        comando_sql =f" SELECT * FROM contatos WHERE nome like '%{nome}%' "
        cursor.execute(comando_sql)
        contato = cursor.fetchall()
        return jsonify(contato)
    except sqlite3.OperationalError:
        return jsonify("Erro de execução de query!"), 404

@app.route('/contatos/empresas/<string:empresa>', methods=["GET"])
def exibirPorEmpresa(empresa):
    try:
        con = sqlite3.connect("agenda.db")
        cursor = con.cursor()
        comando_sql =f" SELECT * FROM contatos WHERE empresa like '%{empresa}%' "
        cursor.execute(comando_sql)
        contato = cursor.fetchall()
        return jsonify(contato)
    except sqlite3.OperationalError:
        return jsonify("Erro de execução de query!"), 404
    
@app.route('/contatos/email/<string:email>', methods=["GET"])
def exibirPorEmail(email):
    try:
        con = sqlite3.connect("agenda.db")
        cursor = con.cursor()
        comando_sql =f" SELECT * FROM contatos WHERE email like '%{email}%' "
        cursor.execute(comando_sql)
        contato = cursor.fetchall()
        return jsonify(contato)
    except sqlite3.OperationalError:
        return jsonify("Erro de execução de query!"), 404


# Criar segundo endpoint filtrando os contatos por empresa e use o protocolo http (404) em caso de falha.
@app.route('/contatos/empresas', methods=["GET"])
def agrupaEmpresas():
    try:
        con = sqlite3.connect("agenda.db")
        cursor = con.cursor()
        comando_sql =f" SELECT empresa , GROUP_CONCAT(nome , ',') FROM contatos GROUP BY empresa "
        cursor.execute(comando_sql)
        contato = cursor.fetchall()
        return jsonify(contato)
    except sqlite3.OperationalError:
        return jsonify("Erro de execução de query!"), 404
    
#################### EXECUTANDO A APLICAÇÃO FLASK #################### 
if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000)
     
     