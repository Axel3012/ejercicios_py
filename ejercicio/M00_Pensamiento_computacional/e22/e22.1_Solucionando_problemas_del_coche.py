def entradaValida(plantilla,opciones):
    tipo = ''
    while tipo == '':       
        tipo = str(input(plantilla))
        tipo = tipo.lower()
        if tipo in opciones:
            return tipo
        else:
            print('Opcion incorrecta. puede elejir: {}'.format(opciones))
            tipo = ''

def reemplazar(i,code,step): 
    lcode = list(code)
    lcode[i] = step
    code = "".join(lcode)
    return code

opciones = ['s','n']            #Opciones validas para la funcion EntradaValida                

arbol = {'preguntas':           #Diccionario que contiene las preguntas y soluciones con su clave
        {
                    '00000':'Arranca?(s/n): ',
                    's0000':'Suena un click?(s/n): ',
                    'n0000':'Estan los bornes de la bateria coroidos?(s/n): ',
                    'sn000':'Se enciende el coche pero no arranca?(s/n): ',
                    'snn00':'Arranca el coche y luego se cala?(s/n): ',
                    'snns0':'Tiene el coche inyeccion de combustibe?(s/n): '
        },
        'soluciones':
        {
                    'ss000':'Reemplaza la bateria',
                    'sns00':'Revisa las bujias',
                    'snnn0':'Lleve su coche al taller',
                    'snnss':'Lleve el coche al taller',
                    'snnsn':'Abre y cierra el starter',
                    'ns000':'Limpia los bornes y arranca de nuevo',
                    'nn000':'Reemplaza los cables y arranca de nuevo'
        }
        }

code = '00000'          #Inicializa variable de tipo cadena con ela clave del nodo root del arbol('00000')
step = ''               #Inicializa la variable step
i = 0                   #Inicializa la variable iteradora
for i in range(5):          #Itera el numero de nodos que hay en nuestro arbol (6)
    step = entradaValida(arbol['preguntas'][code],opciones)         #Llama de la direccion del diccionario la cadena que contiene la pregunta a evaluar // Guarda la respuesta para poderla reemplazar en la clave anterior
    code = reemplazar(i,code,step)          #Llama a una funcion encargada de cambiar el valor de la clave con el dato de str
    if code in arbol['soluciones']:         #Evalua si la clave esta dentro de la direccion del diccionario solicitada
        break                               #En caso de ser asi saldra de la iteracion
solucion = arbol['soluciones'][code]        #Guardara el valor de la clave solicitada
print('Sugerencia de solucion: {}'.format(solucion))
    

