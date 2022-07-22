def datoValidoEspacio(plantilla):
    dato = ' '   
    while dato == ' 'or dato < 0:
        try:
            dato = input(plantilla)
            if dato == '0':
                return dato  
            dato = float(dato)        
        except ValueError:
            print('Ingresa un dato valido!')
            dato = ' '
    return dato

bebe = 0
menores = 0
normales = 0
jubilados = 0

tiposBoletos = [ [2,0, bebe,'de bebe'],
                [12,14, menores, 'de menores'],
                [65,23, normales, 'normales'],
                [float('inf'),18, jubilados, 'jubilado']
              ]

edad = datoValidoEspacio('Edad del visitante: ')
while edad != '0':
    for pos in range(len(tiposBoletos)):
        rango = tiposBoletos[pos][0]
        if edad < rango:
            boletos = tiposBoletos[pos][2]
            boletos += 1
            tiposBoletos[pos][2] = boletos
            break
    edad  = datoValidoEspacio('Edad del visitante: ')

total = 0
print('\n')
for rango, precio, boletos, tipo in tiposBoletos:
    if boletos > 0:
        totalXboleto = float(precio * boletos)
        totalXboleto = round(totalXboleto, 2)
        print('{:<3} entradas {:<10} ({:2d}€): |{:>5}€'.format(boletos, tipo, precio, totalXboleto))
        total += totalXboleto
    else:
        None








