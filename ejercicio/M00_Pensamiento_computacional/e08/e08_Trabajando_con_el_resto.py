def rebanadasSobrantes():
    if NdePersonas % 2 == 1:
        rebanadasXpizza = NdePersonas + 1
    else:
        rebanadasXpizza = NdePersonas
    rsobrante = (rebanadasXpizza * NdePizzas) % NdePersonas
    return rsobrante

NdePersonas = int(input('Numero de personas: '))
NdePizzas = int(input('Numero de pizzas: '))

print('\n')
print('{} personas con {} pizzas'.format(NdePersonas, NdePizzas))
print('Cada persona toma {} piezas'.format(NdePizzas))

rs = rebanadasSobrantes()

print('Sobran {} porciones'.format(rs))




