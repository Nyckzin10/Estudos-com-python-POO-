import sqlite3 

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()



cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Hedris", 80)') 
conexao.commit()


cursor.execute ('SELECT FROM * clientes')


for linha in cursor.fetchall():
    indentifador, nome, peso = linha 


    print(indentifador, nome, peso)




cursor.close()
conexao.close()
