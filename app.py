from pokemons import get_pokemon
from batalla import iniciar_batalla

def main():
    print("Bienvenido al juego de Pokémon!")
    nombre_pokemon = input("Elige tu Pokémon (Charmander, Squirtle, Bulbasaur): ").strip().lower()
    player_pokemon = get_pokemon(nombre_pokemon)

    if not player_pokemon:
        print("Pokémon no válido. El juego se cerrará.")
        return

    print(f"Has elegido: {player_pokemon['name']} (HP: {player_pokemon['hp']})")
    
    while True:
        print("\n¿Quieres buscar un Pokémon salvaje? (si/no)")
        opcion = input().strip().lower()
        if opcion == "si":
            iniciar_batalla(player_pokemon)
        elif opcion == "no":
            print("Gracias por jugar!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
