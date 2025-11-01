import tkinter as tk
import os
from PIL import Image, ImageTk
import threading

from main_infos_impor import caminho_pasta_download
from main_get_coockies_YT import Verificacao_Pasta
from main_back_download_video_yt import Download
info_pasta_download = caminho_pasta_download

#BOTOES
absolute_path = os.path.dirname(os.path.abspath(__file__))
imagem_recarregar = os.path.join(absolute_path, 'button_YT', 'arrow-refresh-reload-icon-30.png')

def Comando_Download():
    url_do_video = urlVIDEO.get()
    playlist_YT = trueORfalse_playlist.get()
    threading.Thread( target= Download(playlist_YT, url_do_video)).start()

    if playlist_YT == True:
        trueORfalse_playlist.set(False)
def Mudar_pasta_Download():
    newName = Verificacao_Pasta(info_pasta_download, True)
    pasta_download_VIDEO['text'] = newName
telaYt = tk.Tk()
telaYt.title("YouTube")
telaYt.config(bg='SpringGreen3')
telaYt.geometry("230x380")

img = Image.open(imagem_recarregar)
img = img.resize((30, 30))
img_tk = ImageTk.PhotoImage(img)

for i in range(5):
    telaYt.rowconfigure(i, weight=1)

telaYt.columnconfigure(0, weight=1)

urlVIDEO = tk.Entry(telaYt)
urlVIDEO.grid(row=0, column=0, columnspan=3, sticky = 'ew')
urlVIDEO.insert(0,'Digite aqui o link')

download_VIDEO = tk.Button(telaYt, text= 'Download', command=Comando_Download)
download_VIDEO.grid(row=1, column=0, columnspan= 3, sticky= 'NESW')

pasta_download_VIDEO = tk.Label(telaYt, text= Verificacao_Pasta(info_pasta_download, False))
botao_trocar_pasta_download = tk.Button(telaYt, image = img_tk, command= Mudar_pasta_Download)
botao_trocar_pasta_download.grid(row = 2, column = 1, sticky= 'NESW')
pasta_download_VIDEO.grid(row = 2, column = 0, sticky= 'NESW')


trueORfalse_playlist = tk.BooleanVar()
checkList = tk.Checkbutton(telaYt, text = "Baixar playlist", variable = trueORfalse_playlist)
checkList.grid(row = 3, column = 0, sticky= 'NESW')

telaYt.mainloop()

