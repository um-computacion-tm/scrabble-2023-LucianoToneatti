from game.scrabble import Scrabble

class Main:
    def __init__(self):
        print('Saludos y bienvenidos')
        self.player_count = self.get_player_count()
        self.game = Scrabble(self.player_count)
    def valid_player_count(self,player_count):
        try:
            count = int(player_count)
            if 2<= count <= 4:
                return True
        except ValueError:
            pass
            return False
    def get_player_count(self):
        while True:
            player_count = input('Número de participantes es:')
            if self.valid_player_count(player_count) is True:
                return int(player_count)
            print('Valor ingresado no valido')
    def play(self):
        print(f'Número de participantes es: {self.player_count}')
        self.game.next_turn()
        print(f"Turno del participante 1")

if __name__ == "__main__":
    main = Main()
    main.play()