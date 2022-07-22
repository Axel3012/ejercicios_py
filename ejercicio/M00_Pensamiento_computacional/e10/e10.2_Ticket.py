def datoValido():   
    try:
        dato = int(input())
        if dato < 0:
            quit()
    except ValueError:
        quit()
    return dato

def datoValidof():   
    try:
        dato = float(input())
        if dato < 0:
            quit()
    except ValueError:
        quit()
    return dato

def datosdeProductos():
    i = 0
    for i in range(numerodeProductos):       
        nombredeProductoN = input('Nombre del producto {}: '.format(i))
        print('Precio de {} $: '.format(nombredeProductoN))
        precioProductoN = datoValidof()
        productos[nombredeProductoN]= precioProductoN

def unidadesVendidas():
    i = 0
    for i in productos.keys():
        nombredeProductoN = i
        print('Unidades vendidas de {}:'.format(nombredeProductoN))
        unidadesVendidasN = datoValido()
        unidadesdeProductos.append(unidadesVendidasN)

def ventasNetas():
    i = 0  
    j = 0
    for i in productos.values():
        precioProductoN = i
        unidadesVendidasN = unidadesdeProductos[j]
        ventaNetaN = precioProductoN * unidadesVendidasN
        ventasdeProductos.append(ventaNetaN)
        j += 1

def iva():
    i = 0
    for i in range(numerodeProductos):
        ventaNetaN = ventasdeProductos[i]
        ivaN = ventaNetaN * impuesto
        ivaProductos.append(ivaN)

def total():
    i = 0
    for i in range(numerodeProductos):
        ventaNetaN = ventasdeProductos[i]
        ivaN = ivaProductos[i]
        totalN = ventaNetaN + ivaN
        ventasBrutas.append(totalN)

def ticket():

    i = 0 
    j = 0
    for i in productos.keys():
        nombreN = i
        uvN = unidadesdeProductos[j]
        ventaNetaN = ventasdeProductos[j]
        impuestoN = ivaProductos[j]
        TotalN = ventasBrutas[j]
        j += 1
   
        print('\n')

        print('Unidades vendidas de {}: {}'.format(nombreN,uvN))
        print('Subtotal: ${} '.format(ventaNetaN))
        print('IVA: ${} '.format(impuestoN))
        print('_'*30 )
        print('Total: ${} '.format(TotalN))
        print('_'*30, '\n' )
        
impuesto = 0.055
productos = {}
unidadesdeProductos = []
ventasdeProductos = []
ivaProductos = []
ventasBrutas = []
print('Cuantos productos vas registrar?:')
numerodeProductos = datoValido()
datosdeProductos()
unidadesVendidas()
ventasNetas()
iva()
total()
ticket()
granTotal = sum(ventasBrutas)
print('TOTAL: ${} '.format(granTotal))




















