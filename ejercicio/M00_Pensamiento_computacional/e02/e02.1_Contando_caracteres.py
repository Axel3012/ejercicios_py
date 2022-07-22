caracteres = input('Ingresa caracteres: ')

while len(caracteres) == 0:
    caracteres = input('Ingresa caracteres: ')
    
print(caracteres)
print('El numero de caracteres es: ', len(caracteres))


#Solucion de profesor

str = input('Escribe algo: ')

print("La cadena'", str, "'tiene", len(str), 'caracteres')
print("La cadena '{}' tiene {} caracteres".format(str, len(str)))