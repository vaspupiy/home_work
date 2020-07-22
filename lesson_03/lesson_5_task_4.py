from googletrans import Translator

file_translator = Translator()
with open('translate.txt', 'r+', encoding='utf-8') as f:
    sentences = f.read()
    result = file_translator.translate(sentences, src='en', dest='ru')
    f.write(result.text)