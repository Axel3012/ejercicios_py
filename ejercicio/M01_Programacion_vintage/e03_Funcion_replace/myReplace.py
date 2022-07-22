#Remplaza el caracter de la posicion solicitada por uno nuevo
def myReplace(str1,pos,new):
    new = str(new)
    replace1 = str1[:pos]
    replace2 = str1[pos+1:]
    str2 = replace1+new+replace2
    return str2

#Solucion del profesor
def myReplacep(cadena, posicion, nuevoValor):
  indice = 0
  resultado = ""
  while indice < len(cadena):
    if indice == posicion:
      resultado += nuevoValor
    else:
      resultado += cadena[indice]
      
    indice += 1

  return resultado

#Remplaza el caracter de la posicion solicitada por uno nuevo
def myReplacefor(str1, pos, new):
    i = 0
    str2 = ''
    for i in range(len(str1)):
        caracter = str1[i]
        if i == pos:
            str2 += new
        else:
            str2 += caracter
    return str2

#Remplaza todas las letras de una cadena por una nueva
def myReplaceLetra(str1, old, new):
    str2 = str1
    for i in range(len(str1)):
        if old in str2:
            caracter = str2[i]
            if caracter == old:
                replace1 = str2[:i]
                replace2 = str2[i+1:]
                str2 = replace1 + new + replace2
    return str2
                




