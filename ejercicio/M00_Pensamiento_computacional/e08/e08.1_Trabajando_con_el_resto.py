def datoValido():
    try:
        dato = int(input())
        if dato < 0:
            quit()
    except ValueError:
        quit()
    return dato

def rebanadasSobrantes():
    if NdePersonas % 2 == 1:
        rebanadasXpizza = NdePersonas + 1
    else:
        rebanadasXpizza = NdePersonas
    rsobrante = (rebanadasXpizza * NdePizzas) % NdePersonas
    return rsobrante

def singularOplural():
    rs = rebanadasSobrantes()
    if rs == 1:
        print('Solo queda una rebanada de pizza!!')
    else:
        print('Sobran {} porciones'.format(rs))

print('Numero de personas: ')
NdePersonas = datoValido()
print('Numero de pizzas: ')
NdePizzas = datoValido()

print('\n')
if NdePizzas == 1:
    print('{} personas con una pizza'.format(NdePersonas))
else:
    print('{} personas con {} pizzas'.format(NdePersonas, NdePizzas))
    print('Cada persona toma {} piezas'.format(NdePizzas))

singularOplural()


