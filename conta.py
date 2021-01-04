

class Conta:
    def __init__(self, numero, titular, saldo, limite = 1000.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    
    def extrato(self):
        print(f"O saldo da conta {self.numero} é de {self.saldo}.")
    
    def deposita(self, valor):
        self.saldo += valor
        print(f"O valor de {valor} foi depositado na conta {self.numero}. O novo saldo é de {self.saldo}")

    def saca(self, valor):
        self.saldo -= valor
        print(f"O valor de {valor} foi sacado da conta {self.numero}. O novo saldo é de {self.saldo}")