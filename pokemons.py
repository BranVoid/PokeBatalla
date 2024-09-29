import pokebase as pb
import random

# Diccionario de líderes de gimnasio y sus Pokémon
leaders = {
    'Brock': 'geodude',  # Por ejemplo, Brock usa Geodude
    'Misty': 'starmie',
}

def get_pokemon(name):
    try:
        pokemon = pb.pokemon(name)
        moves = get_random_moves(pokemon)
        return {
            'name': pokemon.name,
            'hp': pokemon.stats[0].base_stat,
            'attack': pokemon.stats[1].base_stat,
            'level': 1,
            'moves': moves,
            'type': pokemon.types[0].type.name,
        }
    except AttributeError:
        print(f"Error al obtener el Pokémon '{name}'. Verifica el nombre.")
        return None

def get_random_moves(pokemon):
    all_moves = pokemon.moves
    selected_moves = random.sample(all_moves, 4)  # Elegir 4 movimientos aleatorios
    return [{'name': move.move.name, 'power': random.randint(5, 15), 'type': move.move.type.name} for move in selected_moves]

def get_wild_pokemon():
    wild_pokemon_names = ['pidgey', 'rattata', 'zubat', 'geodude', 'bulbasaur', 'charmander', 'squirtle']  # Más Pokémon
    name = random.choice(wild_pokemon_names)
    return get_pokemon(name)

def get_leader_pokemon():
    # Escoge un líder al azar
    leader_name = random.choice(list(leaders.keys()))
    return get_pokemon(leaders[leader_name])
