import os
import pyaes

# Função para descriptografar um arquivo
def descriptar(arquivo, chave):
    try:
        # Lê o arquivo criptografado
        with open(arquivo, 'rb') as entrada:
            dados_criptografados = entrada.read()

        # Ajusta a chave 
        chave = chave[:16]

        # Inicializa o AES no modo CTR
        aes = pyaes.AESModeOfOperationCTR(chave.encode('utf-8'))

        # Descriptografa os dados
        dados_descriptografados = aes.decrypt(dados_criptografados)

        # Sobrescreve o arquivo original com os dados descriptografados
        with open(arquivo, 'wb') as saida:
            saida.write(dados_descriptografados)

        print(f"O arquivo foi descriptografado com sucesso, está salvo como {arquivo}")
    except Exception as erro:
        print(f"Erro inesperado ao descriptografar o arquivo: {erro}/n Tente novamente!")

# Define o arquivo criptografado e a chave
filename = "teste.txt"  # Certifique-se de que esse arquivo foi criptografado previamente
chave = "SantanderCiberseguranca2024#2"

# Chama a função para descriptografar o arquivo
descriptar(filename, chave)
