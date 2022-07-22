def datoValidoCero(plantilla):
    dato = ''   
    while dato == '':
        try:
            dato = input(plantilla)
            if dato == '0':
                return dato  
            dato = float(dato)        
        except ValueError:
            print('Dato invalido, intente de nuevo')
            dato = ''
    return dato

def calculoMedia(numero):
    while type(numero) == float:            #Mientras siga recibiendo datos de tipo flotante continuara registrando numeros y añadiendolos a la lista
        numero = datoValidoCero('Ingresa numero: ')         #Asigna un dato de tipo flotante a la variable numero
        if numero == '0':                                   #Evalua si la variable numero contien un '0'
            cuantos = len(numeros)                          #De ser asi asignara el numero de elementos dentro de la lista a la variable cuantos
            if cuantos < 1:                                #Evalua si el numero de datos es 1, lo que significaria que no se introdujeron datos
                raise ValueError('No se introdujeron datos.')   #De ser asi arrojara un error 
            suma = sum(numeros)                             #En caso de haber registrado mas de 1 dato sumara todos los datos dentro de la lista y los asignara a la variable suma
            media = suma/cuantos                            #Asignara a la variable media la division entre la suma de la lista y el numero de datos en ella
            return media                                    
        numeros.append(numero)              #añadira el numero registrado en la variable numero a la lista numeros



print('Ingresa los numeros que deseas evaluar y preciona "0" para conocer la media de los numeros ingresados.')

numeros = []            #Lista ue contiene los numero ingresados en la funcion calculoMedia
numero = float(0)       #Inicializa la vairable numero con un flotante 
media = calculoMedia(numero)            #recibe el dato de la funcion calculaMedia // el dato es la media de todos los numero ingresados en la lista numeros

print('La media es: {}'.format(media))          










