from cmath import pi
import math


def datoValido():   
    try:
        dato = float(input())
        if dato < 0:
            quit()
    except ValueError:
        quit()
    return dato

def areaRectangulo():
    print('Entrada de datos en mts', '\n')
    print('Longitud del techo:')
    l = datoValido()
    print('Profundidad del techo:')
    w = datoValido()

    area = l * w

    return area

def areaCirculo():
    print('Entrada de datos en mts', '\n')
    print('Radio del techo:')
    r = datoValido()
    pi = math.pi

    area = pi*r*r

    return area

def areaL():
    print('Entrada de datos en mts', '\n')
    print('anchura seccion horizontal:')
    wh = datoValido()
    print('anchura seccion vertical:')
    wv = datoValido()
    wr = wh - wv
    print('profundidad seccion vertical:')
    pv = datoValido()
    print('profundidad seccion horizontal:')
    ph = datoValido()
    areasv = pv * wv
    arear = wr * ph
    area = areasv + arear
    return area
       
print('PROGRAMA PARA CALCULAR EL NUMERO DE BOTES NECESARIOS PARA PINTAR UN TECHO', '\n')

selectForm = str(input('Forma del techo que deseas pintar, rectangular \ circular \ L, (r/c/l): '))

if selectForm  == 'l':
    area = areaL()
elif selectForm == 'c':
    area = areaCirculo()
else: 
    area = areaRectangulo()

bote = 5/100
litros = bote * area
fracciondeBote = litros / 5 
compraBotes = math.ceil(fracciondeBote)

# Solucion del profe para el caso del rectangulo
'''
bote = 5/100
area = l * w
litros = area * bote
botes = litros // 5     # devuelve el valor entero de la division
if litros % 5 > 0:      # evalua si el litros es multiplo de 5
    botes += 1           # ya que de serlo no seria necesario redondear hacia arriba el numero de botes
else: 0                
'''


print('Necesitaras {:.2f} litros para pintar {:.2f} metros^2 de techo'. format(litros,area))
print('Debes comprar {} botes de pintura'.format(compraBotes))










   