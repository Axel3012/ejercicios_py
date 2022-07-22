def datoValido():
    try:
        dato = float(input())
    except ValueError:
        quit()
    return dato

def entradaEnMetros():
    print('Entrada de datos en mts', '\n')
    print('Longitud en mts:')
    l = datoValido()
    print('Profundidad en mts:')
    w = datoValido()
    c = .9144

    area = l * w
    areay = ((l/c)*(w/c))

    print('Area = {} mts^2'.format(area))
    print('Area = {} yds^2'.format(areay))

def entradaEnYardas():    
    print('Entrada de datos en yds', '\n')
    print('Longitud en yds:')
    l = datoValido()
    print('Profundidad en yds:')
    w = datoValido()
    c = .9144

    area = ((l*c) * (w*c))
    areay = l * w

    print('Area = {} yds^2'.format(areay))
    print('Area = {} mts^2'.format(area))

print('Programa para calcular el area de un rectangulo en metros y yardas', '\n')
seting = str(input('Calculo en metros o yardas(m/y)?: '))
if seting == 'm':
    entradaEnMetros()
else:
    entradaEnYardas()


