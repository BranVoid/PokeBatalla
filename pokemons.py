import pokebase as pb
import random

def get_pokemon(name):
    try:
        pokemon = pb.pokemon(name)
        return {
            'name': pokemon.name,
            'hp': pokemon.stats[0].base_stat,
            'attack': pokemon.stats[1].base_stat
        }
    except:
        return None

def get_wild_pokemon():
    wild_pokemon_names = ['pidgey', 'rattata', 'zubat']
    name = random.choice(wild_pokemon_names)
    return get_pokemon(name)
