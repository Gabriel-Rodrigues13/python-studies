

class Conta:
    def __init__(self, numero, titular, saldo, limite = 1000.0):
        print(f"Construindo objeto...{self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    def extrato(self):
        print(f"O saldo da conta {self.__numero} é de {self.__saldo}.")
    
    def deposita(self, valor):
        self.__saldo += valor
        print(f"O valor de {valor} foi depositado na conta {self.__numero}. O novo saldo é de {self.__saldo}")

    def saca(self, valor):
        self.__saldo -= valor
        print(f"O valor de {valor} foi sacado da conta {self.__numero}. O novo saldo é de {self.__saldo}")

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite