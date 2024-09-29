import random
from pokemons import get_wild_pokemon

def iniciar_batalla(player):
    wild_pokemon = get_wild_pokemon()
    print(f"¡Te encontraste con un {wild_pokemon['name']}! (HP: {wild_pokemon['hp']})")
    
    while player['hp'] > 0 and wild_pokemon['hp'] > 0:
        # Turno del jugador
        action = input("Elige tu acción: (1) Atacar (2) Huir: ")
        if action == "1":
            damage = random.randint(5, player['attack'])
            wild_pokemon['hp'] -= damage
            print(f"Atacas a {wild_pokemon['name']} por {damage} de daño. HP restante: {wild_pokemon['hp']}")
        elif action == "2":
            print("Has huido de la batalla.")
            return
        else:
            print("Opción no válida.")
            continue
        
        # Turno del Pokémon salvaje
        if wild_pokemon['hp'] > 0:
            damage = random.randint(3, wild_pokemon['attack'])
            player['hp'] -= damage
            print(f"{wild_pokemon['name']} ataca! HP restante: {player['hp']}")

    if player['hp'] <= 0:
        print("¡Tu Pokémon ha caído en batalla!")
    else:
        print(f"¡Has derrotado a {wild_pokemon['name']}!")