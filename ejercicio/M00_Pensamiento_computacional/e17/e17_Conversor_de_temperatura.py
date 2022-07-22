def datoValidof(plantilla):
    dato = ''   
    while dato == '':
        try:
            dato = float(input(plantilla))
            if dato < 0:
                 dato = ''               
        except ValueError:
            dato = ''
    return dato

def entradaValida(plantilla,opciones):
    tipo = ''
    while tipo == '':       
        tipo = str(input(plantilla))
        tipo = tipo.upper()
        if tipo in opciones:
            return tipo
        else:
            print('Opcion incorrecta, elija entre {}'.format(opciones))
            tipo = ''

def conversion(temperatura, grados):
    if grados == 'C':
        tempn = ((temperatura-32))*5/9
        grados1 = 'F'
    if grados == 'F':
        tempn = ((temperatura*(9/5)))+32
        grados1 = 'C'
    print('{}º {} equivalen a {:.3f}º {}'.format(temperatura,nombre[grados1],tempn,nombre[grados]))

print('Programa que convierte tempretura Fahrenheita a Celcius y viceversa')
nombre = {'C':'Celcius', 'F':'Fahrenheit'}
conversion(datoValidof('Temperatura: '),entradaValida('Convertir a grados Celcius o Fahrenheit? (c/f): ',nombre))


    