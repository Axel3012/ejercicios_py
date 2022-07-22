#Quien eres

nombre = input("¿Como te llamas? ")
print("Hola,", nombre)

#Toma de datos
edad = input("¿Cuantos años tienes? ")
edad = int(edad)
año_actual = input("¿En que año estamos? ")
año_actual = int(año_actual)
has_cumplido = input("Has cumplido años ya? (S/N)? ")

#Calculo del año
if has_cumplido == "S":
    año_nacimiento =año_actual - edad
else:
    año_nacimiento =año_actual - edad
    año_nacimiento = año_nacimiento - 1
     
#Presentacion de resultados
print(nombre, "naciste en", año_nacimiento)
