from game.scrabble import Scrabble
def get_player_count():
    while True:
        try:
            player_count = int(input('Cantidad de jugadores: '))
            if 2 <= player_count <= 4:
                return player_count
            else:
                print('Valor inválido. Debe ser un número entre 2 y 4.')        
        except ValueError:
            print('Valor inválido. Debe ser un número entre 2 y 4.')
def main():
    print('Bienvenido')
    player_count = get_player_count()    
    game = Scrabble(player_count)
    print(f'La cantidad de jugadores es: {player_count}')
    game.next_turn()
    print(f"Turno del jugador 1")
if __name__ == "__main__":
    main()
