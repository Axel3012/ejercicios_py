def datoValidoCero(plantilla):
    dato = ''   
    while dato == '' or dato < 0:
        try:
            dato = input(plantilla)
            if dato == '0':
                return dato  
            dato = int(dato)        
        except ValueError:
            dato = ''
    return dato

n = 0
while type(n) == int:
    n = datoValidoCero("¿Que tabla de multiplicar desea consultar?: ")
    if n == '0':
        print('Adios!!')
        break
    print("\nLa tabla del {} es: ".format(n))
    m = 0
    while m <= 11:
        print ("{:>2} x {} = {:>2}".format(m, n, m*n))
        m += 1

   

        