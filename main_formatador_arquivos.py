from main_fomatador_FFmpeg import Formatador_para_PNG, Formatador_input_Thumbnail_YT
import os

def Formatador_Thumb_Youtube(dicionario_Thumb, formato_de_saida):
    listaThumbs = []
    for thumb in dicionario_Thumb['thumbnails']:
        nomeThumb = os.path.splitext(os.path.basename(thumb))[0]
        caminho = os.path.dirname(thumb)
        newCaminho = os.path.join(caminho, nomeThumb)
        newName_Thumb = f"{newCaminho}{formato_de_saida}"
        listaThumbs.append([thumb,newName_Thumb])
        for i in range(len(listaThumbs)):
            Formatador_para_PNG(listaThumbs[i][0],listaThumbs[i][1])

def Formatador_thumbanails_YT_path(dicionario):
    pasta_fomatacao = []

    for video in dicionario['videos']:
        for thumbnail in dicionario['thumbnails']:
            if os.path.splitext(thumbnail)[0] == os.path.splitext(video)[0]:
                print(f"{video} -> {thumbnail}")
                pasta_fomatacao.append(
                    [video, thumbnail, os.path.splitext(video)[0] + '(NEW)' + os.path.splitext(video)[1]])

    for i in range(len(pasta_fomatacao)):
        Formatador_input_Thumbnail_YT(pasta_fomatacao[i][0], pasta_fomatacao[i][1], pasta_fomatacao[i][2])
        os.remove(pasta_fomatacao[i][0]), os.remove(pasta_fomatacao[i][1])
