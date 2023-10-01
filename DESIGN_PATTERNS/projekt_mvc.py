cytaty = (
    'Lepiej zaliczać się do niektórych, niż do wszystkich',
    'Książki są lustrem, widzisz w nich tylko to, co już masz w sobie',
    'Życie jest jak pudełko czekoladek - nigdy nie wiesz, co Cię trafi',
    'Pozbierać jest dzisięć razy trudniej niż rozsypać',
    'Kiedy łamiesz zasady, łam je mocno i na dobre'
)

class QuoteModel:
    def get_quote(self,n):
        try:
            value = cytaty[n]
        except IndexError as err:
            print(f'nie znaleziono {err}')
        else:
            return value


class QuoteTerminalView:
    def show(self,quote):
        print(f'wybrany cytat: "{quote}"')

    def error(self,msg):
        print(f'Błąd: {msg}')

    def select_quote(self):
        return input('Który numer cytatu chcesz wybrać? ')

class QuoteTerminalController:
    def __init__(self):
        self.model = QuoteModel()
        self.view = QuoteTerminalView()

    def run(self):
        valid_input = False
        while not valid_input:
            try:
                n = self.view.select_quote()
                n = int(n)
                valid_input = True

            except ValueError as ve:
                self.view.error(f'niewłaściwy indeks -> {n}')

            quote = self.model.get_quote(n)
            self.view.show(quote)

def main():
    controller = QuoteTerminalController()
    while True:
        controller.run()

if __name__ == '__main__':
    main()


