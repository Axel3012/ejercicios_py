def datoValido():
    try:
        dato = int(input())
        if dato < 0:
            quit()
    except ValueError:
        quit()
    return dato

def rebanadasSobrantes(ndePizzas):
    rebandasTotales = ndePizzas * rebanadasXpizza
    rebanadasRestantes = rebandasTotales % numerodePersonas

    return rebanadasRestantes

def pizza(rs):
    numerodePizzas = 1
    rebanadasXpizzaTotal = 0
    while rebanadasXpizzaTotal < rs:       
        numerodePizzas += 1
        rebanadasXpizzaTotal = rebanadasXpizza * numerodePizzas
    print('se deben de comprar {}'.format(numerodePizzas))
    rs = rebanadasSobrantes(numerodePizzas)
    print('Sobran {} rebanadas de pizza'.format(rs))

def todos():
    print('Cuantas rebanadas le toca a cada persona?:')
    numerodeRebanadas = datoValido()
    rebanadasSolicitadas = numerodePersonas * numerodeRebanadas
    pizza(rebanadasSolicitadas)

def diferentes():
    i = 0
    suma = []
    for i in range(numerodePersonas):
        print('Cuantas rebanadas quiere persona {}:'.format(i))
        rebanadas = datoValido()
        suma.append(rebanadas)
    rebanadasSolicitadas = sum(suma)
    pizza(rebanadasSolicitadas)

print('Cuantas personas iran a la reunion?: ')
numerodePersonas = datoValido()
rebanadasXpizza = 8
mismo = str(input('El numero de rebanadas es el mismo para todos (s/n)?: '))

if mismo == 's':
    todos()
else:
    diferentes()



