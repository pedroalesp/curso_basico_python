# 1. Escribir el entry point de nuestro programa
# 2. definir la función principal que va a correr el programa
# 3. Solicitar datos al usuario
# 4. Crear una función que reciba los datos del usuario y guardarlos en una variable
# 5. Continuar la lógica con condicionales
# 6. Mutar la plabra ingresa por el usuario e invertirla
# 7. Retornar True o False con condicionales para que el Boolean se aguarde en la variable


def palindromo(palabra):
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input("""
    ✍Beinvenido al identificador de palíndromos✍

    👉Ingresa una frase para saber si es un palíndromo: """)
    es_palindromo = palindromo(palabra)

    if es_palindromo == True:
        print("Es palíndromo 🤩")
    else:
        print("No es palíndromo 🤔")


if __name__ == '__main__':
    run()
