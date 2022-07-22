def creaContador(ini = 0): # Creador de la funcion con comportamiento y estado -> Clase
    clicks = ini 

    def click():
        nonlocal clicks
        clicks += 1
        return clicks

    return click


def creaContadorReutilizable( ini = 0):
    '''
    variables de estado -> Atributos
    '''

    clicks = ini

    '''
    reset, consulta, click
    funciones de comportamiento -> Metodos
    '''

    def reset(v):
        if v < 0:
            print('dato invalido')
        else:
            nonlocal clicks
            clicks = v
            return clicks

    def consulta():
        return clicks
    
    def click():
        nonlocal clicks
        clicks += 1
        return clicks
    '''
    Parte qeu crea lo necesario para que el contador funcione (infraestructura minima) -> costructor
    incluye el return
    '''
    def contador(**kwargs):
        nonlocal clicks

        if len(kwargs) == 0:
            return click()

        if 'consulta' in kwargs:
            return consulta()

        if 'reset' in kwargs:
            valor_inicial = kwargs['reset']
            return reset(valor_inicial)
        
        #raise Exception('Fincion desconocida')

    return contador

class Contador():
    def __init__(self, ini = 0):
        self.clicks = ini

    def click(self):
        self.clicks += 1
        return self.clicks

    def consulta(self):
        return self.clicks

    def reset(self, v):
        self.clicks = v
        return self.clicks

