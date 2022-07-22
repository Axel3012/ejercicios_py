from funciones import datoValidoEnter  #Funcion que valida que los datos sean de tipo flotante pero permite que el dato sea una cadena vacia

numeros = []                            #Lista de numeros ingresados

print('Ingresa los numeros que deseas evaluar y preciona doble Enter para conocer el numero mayor.')

numero = float(0)                       #Inicializa la lista con un flotante 0 
numeros.append(numero)                  #Se agrega el cero a la lista, para en caso de no ingresar datos y presionar Enter se muestre el 0 como el numero mayor              
while type(numero) == float:            #Mientras el tipo de la variable numero sea flotante  se entrara en un bucle hasta que se ingrese una cadena vacia(Enter)
    numero = datoValidoEnter('Ingresa numero: ')        #Solicita un numero de tipo flotante o un Enter 
    while numero in numeros:                            #Verifica quqe no se registren datos repetidos
        numero = datoValidoEnter('Ingresa un numero no registrado: ')   #En caso de registrar un dato repetido este no se agregara a la lista y se solicitara uno nuevo
    if numero == '':                    #Si se registra un Enter dejara de pedir datos
        del numeros[0]                  #Eliminara el 0 por default del programa
        mayor = max(numeros)            #Ejecura una funcion que devuelve el numero mas grande de la lista
        print('El numero mayor es el {}'.format(mayor)) 
    numeros.append(numero)              #En caso de registrar un dato de tipo flotante  el bucle continuara
    


