# Queremos un progama que imprima las potencias de 2 hasta llegar a mil, so:
# 1. definimos el limite
# 2. un contador que incia en 0 y va aumentando
# 3. una variable que tendrá el resultado de la potencia
# 4. creamos el ciclo, mientras la potencia de 2 sea menor a 1000:
#     imprime el resultado, suma 1 al contador y realiza de nuevo la operacion

def run():
    LIMITE = 1000
    contador = 0
    potencia_2 = 2**contador

    while potencia_2 < LIMITE:
        print("2 elevado a " + str(contador) + " es igual a " + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador


if __name__ == "__main__":
    run()