class Navegador:
    def __init__(self):
        self.pilha_voltar = []
        self.pilha_avancar = []

    def visitar_pagina(self, pagina):
        self.pilha_voltar.append(pagina)
        self.pilha_avancar.clear()
        print(f"Visitando: {pagina}")

    def voltar(self):
        if not self.pilha_voltar:
            return "Não há páginas para voltar."
        pagina_atual = self.pilha_voltar.pop()
        self.pilha_avancar.append(pagina_atual)
        return f"Voltando para: {self.pilha_voltar[-1]}" if self.pilha_voltar else "Não há mais páginas anteriores."

    def avancar(self):
        if not self.pilha_avancar:
            return "Não há páginas para avançar."
        pagina_atual = self.pilha_avancar.pop()
        self.pilha_voltar.append(pagina_atual)
        return f"Avançando para: {pagina_atual}"

navegador = Navegador()

navegador.visitar_pagina("Página 1")
navegador.visitar_pagina("Página 2")
navegador.visitar_pagina("Página 3")

print(navegador.voltar())
print(navegador.voltar())
print(navegador.avancar())

navegador.visitar_pagina("Página 4")

print(navegador.avancar())
