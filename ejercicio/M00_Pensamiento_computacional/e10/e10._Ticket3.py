impuesto = 0.055
nombre1 = input('Nombre del Primer producto: ')
precio1 = float(input('Precio de {}: '.format(nombre1)))
nombre2 = input('Nombre del segundo producto: ')
precio2 = float(input('Precio de {}: '.format(nombre2)))
nombre3 = input('Nombre del tercer producto: ')
precio3 = float(input('Precio de {}: '.format(nombre3)))

uv1 = int(input('Unidades vendidas de {}: '.format(nombre1)))
uv2 = int(input('Unidades vendidas de {}: '.format(nombre2)))
uv3 = int(input('Unidades vendidas de {}: '.format(nombre3)))

ventaNeta1 = precio1 * uv1
ventaNeta2 = precio2 * uv2
ventaNeta3 = precio3 * uv3

impuesto1 = impuesto * ventaNeta1
impuesto2 = impuesto * ventaNeta2
impuesto3 = impuesto * ventaNeta3

Total1 = ventaNeta1 + impuesto1
Total2 = ventaNeta2 + impuesto2
Total3 = ventaNeta3 + impuesto3

print('\n')

print('Unidades vendidas de {}: {}'.format(nombre1,uv1))
print('Subtotal: {}'.format(ventaNeta1))
print('IVA: {}'.format(impuesto1))
print('_'*30 )
print('Total: {}'.format(Total1))
print('_'*30, '\n' )

print('Unidades vendidas de {}: {}'.format(nombre2,uv2))
print('Subtotal: {}$'.format(ventaNeta2))
print('IVA: {}$'.format(impuesto2))
print('_'*30 )
print('Total: {}$'.format(Total2))
print('_'*30, '\n' )

print('Unidades vendidas de {}: {}'.format(nombre3,uv3))
print('Subtotal: {}$'.format(ventaNeta3))
print('IVA: {}$'.format(impuesto3))
print('_'*30 )
print('Total: {}$'.format(Total3))
print('_'*30, '\n' )








