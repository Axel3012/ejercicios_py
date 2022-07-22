dias = [31,28,31,30,31,30,31,31,30,31,30,31]

def es_bisiesto(year):
    if year % 4 != 0:
        return False
    if year % 100 == 0 and year % 400 !=0:
        return False
    
    return True
    

#Pedir datos
dia = int(input ("Dia: "))
mes = int(input ("Mes: "))
año = int(input ("Año: "))

#Comprobar bisiesto
if es_bisiesto (año):
    dias[1]=29

#contar los dias de meses anteriores
compara_mes = 0
contador_dias = 0

while compara_mes < mes - 1:
    contador_dias += dias[compara_mes]
    compara_mes += 1
    
contador_dias += dia

print ("El dia es:", contador_dias)

 
    