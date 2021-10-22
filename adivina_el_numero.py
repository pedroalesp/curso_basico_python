import random


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input(">>Ingresa un número del 1 al 100: "))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Nope❌ Intenta con un número mayor")
        else:
              print("Nope❌ Intenta con un número menor")
        numero_elegido = int(input(">>Ingresa un número: "))
    print(">>Encontraste el número 🤘😎")
if __name__ == "__main__":
    run()