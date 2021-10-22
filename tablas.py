def tablas(numero):
    for contador in range(1, 11):
        print( str(numero) + " x " + str(contador) + " = " + str(numero * contador))


def run():
    numero = int(input("""
    ______________________________________________________________

    >> 💻Este es un programa que te dirá las tablas de multipicar 
    de cualquier número🔢

    >> 👉Ingresa un número: """))
    tablas(numero)


if __name__ == "__main__":
    run()