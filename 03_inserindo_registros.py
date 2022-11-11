import sqlite3

con = sqlite3.connect("agenda.db")
cursor = con.cursor()

cursor.execute("""
    INSERT INTO contatos (nome, empresa, telefone, email)
    VALUES
        ('Anne', 'Una Aimores', '33991919191', 'anne@gmail.com')
    """)
con.commit()
print('Valores adicionados com sucesso.\n')

cursor.execute("""
    INSERT INTO contatos (nome, empresa, telefone, email)
    VALUES
        ('Joana', 'Una Liberdade', '31999996666', 'joana@gmail.com')
    """)
con.commit()
print('Valores adicionados com sucesso.\n')

cursor.execute("""
    INSERT INTO contatos (nome, empresa, telefone, email)
    VALUES
        ('Caio', 'UFMG', '31994444444', 'caio@gmail.com')
    """)
con.commit()
print('Valores adicionados com sucesso.\n')

cursor.execute("""
    INSERT INTO contatos (nome, empresa, telefone, email)
    VALUES
        ('Paulo', 'UEMG', '31965656565', 'paulo@yahoo.com')
    """)
con.commit()
print('Valores adicionados com sucesso.\n')

cursor.execute("""
    INSERT INTO contatos (nome, empresa, telefone, email)
    VALUES
        ('João', 'UNIBH', '33991919191', 'joao@gmail.com')
    """)
con.commit()
print('Valores adicionados com sucesso.\n')

cursor.execute("""
    INSERT INTO contatos (nome, empresa, telefone, email)
    VALUES
        ('Pedro', 'UFV', '31998787676', 'pedro@hotmail.com')
    """)
con.commit()
print('Valores adicionados com sucesso.\n')

cursor.execute("""
    INSERT INTO contatos (nome, empresa, telefone, email)
    VALUES
        ('Alice', 'UFV', '31999567896', 'alice@gmail.com')
    """)
con.commit()
print('Valores adicionados com sucesso.\n')

cursor.execute("""
    INSERT INTO contatos (nome, empresa, telefone, email)
    VALUES
        ('Anna Luiza', 'Una Betim', '33991919191', 'annaluiza@yahoo.com')
    """)
con.commit()
print('Valores adicionados com sucesso.\n')

cursor.execute("""
    INSERT INTO contatos (nome, empresa, telefone, email)
    VALUES
        ('Pedro Henrique', 'Una Liberdade', '33991919191', 'pedrohenrique@hotmail.com')
    """)
con.commit()
print('Valores adicionados com sucesso.\n')

cursor.execute("""
    INSERT INTO contatos (nome, empresa, telefone, email)
    VALUES
        ('Pedro Augusto', 'UFMG', '33991919191', 'pedroaugusto@yahoo.com')
    """)
con.commit()
print('Valores adicionados com sucesso.\n')

con.close()
print("Conexao encerrada...")