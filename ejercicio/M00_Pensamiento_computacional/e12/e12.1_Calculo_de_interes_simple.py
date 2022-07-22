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

def crecimiento():
    i = 0
    for i in range(años+1):
        A = inversion * (1 + tasa*i)
        if i > 0:
            print('Valor de la inversion en el año {} es de €{:.2f}'.format(i,A))   
         
inversion = round(datoValidof('Cantidad a invertir: €'),2)
años = datoValido('Tiempo de inversion (años): ')
porcentaje = datoValidof('Tasa de interes: ')
tasa = porcentaje / 100

crecimiento()

