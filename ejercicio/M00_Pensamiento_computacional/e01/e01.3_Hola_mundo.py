import random

saludos = ['Hola, ', 'Saludos, ', 'Bienvenido, ', 'Hey!, ', 'Que onda!, ', 'Quibo, ']
cortesias = ['. ¿Como estas?', '. ¿Como has estado?', '. ¿Que me cuentas?', '. ¿Que tal tu dia?']

nombre = input('¿Como te llamas? ')
print('\n')

def selectRandom(saludos):
    return random.choice(saludos)

def selectRandom(cortesias):
    return random.choice(cortesias)

print(selectRandom(saludos)+ nombre + selectRandom(cortesias))


