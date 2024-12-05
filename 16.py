class No:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None


class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        if self.raiz is None:
            self.raiz = No(chave)
        else:
            self._inserir(self.raiz, chave)

    def _inserir(self, no, chave):
        if chave < no.chave:
            if no.esquerda is None:
                no.esquerda = No(chave)
            else:
                self._inserir(no.esquerda, chave)
        else:
            if no.direita is None:
                no.direita = No(chave)
            else:
                self._inserir(no.direita, chave)

    def remover(self, chave):
        self.raiz = self._remover(self.raiz, chave)

    def _remover(self, no, chave):
        if no is None:
            return no

        if chave < no.chave:
            no.esquerda = self._remover(no.esquerda, chave)
        elif chave > no.chave:
            no.direita = self._remover(no.direita, chave)
        else:
            if no.esquerda is None and no.direita is None:
                return None
            elif no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda
            else:
                sucessor = self._encontrar_minimo(no.direita)
                no.chave = sucessor.chave
                no.direita = self._remover(no.direita, sucessor.chave)
        return no

    def _encontrar_minimo(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def em_ordem(self):
        resultado = []
        self._em_ordem(self.raiz, resultado)
        return resultado

    def _em_ordem(self, no, resultado):
        if no is not None:
            self._em_ordem(no.esquerda, resultado)
            resultado.append(no.chave)
            self._em_ordem(no.direita, resultado)


codigos = [45, 25, 65, 20, 30, 60, 70]
arvore = ArvoreBinariaBusca()
for codigo in codigos:
    arvore.inserir(codigo)

print("Árvore em ordem crescente:", arvore.em_ordem())
arvore.remover(20)
print("Árvore após a remoçao do nó folha:", arvore.em_ordem())
arvore.remover(25)
print("Árvore após a remoçao do nó com um filho:", arvore.em_ordem())
arvore.remover(45)
print("Árvore após a remoçao do nó com dois filhos:", arvore.em_ordem())
