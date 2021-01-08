
class Funcionario:

    def __init__(self, nome):
        self.nome = nome.title()

    def registra_horas(self, horas):
        print('Horas registradas.')
    def mostrar_tarefas(self):
        print('Fez muita coisa...')


    
class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa Caelumer!')

    def busca_curso_do_mes(self, mes=None):
        print(f'Monstrando cursos - {mes}' if mes else 'Mostrando cursos desse mes')

    
class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostando perguntas não respondida no fórum')


class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'


class Junior(Alura, Hipster):
    pass

class Pleno(Alura, Caelum, Hipster):
    pass

jose = Junior('jose')
jose.busca_perguntas_sem_resposta()

luan = Pleno('luan')
luan.busca_perguntas_sem_resposta()
luan.busca_curso_do_mes()
luan.mostrar_tarefas()

print(luan)