def esAnagrama(p1,p2):
    
    lp1 = list(p1)
    lp2 = list(p2)
    if len(str1) != len(str2):
        return lp2
    i = 0
    for i in range(len(lp1)):
        letra = lp1[i]
        if letra in lp2:
            lp2.remove(letra)
    return lp2


str1 = str(input('Primer cadena: '))
str2 = str(input('Segunda cadena: '))

anagrama = esAnagrama(str1,str2)
if len(anagrama) == 0:
    esOno = ' '
else:
    esOno = ' no '

print('{} y {}{}son anagramas'.format(str1,str2,esOno))








