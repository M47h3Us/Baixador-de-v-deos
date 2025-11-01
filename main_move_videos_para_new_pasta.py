import os, shutil

def move_videos_YT(caminho_antigo, caminho_novo):

    for i in os.listdir(caminho_antigo):
        new_path = os.path.join(caminho_novo, os.path.basename(i))
        shutil.move(os.path.join(caminho_antigo,i), new_path)
