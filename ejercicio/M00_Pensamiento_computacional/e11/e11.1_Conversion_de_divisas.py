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

def conversor(pais):
    tipodeCambio = (input('Pais de moneda de cambio (EUA / MEXICO / JAPON / {}): '.format(pais)))
    tipodeCambio = tipodeCambio.upper()
    tipodeCambioN = monedas[tipodeCambio]
    cifra = datoValidof('Cantidad: ')

    x = tipodeCambioN * cifra

    print('Serian {} euros.'.format(x))

def addPais():
    
    pais = input('Pais de moneda de cambio: ')
    pais = pais.upper()

    valor = datoValidof('Tasa de cambio a euro: ')

    monedas[pais] = valor
    
    conversor(pais)


monedas = {0.95: 'USA', 0.0073: 'JAPON', 0.047: 'MEXICO' }

choice = str(input('Conversion a euros? o Agregar tipo de cambio? (C/A): '))
choice = choice.upper()

if choice == 'A':
    addPais()
    
else:
    conversor(None)

    

    







