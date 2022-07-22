mayusculas = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
minusculas = 'abcdefghijklmnñopqrstuvwxyz'

def myLower(str1):
    str2 = ''
    i = 0
    j = 0
    for i in range(len(str1)):
        caracter = str1[i]
        if caracter in mayusculas:
            for j in range(len(mayusculas)):
                if caracter == mayusculas[j]:
                    caracter = minusculas[j]
                    str2 += caracter
        else:
            str2 +=caracter
    return str2

def myLower2(str1):
    str2 = ''
    i = 0
    j = 0
    if isinstance(str1,str):
        for i in range(len(str1)):
            caracter = str1[i]
            if caracter in mayusculas:
                for j in range(len(mayusculas)):
                    if caracter == mayusculas[j]:
                        caracter = minusculas[j]
                        str2 += caracter
            else:
                str2 +=caracter
        return str2
    else:
        error = 'Dato Invalido'
        return error


#Solucion del profesor
def minusculas(cadena):
  res = ""
  for caracter in cadena:
    if caracter in mayusculas:
      res += chr(ord(caracter)+32)
    else:
      res += caracter
  return res
