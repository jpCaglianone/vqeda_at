from collections import deque

class FilaAtendimento:
    def __init__(self):
        self.fila = deque()

    def adicionar_chamado(self, chamado):
        self.fila.append(chamado)

    def remover_chamado(self):
        if self.fila:
             return self.fila.popleft()
        return "Nenhum chamado na fila."

    def exibir_fila(self):
        return list(self.fila)

fila = FilaAtendimento()

fila.adicionar_chamado("Chamado 1: Problema no login")
fila.adicionar_chamado("Chamado 2: Falha no sistema")
fila.adicionar_chamado("Chamado 3: Dúvida sobre o produto")

print("Fila de chamados inicial:", fila.exibir_fila())

print("Atendendo:", fila.remover_chamado())

print("Fila de chamados atual:", fila.exibir_fila())

print("Atendendo:", fila.remover_chamado())
print("Atendendo:", fila.remover_chamado())

print("Atendendo:", fila.remover_chamado())
