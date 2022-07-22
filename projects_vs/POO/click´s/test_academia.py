from academia import Alumno, Asignatura, Profesor

roberto = Alumno('Roberto', 'Rodriguez')
susana = Alumno('Susana', 'Martin')

print(roberto.nombre, roberto.apellidos, roberto) # Roberto Rodriguez
print(susana.nombre, susana.apellidos, susana) # Susana Martin

print(roberto.correo_e, roberto.movil) #

ingles = Asignatura('ingles', 'A2')
ingles.hora = 7.50
aleman = Asignatura('Aleman', 'A2')
aleman.hora = 8

chino = Asignatura('Chino Cantones', 'A2')
chino.hora = 10


print(ingles) # Asignatura: Ingles - A2 - (30 $/mes)

roberto.alta_asignatura(ingles)
roberto.alta_asignatura(chino)


print(roberto.asignaturas) # [Asignatura: Ingles - A2 - (7.5 $/mes), Asignatura: Chino....]
print(susana.asignaturas) #

donJose = Profesor('Jose', 'Martin Fusta', '0W', 'jf@gmail.com') 
print(donJose) #Profesor: 0w - Jose Martin Fusta - jf@gmail.com

print(donJose.sueldo) #200

donJose.alta_asignatura(ingles)

print(donJose.asignaturas) # [Asignatura: Ingles - A2 - (30 $/mes)]

print(donJose.sueldo) #500

