def datoValidof(plantilla):   
    try:
        dato = float(input(plantilla))
        if dato < 0:
            quit()
    except ValueError:
        quit()
    return dato

n1 = datoValidof('Primer numero: ')
n2 = datoValidof('Segundo numero: ')

while n2 == n1:
    n2 = datoValidof('Introdusca un numero no repetido: ')

n3 = datoValidof('Tercer numero: ')
while n3 == n1 or n3 == n2:
    n3 = datoValidof('Introdusca un numero no reperido: ')

if n1 > n2 and n1 > n3:
    mayor = n1
elif n2 > n3:
    mayor = n2
else:
    mayor = n3

print ('El numero mayor es {}'.format(mayor)) 



