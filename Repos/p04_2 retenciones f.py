from f_retenciones1 import *

#Obtener datos de entrada
sueldo = float(input("Sueldo: "))
sit = input ("sit (1/2/3): ")
nhijos = int(input("Numero de hijos: "))

#Obtener Exencion

exencion = obtener_exencion(sit, nhijos)
        
sueldo_a_retener = sueldo - exencion

#Obtener retencion
porcentaje = obtener_retencion(sueldo_a_retener)
    
monto_anual = sueldo_a_retener * porcentaje / 100

monto_mensual = monto_anual / 12

#Mostrar resultados
print("Sueldo anual: \t", sueldo)
print("situacion: \t", sit)
print("base a retener:", sueldo_a_retener)
print("Porcentaje:\t", porcentaje)
print("Total anual:\t", monto_anual)
print()
print("Retencion mensual:", monto_mensual)

    

        
    
        

