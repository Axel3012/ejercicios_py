def datoValidoRep(plantilla):
    dato = ''   
    while dato == '':
        try:
            dato = float(input(plantilla))   
            if dato < 0:
                dato = ''           
        except ValueError:
            dato = ''
    return dato

def entradaValida(plantilla,opciones):
    tipo = ''
    while tipo == '':       
        tipo = str(input(plantilla))
        tipo = tipo.upper()
        if tipo in opciones:
            return tipo
        else:
            print('Opcion incorrecta, debe ser un pais de la Union Europea')
            tipo = ''

paises = {
            'HUNGRIA':27,'CROACIA':25,'DINAMARCA':25,'SUECIA':25,
            'FINLANDIA':24,'RUMANIA':24,'GRECIA':23,'IRLANDA':23,
            'POLONIA':23,'PORTUGAL':23,'ESLOVENIA':22,'ITALIA':22,
            'ESPAÑA':21,'BELGICA':21,'LETONIA':21,'LITUANIA':21,
            'PAISES BAJOS':21,'REPUBLOCA CHECA':21,'AUSTRIA':20,
            'BULGARIA':20,'ESLOVAQUIA':20,'ESTONIA':20,'FRANCIA':20,
            'REINO UNIDO':20,'ALEMANIA':19,'CHIPRE':19,'MALTA':18,'LUXEMBURGO':15
            }

pais = entradaValida('Pais que emite la factura: ',paises)
subtotal = datoValidoRep('Subtotal: €')

ivaPais = paises[pais]/100
iva = ivaPais * subtotal
total = subtotal + iva

print('\nFactura emitida por {}\nIVA aplicado del {}%\nSubtotal: {:.2f}€\nIVA: {:.2f}€\nTOTAL: {:.2f}€'.format(pais,paises[pais],subtotal,iva,total))


