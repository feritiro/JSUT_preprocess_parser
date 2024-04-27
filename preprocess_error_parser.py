import os
# remover characteres
pasta = "C:\\Users\\ferni\\Downloads\\arqtexto"

for nome_arquivo in os.listdir(pasta):
    caminho_arquivo = os.path.join(pasta, nome_arquivo)

    if nome_arquivo.endswith(".txt"):
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()

        # conteudo_modificado = conteudo.replace("風", "フウ")
        conteudo_modificado = conteudo.replace(" ッ", "")

        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo_modificado:
            arquivo_modificado.write(conteudo_modificado)

        # print(f"Arquivo modificado: {nome_arquivo}")
