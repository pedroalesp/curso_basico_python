edad_usuario = int(input("¿Cuántos años tienes?: "))

if edad_usuario > 17:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad mi loco")

#----------------------------------------------------

numero = 5
numero_usuario = int(input("Marca el 5 -> "))
if numero_usuario == numero:
    print("Muy bien :D")
elif numero_usuario < numero:
    print("Mi loco el número ingresado es menor a 5")
else:
    print("¿Pero tas loco? Metiste un número mayor a 5 >:v") 
