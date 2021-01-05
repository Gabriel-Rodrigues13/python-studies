"""
Lançamos o seguinte desafio: para ajudar na formatação de datas você deve crar uma nova classe auxiliar.
Essa classe deve representar uma Data(sem hora) que sabe imprimir uma data formaada. Ela deve funcioanr assim:

from datas import Data
d = Data(21,11,2007)
d.formatada()

imprime:

21/11/2007
"""

class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def formatada(self):
        print(f"{self.dia}/{self.mes}/{self.ano}")
