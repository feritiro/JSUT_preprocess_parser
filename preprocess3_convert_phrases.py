from pykakasi import kakasi
import os


def remover_caracteres(frase):
    caracteres_para_remover = ["ー", "、", "。", "っ", "ッ"]
    for caractere in caracteres_para_remover:
        frase = frase.replace(caractere, "")
    return frase


def converter_para_hiragana(frase):
    frase_sem_caracteres = remover_caracteres(frase)
    kakasi_obj = kakasi()
    kakasi_obj.setMode('J', 'H')  # 'J' para japonês, 'H' para hiragana
    conv = kakasi_obj.getConverter()
    hiragana = conv.do(frase_sem_caracteres)
    return hiragana


def converter_katakana_para_hiragana(frase):
    kakasi_obj = kakasi()
    kakasi_obj.setMode('K', 'H')  # 'K' para katakana, 'H' para hiragana
    conv = kakasi_obj.getConverter()
    hiragana = conv.do(frase)
    return hiragana


def converter_kanji_para_katakana(frase):
    kakasi_obj = kakasi()
    kakasi_obj.setMode('J', 'K')  # 'J' para japonês, 'K' para katakana
    conv = kakasi_obj.getConverter()
    katakana = conv.do(frase)
    return katakana


def split_fonemas_jp(text, fonema_list):
    fonemas = []
    i = 0
    while i < len(text):
        found = False
        for fonema in fonema_list:
            if text[i:i+len(fonema)] == fonema:
                fonemas.append(fonema)
                i += len(fonema)
                found = True
                break
        if not found:
            fonemas.append(text[i])
            i += 1

    return fonemas


