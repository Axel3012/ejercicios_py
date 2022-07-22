def datoValidof(plantilla):   
    try:
        dato = float(input(plantilla))
        if dato < 0:
            quit()
    except ValueError:
        quit()
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

def sistemaInternacional():                 #Calculadora de IMC con datos de entrada del sistema Internacional
    peso = datoValidof('Peso(Kg): ')
    altura = datoValidof('Altura(Mts): ')
    imc = peso / altura**2
    return imc

def sistemaAnglosajon():                    #Calculadora de IMC con datos de entrada del sistema Anglosajon
    peso = datoValidof('Peso(lb): ')
    altura = datoValidof('Altura(ft): ')
    altura = altura*12
    imc = (peso / altura**2)*703
    return imc

    

opciones = '1','2'   #Opciones validas de seleccion para el sistema de entrada que se desee
clasificaciones = [                                                          #Lista bidimensional con datos que indican [imc, 'clasificacion']
                    [16, 'Delgadez severa'],[17,'Delgadez moderada'],
                    [18.5,'Delgadez leve'],[25.01,'Normal'],[30,'Preobeso'],
                    [35,'Obesidad leve'],[39.99,'Obesidad media'],
                    [float('inf'),'Obesidad morbida']
                    ]
                  
print('Programa para calcular el IMC(indice de masa corporal)')

sistema = entradaValida('Datos a ingresar en Sistema internacional(1) o Sistema anglosajon(2): ',opciones) #Solicita un dato valido para poder seleccionar una funcion
if sistema == '1':
    imc = sistemaInternacional() #Registra el valor del IMC con datos de entrada del sistema internacional
if sistema == '2':
    imc = sistemaAnglosajon()    #Registra el valor del IMC con datos de entrada del sistema anglosajon

for rango, clasificacion in clasificaciones:    #Recorre la lista bidimencional llamada clacificaciones
    if imc < rango:                             #Evalua si el dato del IMC es menor que el dato del rango en una pareja de la lista bidimensional, en caso de no serlo evalua el siguiente par de la lista                                               
        break                                   #Cuando se cumpla la condicion se saldra del bucle y se imprimira el dato del IMC y la clacificacion del par que cumpliese la condicion    
print('Tu IMC es de {:.2f}, clasificado como {}'.format(imc,clasificacion))







