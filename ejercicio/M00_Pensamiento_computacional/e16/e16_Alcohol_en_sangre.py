def datoValido(plantilla):   
    try:
        dato = int(input(plantilla))
        if dato < 0:
            quit()
    except ValueError:
        quit()
    return dato

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
        if tipo in opciones:
            return tipo
        else:
            print('Opcion incorrecta, elija entre {}'.format(opciones))
            tipo = ''

def registrarBebida():
    densidad = 0.8                                         #Datos necesarios para el uso de la formula para calcular los gramos absolutos ('A').
    bebidas = datoValidof('Numero de bebidas: ')
    volumen = datoValidof('Volumen de la bebida(mL): ')
    grados = datoValidof('Grado alcoholico de la bebida: ')
    print('\n')

    A = ((bebidas*volumen)*grados*densidad)/100             #Formula para calcular los gramos absolutos.
    An.append(A)                                            #Se agrega el resultado a una lista que se usara en caso de registrar otras bebidas  y poder sumar todos los gramos absolutos.
    otra = entradaValida('Otra Bebida?(s/n): ',opciones)      #Se enviara a una funcion que valida que la entrada de la pregunta sea valida.
    print('\n')
    return otra                                             #Se retornara si se quiere registrar otra bebida.

aiLimite = 0.5                  #Tasa limite de alcoholemia            
An = []                         #Lista de resultados que se usara en caso de registrar otras bebidas  y poder sumar todos los gramos absolutos.
opciones = 's','n'              #Opciones validas para ingresar a la pregunta "Otra Bebida?(s/n)".

otra = registrarBebida()        #Se recupera el dato de si se va a ingresar otra bebida.           

while otra == 's':              #Si la respuesta a "Otra Bebida?(s/n)"  es "s" se registrara otra bebida.
    otra = registrarBebida()    #se volvera a recuperar el dato hasta que el dato sea "n"

if otra == 'n':                 #La respuesta a "Otra Bebida?(s/n)" es "n" no se registrara otra bebida y se procedera a realizar los calculos necesarios
    At = sum(An)                #Se suman todas los gramos absolutos
    ube = At/10
    ai = ube*0.3
    h = datoValidof('Horas transcurridas: ')
    print('\n')
    ar = ai - (0.15*h)
    if ar < 0:
        print('Datos invalidos')
        quit()

    print('Alcohol en la sangre: {:.3f}g/l\n'.format(ar))
    print('El maximo permitido es : {}g/l'.format(aiLimite))

    if ai > aiLimite:
        print('Usted no puede conducir.')
    else:
        print('Usted puede conducir.')



    



