# PokeBatalla
Un proyecto con python que busca hacer algo similar a pokemon.
# Práctica 4: Revisión de Código y Refactorización

## **Objetivo**
El propósito de esta práctica es identificar y corregir bugs, code smells y vulnerabilidades en un proyecto de software personal utilizando herramientas de análisis estático de código, como SonarLint. La intención es aplicar buenas prácticas de codificación para mejorar la calidad y la legibilidad del código, así como su seguridad y mantenimiento.

## **Prerrequisitos**
- Proyecto de software personal en cualquier lenguaje de programación popular (por ejemplo, Python, Java, C#, PHP).
- IDE configurado con la extensión/plugin SonarLint.

## **Actividades**
1. **Análisis de Código con SonarLint:** 
   - Realizar un análisis inicial con la extensión de SonarLint para identificar bugs, code smells y vulnerabilidades en el proyecto.
2. **Implementar Correcciones y Refactorizaciones:** 
   - Corregir y refactorizar el código detectado con violaciones, aplicando principios de Clean Code y buenas prácticas de codificación.
3. **Documentación de Resultados:** 
   - Describir al menos 3 correcciones o refactorizaciones implementadas, explicando cada violación identificada, su corrección y el fragmento de código antes y después de la refactorización.

## **Correcciones Implementadas**

### **Violación 1: Uso inadecuado de `except:` en `get_pokemon`**
- **Descripción:** El bloque `except:` captura todas las excepciones sin especificar el tipo de error, lo que es una mala práctica de manejo de errores. Esto puede dificultar la depuración y hacer que errores críticos sean ignorados.
- **Corrección/Refactorización:** Especificar el tipo de excepción que se quiere capturar. En este caso, se utiliza `except AttributeError` para capturar errores específicos cuando los atributos del Pokémon no se encuentran.
  
**Fragmento de Código Antes de la Corrección:**
```python
def get_pokemon(pokedex, name):
    try:
        return pokedex[name]
    except:
        return None
```
**Fragmento de Código Después de la Corrección:**
```python
def get_pokemon(pokedex, name):
    try:
        return pokedex[name]
    except AttributeError:
        return None
```
### **Violación 2: Eliminación de Parámetros Innecesarios en `calcular_dano`**
- **Descripción:** El parámetro `attacker` en la función `calcular_dano` no se utiliza dentro de la lógica de la función, lo que indica un caso de parámetros redundantes. Mantenerlo en la firma de la función puede confundir a otros desarrolladores y aumentar la complejidad innecesaria.
- **Corrección/Refactorización:**  Eliminar el parámetro `attacker` de la firma de la función y de todos los lugares donde se llama a la función para simplificarla.

**Fragmento de Código Antes de la Corrección:**
```python
def calcular_dano(move, attacker, defender):
    base_damage = move['power']
    effectiveness = efectividad.get(move['type'], {}).get(defender['type'], 1)
    total_damage = base_damage * effectiveness
    return total_damage
```
**Fragmento de Código Después de la Corrección:**
```python
def calcular_dano(move, defender):
    base_damage = move['power']
    effectiveness = efectividad.get(move['type'], {}).get(defender['type'], 1)
    total_damage = base_damage * effectiveness
    return total_damage
```

### **Violación 3: Código Muerto en en `evolver_pokemon`**
- **Descripción:** La condición `else` es redundante en la función `evolver_pokemon`, ya que la función siempre devuelve el Pokémon si no se cumple ninguna condición anterior. Esto crea una estructura condicional innecesaria que aumenta la complejidad.
- **Corrección/Refactorización:**  Simplificar el bloque `if` eliminando la estructura `else`, devolviendo el Pokémon de manera directa cuando no se cumple la condición inicial.

**Fragmento de Código Antes de la Corrección:**
```python
def evolver_pokemon(pokemon):
    if pokemon['name'] == 'charmander':  
        return get_pokemon('charmeleon') 
    elif pokemon['name'] == 'squirtle':  
        return get_pokemon('wartortle') 
    elif pokemon['name'] == 'bulbasaur': 
        return get_pokemon('ivysaur')  
    else:
        return pokemon 
```
**Fragmento de Código Después de la Corrección:**
```python
def evolver_pokemon(pokemon):
    if pokemon['name'] == 'charmander':
        return get_pokemon('charmeleon')
    if pokemon['name'] == 'squirtle':
        return get_pokemon('wartortle')
    if pokemon['name'] == 'bulbasaur':
        return get_pokemon('ivysaur')
    return pokemon  # Sin evolución
```

### **Violación 4: Simplificación de Condicionales Anidadas en `main`**
- **Descripción:**  En la función `main`, se utilizan condicionales `if-elif` anidadas para validar las opciones del usuario al interactuar con el juego, lo cual reduce la legibilidad y claridad del código.
- **Corrección/Refactorización:**  Reemplazar las condicionales `if-elif` con un manejo mediante diccionario que mapea las opciones del usuario a sus respectivas funciones. De esta manera, se mejora la legibilidad y se facilita la extensión del código.

**Fragmento de Código Antes de la Corrección:**
```python
def main():
    print("Bienvenido al juego de Pokémon!")
    nombre_pokemon = input("Elige tu Pokémon (Charmander, Squirtle, Bulbasaur): ").strip().lower()
    player_pokemon = get_pokemon(nombre_pokemon)

    if not player_pokemon:  # 1 bifurcación
        print("Pokémon no válido. El juego se cerrará.")
        return  # 1 retorno (flujo adicional)

    print(f"Has elegido: {player_pokemon['name']} (HP: {player_pokemon['hp']})")
    
    while True:  # 1 bucle
        print("\n¿Quieres buscar un Pokémon salvaje? (si/no)")
        opcion = input().strip().lower()
        if opcion == "si":  # 2ª bifurcación
            iniciar_batalla(player_pokemon)
            if player_pokemon['level'] >= 16:  # 3ª bifurcación (anidada)
                print(f"¡{player_pokemon['name']} ha alcanzado el nivel de evolución!")
                evolver = input("¿Quieres evolucionar? (si/no): ").strip().lower()
                if evolver == "si":  # 4ª bifurcación (anidada)
                    player_pokemon = evolver_pokemon(player_pokemon)
                    print(f"{player_pokemon['name']} ha evolucionado!")
                batalla_con_lider(player_pokemon)
        elif opcion == "no":  # 5ª bifurcación
            print("Gracias por jugar!")
            break  # 1 interrupción del flujo
        else:  # 6ª bifurcación
            print("Opción no válida.")
```
**Fragmento de Código Después de la Corrección:**
```python
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
```

## **Conclusiones**
La refactorización y corrección de los bugs, code smells y vulnerabilidades identificados mejoró la calidad del proyecto. Al aplicar las prácticas de Clean Code, el código resultante es más fácil de leer, mantener y menos propenso a errores.
