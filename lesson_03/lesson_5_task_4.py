from googletrans import Translator

file_translator = Translator()
with open('text_4.txt', 'r', encoding='utf-8') as f:
    sentences = f.read()
    result = file_translator.translate(sentences, src='en', dest='ru')

with open('translate_4.txt', 'w', encoding='utf-8') as f:
    f.write(result.text)
