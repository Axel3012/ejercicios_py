def datoValidof(plantilla):
    dato = ''   
    while dato == '':
        try:
            dato = float(input(plantilla))              
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


def conversion(grados, temperatura, ngrados): #resive los la unidad de entrada, la temperatura y la unidad a la que hay que convertir
    cf = ((temperatura*(9/5)))+32              #Convierte celcius a farenhait
    fc = ((temperatura-32))*5/9                 #Convierte farenhait a celcius
    ck = temperatura + 273.15                   #Convierte celcius a kelvin
    kc = temperatura - 273.15                   #Convierte Kelvin a Celcius
    fk = fc + 273.15                            #Convierte Farenhait a Kelvin
    kf = ((9/5)*kc)+32                          #Convierte Kelvin a Farenhait

    formulas = {'C':{'F':cf,'K':ck},'F':{'C':fc,'K':fk},'K':{'C':kc,'F':kf}} #Lista de resultados 

    tempn = formulas[grados][ngrados]                                           #Devuelve el resultado ingresando al diccionario con primer clave como la unidad de entrada y como segunda clave la unidad de salida

    print('\n','{}º {} equivalen a {:.2f}º {}.'.format(temperatura,nombre[grados],tempn,nombre[ngrados])) #Imprime los datos de la temperatura ingresada, la unidad de temperatura de entrada, el valor de la conversion y la unidad de conversion

opciones = 'C','F','K'                               #Opciones validas para elegir las unidades de entrada y de salida

print('Programa conversor de temperatura. Se debe seleccionar la unidad de entrada y la de salida.','\n') #Instrucciones
nombre = {'C':'Celcius', 'F':'Fahrenheit', 'K':'Kelvin'} #Lista de nombres de las unidades de medida para devolver en el mensaje de salida
conversion(entradaValida('Unidades de entrada Celcius, Fahrenheit o Kelvin, (c/f/k): ',opciones),datoValidof('Temperatura: '), entradaValida('Convertir a grados Celcius, Fahrenheit o Kelvin? (c/f/k): ',opciones)) #Envia le dato de la unidad de enttrada, el valor de la unidad de entrada y envia la unidad a la que se debe de convertir


    