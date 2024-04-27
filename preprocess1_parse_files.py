import os
# Extrai frases e cria na pasta ___
# Diretório de origem
diretorio_origem = r'C:\Users\ferni\Downloads\jsut'

# Diretório de destino
diretorio_destino = r'C:\Users\ferni\Downloads\jsut'

# Itera sobre os diretórios jvs{idx}
for root, dirs, files in os.walk(diretorio_origem):
    # Verifica se o diretório contém a pasta parallel100
    if 'parallel100' in dirs:
        # Atualiza o diretório de origem para a pasta parallel100
        diretorio_parallel100 = os.path.join(root, 'parallel100')

        # Itera sobre os arquivos de transcripts_utf8.txt em parallel100
        for nome_arquivo in os.listdir(diretorio_parallel100):
            if nome_arquivo == 'transcripts_utf8.txt':
                caminho_arquivo = os.path.join(
                    diretorio_parallel100, nome_arquivo)

                # Obtém o idx do diretório
                idx = os.path.basename(root).replace('jvs', '')

                # Lê o conteúdo do arquivo e cria um arquivo para cada linha
                with open(caminho_arquivo, 'r', encoding='utf-8') as file:
                    for i, linha in enumerate(file):
                        # Realiza o procedimento de parser, obtendo o texto antes dos ':' (dois pontos)
                        nome_arquivo_destino = linha.split(':', 1)[0].strip()

                        # Cria o nome do arquivo de destino com o sufixo _jvs{idx}
                        nome_arquivo_destino = f'{nome_arquivo_destino}_jvs{idx}.txt'

                        # Caminho completo do arquivo de destino
                        caminho_destino = os.path.join(
                            diretorio_destino, nome_arquivo_destino)

                        # Escreve a frase no arquivo de destino
                        with open(caminho_destino, 'w', encoding='utf-8') as destino:
                            destino.write(
                                f'{linha.split(":", 1)[1].strip()}\n')

                        # print(f"Arquivo criado com sucesso: {caminho_destino}")

print("Frases extraídas e salvas com sucesso!")
