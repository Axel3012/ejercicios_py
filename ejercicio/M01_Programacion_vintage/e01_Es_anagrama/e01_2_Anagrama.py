def esAnagrama(str1,str2):
    l2 = list(str2)
    comparacion = l2
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        letra1 = str1[i]
        match = []
        for j in range(len(l2)):
            letra2 = comparacion[j]
            if letra1 == letra2:
                match.append('/')
                comparacion = reemplazar(comparacion,match)
                break
            match.append(letra2)
    comparacion = ''.join(comparacion)
    return comparacion == '/'*len(str1)
 
def reemplazar(comparacion,match):
    if len(match) != len(comparacion):
        k = len(match)
        for k in range(k,len(comparacion)):
            match.append(comparacion[k])
    comparacion = match
    return comparacion

str1 = str(input('Primera Cadena: '))
str2 = str(input('Segunda Cadena: '))
if esAnagrama(str1,str2) == True:
        esOno = ' '
else:
    esOno = ' no '
print('{} y {}{}son anagramas'.format(str1,str2,esOno))





