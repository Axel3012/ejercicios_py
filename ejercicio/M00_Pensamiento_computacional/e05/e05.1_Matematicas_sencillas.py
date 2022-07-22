def pedir_numero():
    valor = ""
    while valor == "" or valor < 0:
        try:
            valor = float(input("Ingresa numero: "))
            if valor < 0:
                print("Debe ser un nuemero positivo. Vuelva a intentarlo")
        except ValueError:
            valor = ""
            print("Debe ser un numero. Vuelva a intentarlo")
    
    return valor

n1 = pedir_numero()
n2 = pedir_numero()
while n2 == 0:
    print('Divicion entre 0 invalida, ingrese el dato de nuevo: ')
    n2 = pedir_numero()
    
suma = n1 + n2
resta = n1 - n2
producto = n1 * n2
division = n1 / n2

print('\nLa suma es: {}, la resta es: {}, la multiplicacion es: {}, la division es: {} '.format(suma,resta,producto,division))

      


