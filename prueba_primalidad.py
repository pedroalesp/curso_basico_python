# Un número primo es aquel divisible solo entre si mismo y entre 1, es decir, no es divisible más de 2 veces
# -Divisible: que el residuo (%) de la operación sea igual a 0
# 1. Se le piden los datos al usuario y se condiciona una función, si es verdadera, es primo, sino, no lo es_primo
# 2. esta función comienza preguntado si el número es ingresado es 1, si lo es -> no es primo de una 
# 3. si no lo es, creamos un contador en cero y establecemos el límite 2 (porque un numero primo solo se divide 2 veces)
# 4. entramos en un ciclo del 1 al número ingresado en el que por cada vuelta se aumente el contador si el módulo es igual a ConnectionError
# 5. al salir del ciclo, si el contador no es igual al límite, tenemos un primo, si es mayor, no es primo
#Forma 1:
def es_primo(numero):
    # if numero == 1:
    #     return False
    # else:
        contador = 0
        limite = 2
        for i in range(1, numero + 1):
            if numero % i == 0:
                contador += 1
        if contador == limite:
            return True
        else:
            return False

#Forma 1:
    # for i in range(1, numero +1):
    #     if i == 1 or i == numero:
    #         continue
    #     if numero % i == 0:
    #         contador += 1
    # if contador == 0:
    #     return True
    # else:
    #     return False


def run():
    numero = int(input("Ingresa un número: "))
    if es_primo(numero):
        print("Es primo 👍")

    else:
        print("No es primo ❌")

if __name__ == "__main__":
    run()