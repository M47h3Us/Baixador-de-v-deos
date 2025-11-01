import os

#Pasta absoluta do código
caminho_pasta_Absoluta = os.path.dirname(os.path.abspath(__file__))
#Informação da localização do FFmpeg
caminho_FFmpeg_absoluto = os.path.join(caminho_pasta_Absoluta, 'FFmpeg\\ffmpeg.exe')
#Informação da localização dos coockies do google
caminhos_Coockies_absoluto = os.path.join(caminho_pasta_Absoluta, 'CoockiesGoogle\\www.youtube.com_cookies.txt')
caminho_pasta_download = os.path.join(caminho_pasta_Absoluta, 'pasta_selecionada')


def Return_Info_FFmpeg_Local(local_FFmpeg):
    informacao_FFmpeg = local_FFmpeg
    return informacao_FFmpeg
infoLocalizacao_FFmpeg = Return_Info_FFmpeg_Local(caminho_FFmpeg_absoluto)

def Return_Info_Coockies_Local(local_Coockies):
    informacao_Coockies = local_Coockies
    return informacao_Coockies
infoLocalizacao_Coockies = Return_Info_Coockies_Local(caminhos_Coockies_absoluto)