from game.scrabble import Scrabble

class ScrabbleGame: 

    def __init__(self):
        self.player_count = self.get_valid_player_count()    
    def get_valid_player_count(self):
            while True:
                player_count = self.get_player_input()
                if 2 <= player_count <= 4:
                    return player_count
                print('Valor inválido. Debe ser un número entre 2 y 4.')    
    def get_player_input(self):
        try:
            return int(input('Cantidad de jugadores: '))
        except ValueError:
            print('Valor inválido. Debe ser un número.')    
    def welcome_message(self):
        print('Bienvenido')    
    def display_player_count(self):
        print(f'La cantidad de jugadores es: {self.player_count}')    
    def next_player_turn(self, player_number):
        print(f"Turno del jugador {player_number}")    
    def run(self):
        self.welcome_message()
        self.display_player_count()        
        game = Scrabble(self.player_count)
        self.next_player_turn(1)
if __name__ == "__main__":
    scrabble_game = ScrabbleGame()
    scrabble_game.run()