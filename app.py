
import os 
import pprint
import shutil


def criar_pasta(dir_padrao, name_dir):
    name_paste = os.path.join(dir_padrao,name_dir)
    try:
        os.mkdir(name_paste)
        print("PASTA CRIADA COM SUCESSO")
    except FileExistsError:
        print("Pasta já existe")
    except Exception as error:
        print("NÃO CONSEGUE CRIAR A PASTA\n")
        print(error)
    return name_paste

def separador_de_extensao(lista_arquivos:str) -> set:
    exetensoes_disponiveis = set()
    for arquivo in lista_arquivos:
        incio = arquivo.rfind('.') + 1 
        extensao = arquivo[incio:]
        exetensoes_disponiveis.add(extensao)
    
    return exetensoes_disponiveis

def imprimir(valor):
    pprint.pprint(valor)


def mover_arquivos(destino,path_arquivos):
    try:
        shutil.move(src=path_arquivos, dst=destino)
    except Exception as e:
        print(e)
        
        
def pegar_extensao(nome_arquivo):
    exte = nome_arquivo.rfind('.') + 1
    return nome_arquivo[exte:]


    
PATH_DESTINY = '/home/mateussiilva/Downloads/'
arquivos_separados = dict()


# NAVEGA ATÉ O DESTINO
os.chdir(PATH_DESTINY)


lista_arquivos = [file for file in os.listdir(os.getcwd()) if os.path.isfile(file)]
diretorios_existentes = [paste for paste in os.listdir(os.getcwd()) if os.path.isdir(paste)]

nomes_extensoes = separador_de_extensao(lista_arquivos=lista_arquivos)
for nome in nomes_extensoes:
    arquivos_separados[str(nome)] = []
# print(arquivos_separados)

for chave in arquivos_separados.keys():
    for arquivo in lista_arquivos:
        if pegar_extensao(arquivo) == chave:
            arquivos_separados[chave].append(arquivo)
    

pasta_de_arquivos = list()

for nome in nomes_extensoes:
    nome_pasta = 'arquivos' + nome.title()
    if nome_pasta not in diretorios_existentes:
        pasta = criar_pasta(PATH_DESTINY,nome_pasta)
        pasta_de_arquivos.append(pasta)

for valor in pasta_de_arquivos:
    print(valor)
    









# print(*lista_arquivos)