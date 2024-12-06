contatos = [
    {"nome": "João", "telefone": "(11) 91234-5678"},
    {"nome": "Maria", "telefone": "(21) 99876-5432"},
    {"nome": "Pedro", "telefone": "(31) 98765-4321"},
    {"nome": "Ana", "telefone": "(41) 92345-6789"},
    {"nome": "Carlos", "telefone": "(51) 93210-1111"},
    {"nome": "Fernanda", "telefone": "(61) 94567-8901"},
    {"nome": "Lucas", "telefone": "(71) 91122-3344"},
    {"nome": "Juliana", "telefone": "(81) 91233-4455"},
    {"nome": "Rafael", "telefone": "(91) 99988-7766"},
    {"nome": "Gabriela", "telefone": "(51) 98877-6655"},
    {"nome": "Renata", "telefone": "(31) 95678-1234"},
    {"nome": "Thiago", "telefone": "(11) 94433-5566"},
    {"nome": "Beatriz", "telefone": "(21) 92211-3344"},
    {"nome": "Eduardo", "telefone": "(41) 93123-4567"},
    {"nome": "Carolina", "telefone": "(61) 94876-5432"},
    {"nome": "Felipe", "telefone": "(71) 91199-8877"},
    {"nome": "Patrícia", "telefone": "(81) 92344-5566"},
    {"nome": "Bruno", "telefone": "(91) 91188-7766"},
    {"nome": "Sabrina", "telefone": "(51) 95555-4444"},
    {"nome": "Leandro", "telefone": "(31) 94444-3333"},
]

def busca_contato(lista, nome_procurado):
    for contato in lista:
        if contato["nome"].lower() == nome_procurado.lower():
            return contato["telefone"]
    return None

nome_a_procurar = "Felipe"
telefone = busca_contato(contatos, nome_a_procurar)

if telefone:
    print(f"Contato encontrado: {nome_a_procurar}, Telefone: {telefone}")
else:
    print(f"Contato '{nome_a_procurar}' não encontrado.")
