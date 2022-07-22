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

def datoValidoRep(plantilla):
    dato = ''   
    while dato == '':
        try:
            dato = int(input(plantilla))              
        except ValueError:
            dato = ''
    return dato

idiomaMes = {'ESPAÑOL':{1:'ENERO',2:'FEBRERO',3:'MARZO',4:'ABRIL',5:'MAYO',6:'JUNIO',
            7 :'JULIO',8:'AGOSTO', 9:'SEPTIEMBRE', 10:'OCTUBRE', 11:'NOVIEMBRE',12:'DICIEMBRE'},
            'INGLES':{1:'JANUARY',2:'FEBRUARY',3:'MARCH',4:'APRIL',5:'MAY',6:'JUNE',
            7 :'JULY',8:'AUGUST', 9:'SEPTEMBER', 10:'OCTOBER', 11:'NOVEMBER',12:'DECEMBER'},
            'FRANCES':{1:'JANVIER',2:'FÉVRIER',3:'MARS',4:'AVRIL',5:'MAI',6:'JUIN',
            7 :'JUILLET',8:'AOÛT', 9:'SEPTEMBRE', 10:'OCTOBRE', 11:'NOVEMBRE',12:'DÉCEMBRE'}
            }

opcinesIdioma = ['ESPAÑOL','INGLES','FRANCES']
idioma = entradaValida('Idioma, Language, Langage: ',opcinesIdioma)

if idioma == 'ESPAÑOL':
    mes = datoValidoRep('Ingresa el numero del mes: ')
    strMes = idiomaMes[idioma][mes]
    print ('El mes {} es {}'.format(mes,strMes))

if idioma == 'INGLES':
    mes = datoValidoRep('enter the number of the month: ')
    strMes = idiomaMes[idioma][mes]
    print ('The month {} is {}'.format(mes,strMes))
    
if idioma == 'FRANCES':
    mes = datoValidoRep('Entrez le numéro du mois: ')
    strMes = idiomaMes[idioma][mes]
    print ('Le mois {} est {}'.format(mes,strMes))




