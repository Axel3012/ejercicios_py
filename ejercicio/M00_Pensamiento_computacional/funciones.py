def entradaValida(plantilla,opciones):
    tipo = ''
    while tipo == '':       
        tipo = str(input(plantilla))
        tipo = tipo.upper()
        if tipo in opciones:
            return tipo
        else:
            print('Opcion incorrecta.')
            tipo = ''
            
def datoValidof(plantilla):   
    try:
        dato = float(input(plantilla))
        if dato < 0:
            quit()
    except ValueError:
        quit()
    return dato

def datoValido(plantilla):   
    try:
        dato = int(input(plantilla))
        if dato < 0:
            quit()
    except ValueError:
        quit()
    return dato

def datoValidoRep(plantilla):
    dato = ''   
    while dato == '':
        try:
            dato = float(input(plantilla))              
        except ValueError:
            dato = ''
    return dato

def datoValidoEspacio(plantilla):
    dato = 'a'   
    while dato == 'a':
        try:
            dato = input(plantilla)
            if dato == '':
                return dato  
            dato = float(dato)        
        except ValueError:
            dato = 'a'
    return dato

def reemplazarIterando(i,code,step):
    lcode = list(code)
    lcode[i] = step
    code = "".join(lcode)
    return code

