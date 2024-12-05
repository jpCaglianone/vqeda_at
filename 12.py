import os

def listar_arquivos(caminho):
    arquivos = []

    try:
        for item in os.listdir(caminho):
            caminho_completo = os.path.join(caminho, item)

            if os.path.isfile(caminho_completo):
                arquivos.append(caminho_completo)
            elif os.path.isdir(caminho_completo):
                arquivos.extend(listar_arquivos(caminho_completo))
    except PermissionError:
        pass

    return arquivos

caminho_inicial = "C:\\"
arquivos_encontrados = listar_arquivos(caminho_inicial)

i = 0
for arquivo in arquivos_encontrados:
    if i < 1000:
        print(arquivo)
        i = i + 1
    else:
        break