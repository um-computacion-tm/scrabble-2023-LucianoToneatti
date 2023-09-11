from game.scrabble import Scrabble


def main():
    print('Bienvenido')
    while True:
        try:
            player_count = int(input('cantidad de jugadores '))
            if player_count < 2 or player_count > 4:
                raise ValueError
            else:
                break
        except ValueError:
            print('Valor invalido')
    game = Scrabble(player_count)
    print('La cantidad de jugadores es: ' + str(player_count))
    game.next_turn()
    print(f"Turno del jugador 1")
    """word = input('Ingrese palabra: ')
    location_x = input('Ingrese posición X: ')
    location_y = input('Ingrese posición Y: ')
    location = (location_x, location_y)
    orientation = input('Ingrese orientación (V/H): ')
    game.validate_word"""
if __name__ == "__main__":
    main()