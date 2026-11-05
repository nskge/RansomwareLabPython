import os
from cryptography.fernet import Fernet

def carregarChave():
    return open("chave.key", "rb").read()

def descriptografarArquivos(arquivo,chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dadosCriptografados = file.read()
    dadosDescriptografados = f.decrypt(dadosCriptografados)
    with open(arquivo, "wb") as file:
        file.write(dadosDescriptografados)

def encontraArquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransomware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

def main():
    chave = carregarChave()
    arquivos = encontraArquivos("test_files")
    for arquivo in arquivos:
        descriptografarArquivos(arquivo, chave)

    print("Arquivos descriptografados com sucesso!")

if __name__ == "__main__":
    main()

