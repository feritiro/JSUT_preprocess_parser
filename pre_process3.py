import os
import shutil

# Diretório de origem
diretorio_origem = r'C:\Users\ferni\Downloads\arqtexto'
diretorio_destino = r'C:\Users\ferni\Downloads\jsut'

# Lista de sufixos desejados
sufixos = ['jvs001', 'jvs002', 'jvs003', 'jvs004', 'jvs005',
           'jvs006', 'jvs007', 'jvs008', 'jvs009', 'jvs010',
           'jvs011', 'jvs012', 'jvs013', 'jvs014', 'jvs015',
           'jvs016', 'jvs017', 'jvs018', 'jvs019', 'jvs020']

# Itera sobre os arquivos .txt no diretório de origem
for nome_arquivo in os.listdir(diretorio_origem):
    if nome_arquivo.endswith('.txt'):
        # Caminho completo do arquivo de origem
        caminho_origem = os.path.join(diretorio_origem, nome_arquivo)

        # Obtém o nome do arquivo sem a extensão
        nome_sem_extensao = os.path.splitext(nome_arquivo)[0]

        # Cria cópias do arquivo com os sufixos desejados no diretório de destino
        for sufixo in sufixos:
            novo_nome = f'{nome_sem_extensao}_{sufixo}.txt'
            caminho_destino = os.path.join(diretorio_destino, novo_nome)
            shutil.copy(caminho_origem, caminho_destino)

print("Cópias dos arquivos criadas com sucesso no diretório de destino!")
