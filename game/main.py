from game.scrabble import Scrabble


def main():
    player_count = int(input('cantidad de jugadores'))
    game = Scrabble(player_count)
    print('La cantidad de jugadores es: ' + str(player_count))