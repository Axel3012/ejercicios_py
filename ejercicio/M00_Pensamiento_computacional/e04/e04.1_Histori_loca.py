nombre = input('Como se llama el protagonista?: ')
verbo = input('Que esta haciendo?: ')
adverbio = input('Donde?, como? o cuando?, lo hace: ')
adjetivo = input('El adjetivo que se te ocurra: ')

output = '{} estaba {} {}, cuando un perro {} le mordio, pobre {} :c '

print('\n', output.format(nombre, verbo, adverbio, adjetivo, nombre))
