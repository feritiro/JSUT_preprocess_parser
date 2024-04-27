import os
import shutil
# Move .wav files
# Diretório de origem
diretorio_origem = r'C:\Users\ferni\Downloads\jsut'

# Diretório de destino
diretorio_destino = r'C:\Users\ferni\Downloads\jsut'

# Itera sobre os diretórios de jvs001 até jvs020
for i in range(1, 21):
    # Adiciona zeros à esquerda para garantir três dígitos
    idx = str(i).zfill(3)

    diretorio_atual = os.path.join(
        diretorio_origem, f'jvs{idx}\parallel100\wav24kHz16bit')

    # Verifica se o diretório de origem existe
    if os.path.exists(diretorio_atual):
        # Move os arquivos para o diretório de destino
        for nome_arquivo in os.listdir(diretorio_atual):
            caminho_origem = os.path.join(diretorio_atual, nome_arquivo)
            caminho_destino = os.path.join(diretorio_destino, nome_arquivo)
            shutil.move(caminho_origem, caminho_destino)

print("Arquivos movidos com sucesso para o diretório de destino!")
