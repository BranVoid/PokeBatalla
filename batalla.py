import random
from pokemons import get_wild_pokemon, get_leader_pokemon

# Diccionario de efectividades (para cada tipo)
efectividad = {
    'agua': {'fuego': 2, 'planta': 0.5, 'agua': 1},
    'fuego': {'planta': 2, 'agua': 0.5, 'fuego': 1},
    'planta': {'agua': 2, 'fuego': 0.5, 'planta': 1},
}

def iniciar_batalla(player):
    wild_pokemon = get_wild_pokemon()
    print(f"¡Te encontraste con un {wild_pokemon['name']}! (HP: {wild_pokemon['hp']})")
    
    while player['hp'] > 0 and wild_pokemon['hp'] > 0:
        print("\nTus movimientos:")
        for i, move in enumerate(player['moves']):
            print(f"{i + 1}: {move['name']} (Potencia: {move['power']}, Tipo: {move['type']})")

        action = input("Elige tu acción: (1-4 para atacar, 5 para huir): ")
        if action in ['1', '2', '3', '4']:
            move = player['moves'][int(action) - 1]
            damage = calcular_dano(move, player, wild_pokemon)
            wild_pokemon['hp'] -= damage
            print(f"Atacas a {wild_pokemon['name']} por {damage} de daño. HP restante: {wild_pokemon['hp']}")
        elif action == "5":
            print("Has huido de la batalla.")
            return
        else:
            print("Opción no válida.")
            continue
        
        if wild_pokemon['hp'] > 0:
            damage = random.randint(3, wild_pokemon['attack'])
            player['hp'] -= damage
            print(f"{wild_pokemon['name']} ataca! HP restante: {player['hp']}")

    if player['hp'] <= 0:
        print("¡Tu Pokémon ha caído en batalla!")
    else:
        print(f"¡Has derrotado a {wild_pokemon['name']}!")

def calcular_dano(move, attacker, defender):
    base_damage = move['power']
    effectiveness = efectividad.get(move['type'], {}).get(defender['type'], 1)
    total_damage = base_damage * effectiveness
    return total_damage

def batalla_con_lider(player):
    leader_pokemon = get_leader_pokemon()
    print(f"¡Te enfrentas al líder de gimnasio! El líder usa: {leader_pokemon['name']} (HP: {leader_pokemon['hp']})")

    while player['hp'] > 0 and leader_pokemon['hp'] > 0:
        print("\nTus movimientos:")
        for i, move in enumerate(player['moves']):
            print(f"{i + 1}: {move['name']} (Potencia: {move['power']}, Tipo: {move['type']})")

        action = input("Elige tu acción: (1-4 para atacar): ")
        if action in ['1', '2', '3', '4']:
            move = player['moves'][int(action) - 1]
            damage = calcular_dano(move, player, leader_pokemon)
            leader_pokemon['hp'] -= damage
            print(f"Atacas a {leader_pokemon['name']} por {damage} de daño. HP restante: {leader_pokemon['hp']}")
        
        if leader_pokemon['hp'] > 0:
            damage = random.randint(3, leader_pokemon['attack'])
            player['hp'] -= damage
            print(f"{leader_pokemon['name']} ataca! HP restante: {player['hp']}")

    if player['hp'] <= 0:
        print("¡Tu Pokémon ha caído en batalla!")
    else:
        print(f"¡Has derrotado al líder de gimnasio usando a {player['name']}!")

