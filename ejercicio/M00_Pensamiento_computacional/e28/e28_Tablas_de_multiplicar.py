def datoValidoRep(plantilla):
    dato = ''   
    while dato == '' or dato < 0 :
        try:
            dato = int(input(plantilla))              
        except ValueError:
            dato = ''
    return dato


n = datoValidoRep("¿Que tabla de multiplicar desea consultar?: ")
print("La tabla del {} es: ".format(n))
for m in range (1, 11):
    print ("{:>2} x {} = {:>2}".format(m, n, m*n))
    