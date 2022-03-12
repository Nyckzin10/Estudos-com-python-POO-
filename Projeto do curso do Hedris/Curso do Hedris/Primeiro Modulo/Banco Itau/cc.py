from classes.conta import Conta

class ContaConrrente(Conta):
    def __init__(self, agencia, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self.__limite = limite

    @property
    def limite(self):
        return self.__limite
    def sacar(self, valor):
        if (self.saldo+ self.limite) < valor:
            print('Saldo Insuficiente')
            return
        self.saldo -= valor
        self.detalhes()
