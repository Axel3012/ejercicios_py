def datoValido(plantilla):   
    try:
        dato = int(input(plantilla))
        if dato < 0:
            quit()
    except ValueError:
        quit()
    return dato

def datoValidof(plantilla):   
    try:
        dato = float(input(plantilla))
        if dato < 0:
            quit()
    except ValueError:
        quit()
    return dato

inversion = round(datoValidof('Cantidad a invertir: €'),2)
años = datoValidof('Tiempo de inversion (años): ')
porcentaje = datoValidof('Tasa de interes: ')
tasa = porcentaje / 100

A = inversion * (1 + tasa*años)


print('tras {} años de inversion al {:.1f} %, su cantidad debe ser de €{:.2f}.'.format(años, porcentaje, A))