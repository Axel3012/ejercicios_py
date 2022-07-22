def datoValidof(plantilla):   
    try:
        dato = float(input(plantilla))
        if dato < 0:
            quit()
    except ValueError:
        quit()
    return dato

tasadeCambio = datoValidof('Tasa de cambio: ')
dolares = datoValidof('Dolares: $')

euros = dolares * tasadeCambio

print('${} a una tasa de cambio de {}:'.format(dolares, tasadeCambio))
print('Total: €{:.2f} '.format(euros))


