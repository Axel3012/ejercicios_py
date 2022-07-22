def datoValidoRep(plantilla):
    dato = ''   
    while dato == '':
        try:
            dato = int(input(plantilla))              
        except ValueError:
            dato = ''
    return dato

mes = datoValidoRep('Ingresa el numero de mes: ')

if mes == 1:
    strmes = 'Enero'
elif mes == 2:
    strmes = 'Febrero'
elif mes == 3:
    strmes = 'Marzo'
elif mes == 4:
    strmes = 'Abril'
elif mes == 5:
    strmes = 'Mayo'
elif mes == 6:
    strmes = 'Junio'
elif mes == 7:
    strmes = 'Julio'
elif mes == 8:
    strmes = 'Agosto'
elif mes == 9:
    strmes = 'Septiembre'
elif mes == 10:
    strmes = 'Octubre'
elif mes == 11:
    strmes = 'Noviembre'
elif mes == 12:
    strmes = 'Diciembre'
    
print(' El mes {} es {}'.format(mes,strmes))

