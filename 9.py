class HashTable:
    def __init__(self):
        self.tabela = {}

    def adicionar_perfil(self, nome_usuario, perfil):
        self.tabela[nome_usuario] = perfil

    def recuperar_perfil(self, nome_usuario):
        if nome_usuario in self.tabela:
            return self.tabela[nome_usuario]
        return "Perfil não encontrado."

rede_social = HashTable()

rede_social.adicionar_perfil("joao123", {"nome": "João", "idade": 25, "cidade": "São Paulo"})
rede_social.adicionar_perfil("maria456", {"nome": "Maria", "idade": 30, "cidade": "Rio de Janeiro"})
rede_social.adicionar_perfil("ana789", {"nome": "Ana", "idade": 22, "cidade": "Belo Horizonte"})

print(rede_social.recuperar_perfil("joao123"))
print(rede_social.recuperar_perfil("maria456"))
print(rede_social.recuperar_perfil("carlos000"))