# Lista de fonemas
fonema_list = [

    'きゃん', 'きゅん', 'きょん',
    'しゃん', 'しゅん', 'しょん',
    'ちゃん', 'ちゅん', 'ちょん',
    'にゃん', 'にゅん', 'にょん',
    'ひゃん', 'ひゅん', 'ひょん',
    'みゃん', 'みゅん', 'みょん',
    'りゃん', 'りゅん', 'りょん',
    'ぎゃん', 'ぎゅん', 'ぎょん',
    'じゃん', 'じゅん', 'じょん',
    'びゃん', 'びゅん', 'びょん',
    'ぴゃん', 'ぴゅん', 'ぴょん',

    'キャン', 'キュン', 'キョン',
    'シャン', 'シュン', 'ション',
    'チャン', 'チュン', 'チョン',
    'ニャン', 'ニュン', 'ニョン',
    'ヒャン', 'ヒュン', 'ヒョン',
    'ミャン', 'ミュン', 'ミョン',
    'リャン', 'リュン', 'リョン',
    'ギャン', 'ギュン', 'ギョン',
    'ジャン', 'ジュン', 'ジョン',
    'ビャン', 'ビュン', 'ビョン',
    'ピャン', 'ピュン', 'ピョン',

    'くぁん', 'くぃん', 'くぇん', 'くぉん',
    'すぁん', 'すぃん', 'すぇん', 'すぉん',
    'つぁん', 'つぃん', 'つぇん', 'つぉん',
    'ぬぁん', 'ぬぃん', 'ぬぇん', 'ぬぉん',
    'ふぁん', 'ふぃん', 'ふぇん', 'ふぉん',

    'クァン', 'クィン', 'クェン', 'クォン',
    'スァン', 'スィン', 'スェン', 'スォン',
    'ツァン', 'ツィン', 'ツェン', 'ツォン',
    'ヌァン', 'ヌィン', 'ヌェン', 'ヌォン',
    'ファン', 'フィン', 'フェン', 'フォン',

    'ファン', 'フィン', 'フェン', 'フォン', 'ウェン', 'ウォン',
    'ヴァン', 'ヴィン', 'ヴェン', 'ヴォン', 'ヴャン', 'ヴュン', 'ヴョン',
    'シェン', 'ディン', 'シェン', 'ジェン',
    'ディン', 'チェン', 'ルィン', 'ティン',

    'きゃ', 'きゅ', 'きょ',
    'しゃ', 'しゅ', 'しょ',
    'ちゃ', 'ちゅ', 'ちょ',
    'にゃ', 'にゅ', 'にょ',
    'ひゃ', 'ひゅ', 'ひょ',
    'みゃ', 'みゅ', 'みょ',
    'りゃ', 'りゅ', 'りょ',
    'ぎゃ', 'ぎゅ', 'ぎょ',
    'じゃ', 'じゅ', 'じょ',
    'びゃ', 'びゅ', 'びょ',
    'ぴゃ', 'ぴゅ', 'ぴょ',

    'キャ', 'キュ', 'キョ',
    'シャ', 'シュ', 'ショ',
    'チャ', 'チュ', 'チョ',
    'ニャ', 'ニュ', 'ニョ',
    'ヒャ', 'ヒュ', 'ヒョ',
    'ミャ', 'ミュ', 'ミョ',
    'リャ', 'リュ', 'リョ',
    'ギャ', 'ギュ', 'ギョ',
    'ジャ', 'ジュ', 'ジョ',
    'ビャ', 'ビュ', 'ビョ',
    'ピャ', 'ピュ', 'ピョ',

    'シェ', 'ジェ', 'ディ', 'チェ', 'ティ', 'ルィ',
    'ヴァ', 'ヴィ', 'ヴェ', 'ヴォ', 'ヴャ', 'ヴュ', 'ヴョ',
    'ウェ', 'ウォ',

    'くぁ', 'くぃ', 'くぇ', 'くぉ',
    'すぁ', 'すぃ', 'すぇ', 'すぉ',
    'つぁ', 'つぃ', 'つぇ', 'つぉ',
    'ぬぁ', 'ぬぃ', 'ぬぇ', 'ぬぉ',
    'ふぁ', 'ふぃ', 'ふぇ', 'ふぉ',

    'クァ', 'クィ', 'クェ', 'クォ',
    'スァ', 'スィ', 'スェ', 'スォ',
    'ツァ', 'ツィ', 'ツェ', 'ツォ',
    'ヌァ', 'ヌィ', 'ヌェ', 'ヌォ',
    'ファ', 'フィ', 'フェ', 'フォ',

    'あん', 'いん', 'うん', 'えん', 'おん',
    'かん', 'きん', 'くん', 'けん', 'こん',
    'さん', 'しん', 'すん', 'せん', 'そん',
    'たん', 'ちん', 'つん', 'てん', 'とん',
    'なん', 'にん', 'ぬん', 'ねん', 'のん',
    'はん', 'ひん', 'ふん', 'へん', 'ほん',
    'まん', 'みん', 'むん', 'めん', 'もん',
    'やん', 'ゆん', 'よん',
    'らん', 'りん', 'るん', 'れん', 'ろん',
    'わん',
    'がん', 'ぎん', 'ぐん', 'げん', 'ごん',
    'ざん', 'じん', 'ずん', 'ぜん', 'ぞん',
    'だん', 'ぢん', 'づん', 'でん', 'どん',
    'ばん', 'びん', 'ぶん', 'べん', 'ぼん',
    'ぱん', 'ぴん', 'ぷん', 'ぺん', 'ぽん',

    'アン', 'イン', 'ウン', 'エン', 'オン',
    'カン', 'キン', 'クン', 'ケン', 'コン',
    'サン', 'シン', 'スン', 'セン', 'ソン',
    'タン', 'チン', 'ツン', 'テン', 'トン',
    'ナン', 'ニン', 'ヌン', 'ネン', 'ノン',
    'ハン', 'ヒン', 'フン', 'ヘン', 'ホン',
    'マン', 'ミン', 'ムン', 'メン', 'モン',
    'ヤン', 'ユン', 'ヨン',
    'ラン', 'リン', 'ルン', 'レン', 'ロン',
    'ワン',
    'ガン', 'ギン', 'グン', 'ゲン', 'ゴン',
    'ザン', 'ジン', 'ズン', 'ゼン', 'ゾン',
    'ダン', 'ヂン', 'ヅン', 'デン', 'ドン',
    'バン', 'ビン', 'ブン', 'ベン', 'ボン',
    'パン', 'ピン', 'プン', 'ペン', 'ポン',

    'あ', 'い', 'う', 'え', 'お',
    'か', 'き', 'く', 'け', 'こ',
    'さ', 'し', 'す', 'せ', 'そ',
    'た', 'ち', 'つ', 'て', 'と',
    'な', 'に', 'ぬ', 'ね', 'の',
    'は', 'ひ', 'ふ', 'へ', 'ほ',
    'ま', 'み', 'む', 'め', 'も',
    'や', 'ゆ', 'よ',
    'ら', 'り', 'る', 'れ', 'ろ',
    'わ', 'を', 'ん',
    'が', 'ぎ', 'ぐ', 'げ', 'ご',
    'ざ', 'じ', 'ず', 'ぜ', 'ぞ',
    'だ', 'ぢ', 'づ', 'で', 'ど',
    'ば', 'び', 'ぶ', 'べ', 'ぼ',
    'ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ',

    'ア', 'イ', 'ウ', 'エ', 'オ',
    'カ', 'キ', 'ク', 'ケ', 'コ',
    'サ', 'シ', 'ス', 'セ', 'ソ',
    'タ', 'チ', 'ツ', 'テ', 'ト',
    'ナ', 'ニ', 'ヌ', 'ネ', 'ノ',
    'ハ', 'ヒ', 'フ', 'ヘ', 'ホ',
    'マ', 'ミ', 'ム', 'メ', 'モ',
    'ヤ', 'ユ', 'ヨ',
    'ラ', 'リ', 'ル', 'レ', 'ロ',
    'ワ', 'ヲ', 'ン',
    'ガ', 'ギ', 'グ', 'ゲ', 'ゴ',
    'ザ', 'ジ', 'ズ', 'ゼ', 'ゾ',
    'ダ', 'ヂ', 'ヅ', 'デ', 'ド',
    'バ', 'ビ', 'ブ', 'ベ', 'ボ',
    'パ', 'ピ', 'プ', 'ペ', 'ポ',

    'ヴ',
    # ... adicione outras entradas conforme necessário

]


def processar_arquivo(caminho_arquivo):
    # Ler o conteúdo do arquivo
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        linha = arquivo.readline().strip()

    # Remover caracteres antes de converter
    frase_sem_caracteres = remover_caracteres(linha)

    # Converter a frase para hiragana
    # frase_em_hiragana = converter_para_hiragana(frase_sem_caracteres)
    # frase_em_hiragana = converter_katakana_para_hiragana(frase_em_hiragana)
    frase_kana = converter_kanji_para_katakana(frase_sem_caracteres)
    fonemas_separados = split_fonemas_jp(frase_kana, fonema_list)

    # Escrever a frase em hiragana de volta no arquivo
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(" ".join(fonemas_separados))


# Diretório de entrada para os arquivos a serem processados
diretorio_entrada = r'C:\Users\ferni\Downloads\jsut2'

# Iterar sobre os arquivos no diretório de entrada
for nome_arquivo in os.listdir(diretorio_entrada):
    if nome_arquivo.endswith(".txt"):
        caminho_arquivo = os.path.join(diretorio_entrada, nome_arquivo)
        processar_arquivo(caminho_arquivo)
