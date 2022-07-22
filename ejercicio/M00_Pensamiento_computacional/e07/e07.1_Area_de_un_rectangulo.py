def datoValido():
    try:
        dato = float(input())
    except ValueError:
        quit()
    return dato

print('Programa para calcular el area de un rectangulo en metros y yardas', '\n')
print('Longitud en mts:')
l = datoValido()
print('Profundidad en mts:')
w = datoValido()
c = .9144

area = l * w
areay = ((l/c)*(w/c))

print('Area = {} mts^2'.format(area))
print('Area = {} yds^2'.format(areay))




