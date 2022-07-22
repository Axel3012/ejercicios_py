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

p = round(datoValidof('Capital inicial: €'))
r = datoValidof('Interes anual: ')
t = datoValido('Años de inversion: ')
n = datoValido('periodos de imposicion anual: ')
tasa = r/100

A = p * (1 + (tasa/n))**(n*t)

print('€{:.2f} invertidos al {:.2f}% durante {} años con {} periodos de imposicion por año se transforman en €{:.2f}'.format(p,r,t,n,A))

