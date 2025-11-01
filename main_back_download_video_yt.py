#Bibliotecas
from yt_dlp import YoutubeDL
import os
from tkinter import filedialog

#Import partes código
from main_formatador_links import formatador_URL_youtube #Garante que o usuário não baixe uma playlist sem querer
from main_infos_impor import infoLocalizacao_FFmpeg, infoLocalizacao_Coockies, caminho_pasta_download   #Localização de onde está os cookies e FFmpeg para o utilizar no código
from criado_pasta_formatacao import Criar_Pasta_Para_Formatacao, Get_Itens_Pasta_Pre_Formatacao, Get_Itens_Pasta_Formatada #Cria a pasta de formatação para formatar os vídeos antes de o entregar
from main_formatador_arquivos import Formatador_Thumb_Youtube, Formatador_thumbanails_YT_path #Formata o vídeo
from main_move_videos_para_new_pasta import move_videos_YT
from main_get_coockies_YT import iniciar
from main_get_coockies_YT import Verificacao_Pasta

#Localização pastas importantes
localizacao_Pasta_download = caminho_pasta_download
localizacao_FFmpeg = infoLocalizacao_FFmpeg
localizacao_Coockies_Google = infoLocalizacao_Coockies

#Imputs básicos para formatação inicial
def Download(playlist, url):
    pasta_de_download = Verificacao_Pasta(localizacao_Pasta_download, False)
    playlist_YT = playlist
    url_Video = url


    #Comandos puxados de outras partes do código

    caminho_pasta_formatacao = Criar_Pasta_Para_Formatacao()

    match playlist_YT:
        case False:
            url_Video = f'{formatador_URL_youtube(url_Video)}'

    formatacao_YT_dlp = {
        'format': 'best',
        'outtmpl': os.path.join(caminho_pasta_formatacao, '%(title)s.%(ext)s'),
        'writethumbnail': True,
        'ffmpeg_location': f'{localizacao_FFmpeg}',
        'nopart': True,
        'cookiefile': f'{localizacao_Coockies_Google}'
    }
    iniciar()
    with YoutubeDL(formatacao_YT_dlp) as ydl: #Requisita o downloado para o youtube
        ydl.download([url_Video])

    caminho_Thumbs_e_Videos_preFormatacao = Get_Itens_Pasta_Pre_Formatacao(caminho_pasta_formatacao)
    Formatador_Thumb_Youtube(caminho_Thumbs_e_Videos_preFormatacao, r'.png')
    caminho_Formatado = Get_Itens_Pasta_Formatada(caminho_pasta_formatacao)
    Formatador_thumbanails_YT_path(caminho_Formatado)
    move_videos_YT(caminho_pasta_formatacao, pasta_de_download)

    print("================================")

