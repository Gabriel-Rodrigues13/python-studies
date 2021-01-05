

class Conta:
    def __init__(self, numero, titular, saldo, limite = 1000.0):
        print(f"Construindo objeto...{self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    def extrato(self):
        print(f"O saldo da conta {self.__numero} é de {self.__saldo}. Seu limite é {self.limite}")
    
    def deposita(self, valor):
        self.__saldo += valor
        print(f"O valor de {valor} foi depositado na conta {self.__numero}. O novo saldo é de {self.__saldo}")

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_sacar = self.saldo + self.limite
        return valor_a_sacar <= valor_disponivel_sacar

    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
            print(f"O valor de {valor} foi sacado da conta {self.__numero}. O novo saldo é de {self.__saldo}")
        else:
            print(f'O valor {valor} passou o limite')

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