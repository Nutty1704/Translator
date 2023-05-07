from text import TextTranslator
from word import WordTranslator
import time

class Main:
    def __init__(self) -> None:
        self.run()

    def run(self):
        while True:
            print('1. Translate a text file')
            print('2. Translate a Word document')
            print('3. Exit')
            choice = input('Enter your choice: ')

            if choice == '1':
                TextTranslator()
            elif choice == '2':
                WordTranslator()
            elif choice == '3':
                break
            else:
                print('Invalid choice. Try again.')

            time.sleep(1)


if __name__ == "__main__":
    Main()