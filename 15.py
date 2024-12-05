class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, no_atual, valor):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(valor)
            else:
                self._inserir_recursivo(no_atual.esquerda, valor)
        elif valor > no_atual.valor:
            if no_atual.direita is None:
                no_atual.direita = No(valor)
            else:
                self._inserir_recursivo(no_atual.direita, valor)

    def encontrar_minimo(self):
        atual = self.raiz
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual.valor

    def encontrar_maximo(self):
        atual = self.raiz
        while atual.direita is not None:
            atual = atual.direita
        return atual.valor

arvore = ArvoreBinaria()
notas = [85, 70, 95, 60, 75, 90, 100, 25]
for nota in notas:
    arvore.inserir(nota)

minimo = arvore.encontrar_minimo()
maximo = arvore.encontrar_maximo()

print("Nota mínima:", minimo)
print("Nota máxima:", maximo)
