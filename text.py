import os
from googletrans import Translator
from util import get_language_code

class TextTranslator:
    def __init__(self):
        self.translator = Translator()
        self.translate()

    def get_file_path(self) -> None:
        while True:
            file_path = input('Enter the file path: ')
            if os.path.exists(file_path):
                if file_path.endswith('.txt'):
                    return file_path
                else:
                    print('Invalid file extension. Try again.')
            else:
                print('Invalid file path. Try again.')

    def translate(self) -> None:
        file_path = self.get_file_path()
        lang_code = self.get_language_code()
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        translated_text = self.translator.translate(text, dest=lang_code).text

        # create a new file with the translated text
        new_path = file_path.rstrip('.txt') + f'-{lang_code}.txt'

        with open(new_path, 'w', encoding='utf-8') as f:
            f.write(translated_text)

        print('Translation complete.')

    def get_language_code(self) -> str:
        while True:
            lang = input('Enter the language: ')
            lang_code = get_language_code(lang)

            if lang_code:
                return lang_code
            else:
                print('Invalid language. Try again.')

    
    def run(self) -> None:
        self.get_file_path()
        self.get