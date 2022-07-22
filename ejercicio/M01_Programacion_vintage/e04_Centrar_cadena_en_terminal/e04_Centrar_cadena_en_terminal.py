from Centrar import *

#Ingresa una cadena y te la imprime centrada
str1 = input('Ingresa cadena: ')
textoCentrado = centrar(str1)
print(textoCentrado)

#imprime 'hola' centrada a el valor ingresado
textoCentrado = centrar2('hola',145)
print(textoCentrado)

#Dato invalido
textoCentrado = centrar2(34,135)
print(textoCentrado)

#Dato invalido
textoCentrado = centrar2('holar','pez')
print(textoCentrado)

#Dato invalido
textoCentrado = centrar2(123,'pez')
print(textoCentrado)

