import subprocess
import os
from main_infos_impor import caminho_FFmpeg_absoluto

caminhoFFmpeg = caminho_FFmpeg_absoluto
def Formatador_para_MP4(arquivo,formatoDesaida, caminhoDesaida):

    arquivo_sem_extensao = os.path.splitext(os.path.basename(arquivo)) #Extensão retirada
    arquivo_com_nova_extensao = arquivo_sem_extensao[0] + formatoDesaida #Extensão trocada
    arquivo_com_novo_caminho = os.path.join(caminhoDesaida, arquivo_com_nova_extensao) #Caminho trocado

    comando = [
        caminhoFFmpeg,
        "-y",
        "-i", arquivo,
        "-c", "copy",
        arquivo_com_novo_caminho
    ]

    try:
        subprocess.run(comando, check=True)
        os.remove(arquivo)
        print(f"Convertido com sucesso para: {arquivo_com_novo_caminho}")
    except subprocess.CalledProcessError:
        print("Erro ao converter o arquivo.")
    print("Convertido com sucesso!")

    return arquivo_com_novo_caminho
def Formatador_para_PNG(caminho_original, caminho_novo):

    comando = [
        caminhoFFmpeg,
        "-y",  # sobrescreve sem perguntar
        "-i", caminho_original,
        caminho_novo
    ]

    try:
        subprocess.run(comando, check=True)
        print(f"Convertido com sucesso para: {caminho_novo}")
        os.remove(caminho_original)

    except subprocess.CalledProcessError:
        print("Erro ao converter o arquivo.")
    print("Convertido com sucesso!")

    return caminho_novo

def Formatador_input_Thumbnail_YT(video,thumb,formato_de_saida):

    comando = [
        caminhoFFmpeg,
        "-i", video,
        "-y",
        "-i", thumb,
        "-map", "0",
        "-map", "1",
        "-c", "copy",
        "-disposition:v:1", "attached_pic",
        formato_de_saida
    ]

    subprocess.run(comando)