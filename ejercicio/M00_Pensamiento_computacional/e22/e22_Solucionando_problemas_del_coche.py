def entradaValida(plantilla,opciones):
    tipo = ''
    while tipo == '':       
        tipo = str(input(plantilla))
        tipo = tipo.lower()
        if tipo in opciones:
            return tipo
        else:
            print('Opcion incorrecta. puede elejir: {}'.format(opciones))
            tipo = ''

opciones = ['s','n']


def tomaDeciciones():
    step1 = entradaValida('Arranca?(s/n): ',opciones)
    if step1 == 's':
        step2_s = entradaValida('Suena un clic-clic?(s/n): ',opciones)
        if step2_s == 's':
            solucion = 'Reemplaza la bateria'
            return solucion
        step3_s_n = entradaValida('Se enciende el coche pero no arranca?(s/n): ',opciones)
        if step3_s_n == 's':
            solucion = 'Revisa las bujias'
            return solucion
        step4_s_n_n = entradaValida('Arranca el coche y luego se cala?(s): ',opciones='s')
        step5_s_n_n_s = entradaValida('Tiene el coche inyeccion de combustible?(s/n): ',opciones)
        if step5_s_n_n_s == 's':
            solucion = 'Lleve el coche al taller'
            return solucion
        solucion = 'Abre y cierra el starter'
        return solucion
    step2_n = entradaValida('Estan los bordes de la bateria corroidos?(s/n): ',opciones)
    if step2_n == 's':
        solucion = 'Limpia los bornes y arranca de nuevo'
        return solucion
    solucion = 'Reemplaza los cables y arranca de nuevo'
    return solucion

solucion = tomaDeciciones()
print('Sugerencia de solucion: {}'.format(solucion))




