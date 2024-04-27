def split_fonemas_jp(text, fonema_list):
    # Separar os caracteres japoneses e aplicar o mapeamento
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
    # ... adicione outras entradas conforme necessário

]

# Exemplo de uso
input_text = "またとうじのようにごだいみょう"
fonemas_separados = split_fonemas_jp(input_text, fonema_list)

# Imprimir os fonemas separados
print(" ".join(fonemas_separados))
