import random
import time

isbn_lista = sorted(random.sample(range(10**12, 10**13), 100000))
isbn_procurado = isbn_lista[random.randint(0, 99999)]

def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1
    iteracoes = 0

    while inicio <= fim:
        iteracoes += 1
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return meio, iteracoes
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1, iteracoes

def busca_linear(lista, alvo):
    iteracoes = 0
    for i in range(len(lista)):
        iteracoes += 1
        if lista[i] == alvo:
            return i, iteracoes
    return -1, iteracoes

inicio_binaria = time.time()
indice_binaria, iteracoes_binaria = busca_binaria(isbn_lista, isbn_procurado)
fim_binaria = time.time()

inicio_linear = time.time()
indice_linear, iteracoes_linear = busca_linear(isbn_lista, isbn_procurado)
fim_linear = time.time()

print(f"ISBN procurado: {isbn_procurado}")
print(f"--- Busca Binária ---")
print(f"Índice encontrado: {indice_binaria}, Iterações: {iteracoes_binaria}, Tempo: {fim_binaria - inicio_binaria:.6f} segundos")
print(f"--- Busca Linear ---")
print(f"Índice encontrado: {indice_linear}, Iterações: {iteracoes_linear}, Tempo: {fim_linear - inicio_linear:.6f} segundos")
