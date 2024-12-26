import os
import pyaes

# Função para criptografar um arquivo
def encriptar(arquivo, chave):
    try:
        # Lê o arquivo original
        with open(arquivo, 'rb') as entrada:
            dados = entrada.read()

        # Ajusta a chave para 16 bytes
        chave = chave[:16]

        # Inicializa o AES no modo CTR
        aes = pyaes.AESModeOfOperationCTR(chave.encode('utf-8'))

        # Criptografa os dados
        dados_criptografados = aes.encrypt(dados)

        # Salva os dados criptografados em um novo arquivo
        arquivo_saida = arquivo
        with open(arquivo_saida, 'wb') as saida:
            saida.write(dados_criptografados)

        print(f"O arquivo foi criptografado com sucesso, está salvo como: {arquivo_saida}")
    except Exception as erro:
        print(f"Erro inesperado ao criptografar o arquivo: {erro}\n Tente novamente!")

# Define o arquivo e a chave
filename = "teste.txt"  # Certifique-se de que esse arquivo existe na mesma pasta do script
chave = "SantanderCiberseguranca2024#2"

# Chama a função para criptografar o arquivo
encriptar(filename, chave)
