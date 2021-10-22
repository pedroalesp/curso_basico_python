# 💲💰CONVERSOR DE MONEDAS 💲💰

# Vamos a crear un pequeño menú para que nuestros usuario
# elija la moneda que quiere connvertir a dolar

def conversor(moneda_actual, valor_dolar):
    moneda = input("¿Cuántos" + " " +  moneda_actual + " " + "quieres convertir?: ")
    moneda = int(moneda)
    valor_cambio = moneda/valor_dolar
    valor_cambio = str(round(valor_cambio, 2))
    moneda = str(moneda)
    print(moneda + " " + moneda_actual + " Son: " + valor_cambio + "$")

menu = """
💲💰Bienvenido al conversor de monedas💲💰
Aquí podrás convertir monedas de distintos países a dólares americanos.

1 --> CLP
2 --> EUR
3 --> COP

👉 Introduce el número de la moneda que queires convertir: """

opcion = int(input(menu))

if opcion == 1:
    conversor("CLP", 800)

elif opcion == 2:
    conversor("EUR", 0.86)
    
elif opcion == 3:
    conversor("EUR", 3763)
    
else:
    print("Ingresa una opción válida")