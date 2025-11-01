import os

def Criar_Pasta_Para_Formatacao():
    caminho_abso = os.environ.get("USERPROFILE")
    caminho_pasta_criada = f"{caminho_abso}\\Pasta formatação"
    if not os.path.exists(caminho_pasta_criada):
        os.makedirs(caminho_pasta_criada)
        print("Pasta criada com sucesso!")
    else:
        print("Pasta já existente")
    return caminho_pasta_criada

def Get_Itens_Pasta_Pre_Formatacao(caminho_pasta_para_formatacao):
    listaArquivos = {'videos': [], 'thumbnails': []}
    for i in os.listdir(caminho_pasta_para_formatacao):
        if os.path.splitext(i)[1] == '.mp4':
            listaArquivos['videos'].append(os.path.join(caminho_pasta_para_formatacao, i))
        elif os.path.splitext(i)[1] == '.webp':
            listaArquivos['thumbnails'].append(os.path.join(caminho_pasta_para_formatacao, i))
        else:
            os.remove(os.path.join(caminho_pasta_para_formatacao, i))
    return listaArquivos

def Get_Itens_Pasta_Formatada(caminho_pasta_para_formatacao):

    listaArquivos = {'videos': [], 'thumbnails': []}

    for item in os.listdir(caminho_pasta_para_formatacao):
        if os.path.splitext(item)[1] == '.mp4':
            listaArquivos['videos'].append(os.path.join(caminho_pasta_para_formatacao, item))
        elif os.path.splitext(item)[1] == '.png':
            listaArquivos['thumbnails'].append(os.path.join(caminho_pasta_para_formatacao, item))

    return listaArquivos