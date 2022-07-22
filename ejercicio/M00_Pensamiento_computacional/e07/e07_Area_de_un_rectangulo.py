print('Programa para calcular el area de un rectangulo en metros y yardas', '\n')
l = float(input('largo: '))
w = float(input('Acho: '))
c = .9144

area = l * w
areay = ((l/c)*(w/c))

print('Area = {} mts^2'.format(area))
print('Area = {} yds^2'.format(areay))




