from text import TextTranslator

class Main:
    def __init__(self) -> None:
        self.run()

    def run(self):
        while True:
            print('1. Translate a text file')
            print('2. Exit')
            choice = input('Enter your choice: ')

            if choice == '1':
                TextTranslator()
            elif choice == '2':
                break
            else:
                print('Invalid choice. Try again.')


if __name__ == "__main__":
    Main()