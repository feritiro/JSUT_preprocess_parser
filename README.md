# Japanese Mora-Based Preprocessing Parser

This project implements a preprocessing tool that converts Japanese sentences into space-separated mora (or pseudo-mora) units. It is designed for tasks such as phoneme alignment, lip-sync animation, and speech synthesis where fine-grained control over syllable-like units is needed. *The conversion is customized for my objectives.

## Example 

Input: コンピュータゲームのメーカーや、業界団体などに関連する人物のカテゴリ。

Output: コン ピュ タ ゲ ム ノ メ カ ヤ ギョ ウ カ イ ダン タ イ ナ ド ニ カン レン ス ル ジン ブ ツ ノ カ テ ゴ リ

Output2: k on p i u t a g e m u n o m e k a i a g y o u k a i d an t a i n a d o n i k an ren s u ru jin b u ts u n o k a t e g o ri

## Features

- Parses Japanese text into units approximating morae (音拍)
- Strips punctuation and unwanted symbols
- Converts complex katakana combinations into component moras (e.g., コンピュータ → コン ピュ タ)
- Useful for:
  - Lip-sync animation
  - Phoneme-level TTS
  - Language modeling
  - Forced alignment preprocessing

---
## Implementation Details

- Language: Python 3.8+
- Dependencies: pykakasi 
- Conversion based on dictionary table

---
