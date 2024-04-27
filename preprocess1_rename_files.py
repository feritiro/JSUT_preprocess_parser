import os

jsut_dir = r'C:\Users\ferni\Downloads\jsut'
# Rename .wzv files
i_max = 20
i = 1
while (i <= i_max):
    # Diretório dos arquivos .wav
    idx = str(i).zfill(3)
    diretorio = jsut_dir+'\jvs'+idx+'\parallel100\wav24kHz16bit'

    # Itera sobre todos os arquivos no diretório
    for nome_arquivo in os.listdir(diretorio):
        # Verifica se o arquivo é do tipo .wav e possui o padrão VOICEACTRESS100_XXX
        if nome_arquivo.endswith('.wav') and nome_arquivo.startswith('VOICEACTRESS100_'):
            # Separa o número do arquivo
            numero_arquivo = nome_arquivo.split('_')[1].split('.')[
                0]  # Remove a extensão .wav

            # Novo nome do arquivo
            novo_nome = f'VOICEACTRESS100_{numero_arquivo}_jvs'+idx+'.wav'

            # Caminho completo dos arquivos antigo e novo
            caminho_antigo = os.path.join(diretorio, nome_arquivo)
            caminho_novo = os.path.join(diretorio, novo_nome)

            # Renomeia o arquivo
            os.rename(caminho_antigo, caminho_novo)
    i += 1

print("Arquivos renomeados com sucesso!")
