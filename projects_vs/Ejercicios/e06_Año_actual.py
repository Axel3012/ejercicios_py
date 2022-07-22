from datetime import datetime

edadActual = int(input('Que edad tienes?: '))
edadJubilacion = int(input('A que edad te jubilaras?: '))

añosRestantes = edadJubilacion - edadActual
añoActual  = datetime.today().strftime('%Y')
añoActual1 = int(añoActual)
añoJubilacion = añoActual1 + añosRestantes

if añosRestantes <= 0:
    print('Ya te puedes jubilar!')
else:
    print('Te quedan {} años para jubilarte'.format(añosRestantes))

    print('Estamos en {}, te jubilaras en {}.'.format(añoActual1, añoJubilacion))

