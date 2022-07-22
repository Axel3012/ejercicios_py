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

def entradaValida(plantilla,completo, acotado):
      
    provincia = str(input(plantilla)).upper()
    if len(provincia) > 2:
        if provincia in completo:
            tasa = completo[provincia]
            return tasa
        else:
            return 0
    else: 
        if provincia in acotado:
            tasa = acotado[provincia]
            return tasa
        else:
            return 0

provinciasL = {'VALENCIA':0.055, 'MADRID':0.11, 'BARCELONA':0.084}
provinciasC = {'VA':0.055, 'MA':0.11, 'BA':0.084}

producto = datoValidof('Precio de producto: €')
tasaProvincia = entradaValida('Provincia:',provinciasL,provinciasC)
tasaTotal = producto * tasaProvincia
total = tasaTotal + producto

print('Subtotal: €{:.2f} \nTasa: {:.2f}€ \nTotal: {:.2f}€'.format(producto,tasaTotal,total))






