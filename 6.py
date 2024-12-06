import random
import time

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

lista_1000 = [random.randint(1, 10000) for _ in range(1000)]
lista_10000 = [random.randint(1, 10000) for _ in range(10000)]
lista_100000 = [random.randint(1, 10000) for _ in range(100000)]

inicio_1000 = time.time()
bubble_sort(lista_1000)
fim_1000 = time.time()
print(f"Tempo para ordenar 1.000 elementos: {fim_1000 - inicio_1000:.4f} segundos")

inicio_10000 = time.time()
bubble_sort(lista_10000)
fim_10000 = time.time()
print(f"Tempo para ordenar 10.000 elementos: {fim_10000 - inicio_10000:.4f} segundos")

inicio_100000 = time.time()
bubble_sort(lista_100000)
fim_100000 = time.time()
print(f"Tempo para ordenar 10.0000 elementos: {fim_100000 - inicio_100000:.4f} segundos")