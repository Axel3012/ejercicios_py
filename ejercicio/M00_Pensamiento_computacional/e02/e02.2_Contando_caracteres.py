caracteres = input('Ingresa caracteres: ')

while len(caracteres) == 0:
    caracteres = input('Ingresa caracteres: ')
    
str = caracteres
puntero = 0

while str != '':
    str = str[1:]
    puntero += 1
    
print('\n')
print('La cadena "{}" tiene {} caracteres'. format(caracteres, puntero))

    
