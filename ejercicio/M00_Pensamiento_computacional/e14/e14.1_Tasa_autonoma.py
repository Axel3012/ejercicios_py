#Solucion del profesor

tasa = 0.055

total = float(input('Precio de producto: '))
provincia = str(input('Provincia: ')).upper()

iva = total * tasa
ticket = ''

if provincia == 'VA':
    ticket = ('Subtotal: {}€ \nTasa: {}€\n'.format(total,iva))
    total = iva + total
    
print(ticket + 'Total: {}'.format(total))

