def run():
    # mi_diccionario = {
    #     'llave1': 1, #valor 1
    #     'llave2': 2, #valor 2
    #     'llave3': 3 #valor 3
    # }
    # print(mi_diccionario)
    # print(mi_diccionario['llave1'])

    pokemon_tipos = {
        'pikachu': 'electrico',
        'charmander': 'fuego',
        'squirturttle': 'agua'
    }
    # for pokemon in pokemon_tipos.keys():
    #     print(pokemon)
    # for pokemon in pokemon_tipos.values():
    #     print(pokemon)

    for pokemon, tipo in pokemon_tipos.items():
        print(pokemon + ' es tipo ' + tipo)


if __name__ == '__main__':
    run()