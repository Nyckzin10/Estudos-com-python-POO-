from abc import ABC, abstractmethod



class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade


    @property
    def  nome (self):
        return self._nome



    @property
    def idade (self):
        return self._idade



class Cliente(Pessoa):
    def __init(self, nome, idade,):
        super().__init__(nome, idade)
        self.conta = nome

    def inserir_conta(self, conta):
        self.conta = conta


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo


    def depositar(self, valor):
        self.valor = valor


    def detalhes(self):
        print(f'Agencia: {self.agencia}'
              f'conta: {self.conta}'
              f'saldo: {self.saldo}')

    @abstractmethod
    def sacar(self, valor): pass



class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print(f'Saldo Insuficiente')


        self.saldo -= valor
        self.detalhes()

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite = 100):
        super().__init__(agencia, conta, saldo)
        self.limite = limite


    def sacar(self, valor):
        if (self.saldo + self.limite)< valor:
            print('Saldo insuficente')
            return

        self.saldo -= valor
        self.detalhes()

class Banco:
    def __init__(self):
        self.agencias = [1111, 2222, 3333]
        self.clientes = []
        self.contas = []


    def inserir_clientes(self, clientes):
        self.clientes.append(clientes)

    def inseiri_contas(self, contas):
        self.contas.append(contas)



    def autenticar(self, cliente):
      if cliente not in self.clientes:
          return False


       if cliente.conta not in self.contas:
           return False


        if cliente.contas.agencia not in self.agencias:
            return False

        return True