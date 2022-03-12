import sqlite3 
import conn 

class AgendaDB:

    def __init__(self, arquivo):
        self.conn - sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()


    def inserir(self, nome, telefone):
        consulta =  'INSERT OR IGNORE INTO agenda (nome, telefone) VALUE (?, ?)'
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()


    def editar(self, nome, telefone, id):
        consultar = 'UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(consultar, (nome, telefone, id))
        self.conn.commit()


    def excluir(self, id):
        consultar = 'DELETE FROM agenda WHERER id=?'
        self.cursor.execute(consultar, (id,))
        self.conn.commit()


    def listar(self):
        self.curosr.execute('SELECT * FROM agenda')

        for linha in self.cursor.fetchall():
            print(linha)


    def buscar(self, valor):
        consultar = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(consultar, (f'%{valor}',))

        for linha in self.cursor.fetchall():
            print(linha)

    
    def fechar(self):
        self.cursor.close()
        self.conn.close()



if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')
    agenda.buscar('')



