from pokemons import get_pokemon, get_wild_pokemon
from batalla import iniciar_batalla, batalla_con_lider

def main():
    print("Bienvenido al juego de Pokémon!")
    nombre_pokemon = input("Elige tu Pokémon (Charmander, Squirtle, Bulbasaur): ").strip().lower()
    player_pokemon = get_pokemon(nombre_pokemon)
    if not player_pokemon:
        print("Pokémon no válido. El juego se cerrará.")
        return
    print(f"Has elegido: {player_pokemon['name']} (HP: {player_pokemon['hp']})")
    # Mapeo de opciones a funciones
    opciones = {
        'si': lambda: iniciar_batalla(player_pokemon),
        'no': lambda: print("Gracias por jugar!")
    }
    while True:
        print("\n¿Quieres buscar un Pokémon salvaje? (si/no)")
        opcion = input().strip().lower() 
        # Ejecutar la opción seleccionada si es válida
        if opcion in opciones:
            opciones[opcion]()
            if opcion == 'no':
                break
            # Lógica de evolución
            if player_pokemon['level'] >= 16:
                print(f"¡{player_pokemon['name']} ha alcanzado el nivel de evolución!")
                evolver = input("¿Quieres evolucionar? (si/no): ").strip().lower()
                if evolver == "si":
                    player_pokemon = evolver_pokemon(player_pokemon)
                    print(f"{player_pokemon['name']} ha evolucionado!")
                batalla_con_lider(player_pokemon)
        else:
            print("Opción no válida.")

def evolver_pokemon(pokemon):
    if pokemon['name'] == 'charmander':
        return get_pokemon('charmeleon')
    if pokemon['name'] == 'squirtle':
        return get_pokemon('wartortle')
    if pokemon['name'] == 'bulbasaur':
        return get_pokemon('ivysaur')
    return pokemon  # Sin evolución

if __name__ == "__main__":
    main()
