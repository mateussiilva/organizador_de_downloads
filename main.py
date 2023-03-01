


import os 
import shutil

paste_padrao = "arquivos"

path_destino = "/home/mateus/Downloads/"
path_origem = os.getcwd()

pastas = {
    "deb": paste_padrao + "Deb",
    "imgs": "Imagens",
    "torrents": paste_padrao + "Torrent",
    "tmp": paste_padrao + "Tmp",
    "pdf": paste_padrao + "PDF",
}


def get_pasta_existentes():
    global path_destino
    p_exists = []
    for dado in os.listdir(path_destino):
        if os.path.isdir(os.path.join(path_destino, dado)):
            p_exists.append(dado)
        
    return p_exists

pastas_existentes = get_pasta_existentes()

os.chdir(path_destino)
for pasta in pastas.values():
    if pasta not in pastas_existentes:
    
        # print("Essa pasta não existe",pasta)
        print()
        break
    else:
        for p in pastas_existentes:
            if p != pasta:
                print(p)
    
                
        
os.chdir(path_origem)