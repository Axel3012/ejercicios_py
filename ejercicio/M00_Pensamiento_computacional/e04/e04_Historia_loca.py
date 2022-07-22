nombre = input('Como se llama el protagonista?: ')
verbo = input('Que esta haciendo?: ')
adverbio = input('Donde?, como? o cuando?, lo hace: ')
adjetivo = input('El adjetivo que se te ocurra: ')

plantilla = '0 estaba 1 2, cuando un perro 3 le mordio, pobre 0 :c '

i = 0
frase = ''

while i < len(plantilla):
    letra = plantilla[i]
    
    if letra == '0':
        frase += nombre
    elif letra == '1':
        frase += verbo
    elif letra == '2':
        frase += adverbio
    elif letra == '3':
        frase += adjetivo
    else:
        frase += letra
    i += 1
    
print(frase)

    
        
        
        
        



