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
            if dato > 12 or dato < 1:
                print('Dato invalido!!')   
                dato = ''       
        except ValueError:
            dato = ''
    return dato

idiomaMes = {'ESPAÑOL':{1:'ENERO',2:'FEBRERO',3:'MARZO',4:'ABRIL',5:'MAYO',6:'JUNIO',
            7 :'JULIO',8:'AGOSTO', 9:'SEPTIEMBRE', 10:'OCTUBRE', 11:'NOVIEMBRE',12:'DICIEMBRE',
            'frase1':'Ingresa el numero del mes: ','frase2':'El mes {} es {}'},

            'ENGLISH':{1:'JANUARY',2:'FEBRUARY',3:'MARCH',4:'APRIL',5:'MAY',6:'JUNE',
            7 :'JULY',8:'AUGUST', 9:'SEPTEMBER', 10:'OCTOBER', 11:'NOVEMBER',12:'DECEMBER',
            'frase1':'enter the number of the month: ','frase2':'The month {} is {}'},
            

            'FRANCAIS':{1:'JANVIER',2:'FÉVRIER',3:'MARS',4:'AVRIL',5:'MAI',6:'JUIN',
            7 :'JUILLET',8:'AOÛT', 9:'SEPTEMBRE', 10:'OCTOBRE', 11:'NOVEMBRE',12:'DÉCEMBRE',
            'frase1':'Entrez le numéro du mois: ','frase2':'Le mois {} est {}'}
            }

opcinesIdioma = ['ESPAÑOL','ENGLISH','FRANCAIS']
idioma = entradaValida('Idioma, Language, Language: ',opcinesIdioma)

mes = datoValidoRep(idiomaMes[idioma]['frase1'])

strMes = idiomaMes[idioma][mes]
print (idiomaMes[idioma]['frase2'].format(mes,strMes))







