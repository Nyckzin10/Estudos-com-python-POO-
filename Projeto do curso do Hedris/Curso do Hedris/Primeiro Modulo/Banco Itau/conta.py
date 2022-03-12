from abc import ABC, abstractmethod

class Conta(ABC):
    def __int__(self, agencia, conta, saldo):
        self.__agencia = agencia
        self.__conta = conta
        self.__saldo = saldo

    @property
    def agencia(self):
        return self.__agencia

    @property
    def conta(self):
        return self.__conta

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Saldo precisar ser númerico")
        self.__saldo = valor

    def depositar(self, valor):
        if not isinstance(valor,   (int, float)):
            raise ValueError("O Valor Precisa ser depositado.")

        self.saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'Agência: {self.agencia}', end=' ')
        print(f'Conta: {self.conta}', end=' ')
        print(f'Saldo: {self.saldo}')


    @abstractmethod
    def sacar(self):
        pass