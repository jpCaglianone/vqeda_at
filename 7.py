def verificar_duplicatas(lista):
    elementos_vistos = set()
    for elemento in lista:
        if elemento in elementos_vistos:
            return True
        elementos_vistos.add(elemento)
    return False

lista = [1, 2, 3, 4, 5, 6, 3]
print(verificar_duplicatas(lista))

lista_sem_duplicatas = [1, 2, 3, 4, 5, 6]
print(verificar_duplicatas(lista_sem_duplicatas))
