import os

def listar_arquivos(diretorio):
    for nome in os.listdir(diretorio):
        caminho = os.path.join(diretorio, nome)
        try:
            if os.path.isdir(caminho):
                listar_arquivos(caminho)
            else:
                print(caminho)
        except PermissionError:
            pass

def main():
    listar_arquivos('C:/Users/')

if __name__ == '__main__':
    main()
