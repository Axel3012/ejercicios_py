def datoValido(plantilla):   
    try:
        dato = int(input(plantilla))
        if dato < 0:
            quit()
    except ValueError:
        quit()
    return dato

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
        if tipo in opciones:
            return tipo
        else:
            print('Opcion incorrecta, elija entre {}'.format(opciones))
            tipo = ''

def interesSimple():
    A = round(datoValidof('Rendimiento a conseguir: €'),2)
    t = datoValidof('Tiempo de inversion (años): ')
    r = datoValidof('Tasa de interes: ')
    tasa = r / 100

    p = A / (1 + tasa*t)

    print('Para alcanzar un rendimiento de €{:.2f} con una tasa del {:.2f}% en {:.0f} años, se deben invertir €{:.2f}'.format(A, r, t, p))

def interesCompuesto():
    A = round(datoValidof('Rendimiento a conceguir: €'))
    r = datoValidof('Interes anual: ')
    t = datoValidof('Años de inversion: ')
    n = datoValido('periodos de imposicion anual: ')
    tasa = r/100

    p = A / (1 + (tasa/n))**(n*t)

    print('Para alcanzar un rendimiento de €{:.2f} con una tasa del {:.2f}% en {} años con  {} periodos de imposicion por año, se deben invertir €{:.2f}'.format(A,r,t,n,p))

print('\n')

opciones = 's','c'
tipo = entradaValida(('Tipo de interes compuesto o simple? (c/s).'),opciones)


if tipo == 's':
    interesSimple()
else: 
    interesCompuesto()
