from classes.conta import Conta

class ContaPoupanca(Conta):
    def sacar(self):
        if self.saldo < valor:
            print('Saldo Insuficiente')
            return
        self.saldo -= valor
        self.detalhes()
