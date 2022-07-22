def datoValidof(plantilla):   
    try:
        dato = float(input(plantilla))
        if dato < 0:
            quit()
    except ValueError:
        quit()
    return dato

print('Programa para calcular el IMC(indice de masa corporal)')

peso = datoValidof('Peso(Kg): ')
altura = datoValidof('Altura(Mts): ')
imc = peso / altura**2

if imc < 15:
    diagnostico = 'peso esta por debajo de la normalidad'

if imc > 15 and imc < 18.5:
    diagnostico = 'peso es normal'
if imc > 18.5:
    diagnostico = 'peso esta por encima de la normalidad'

print('Tu IMC es de {:.2f}, tu {}'.format(imc, diagnostico))
