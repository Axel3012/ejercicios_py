class Asignatura():
    def __init__(self, nombre, nivel):
        self.nombre = nombre    
        self.nivel = nivel
        self.hora = 0

    def __str__(self):
        return 'Asignaturas {} - {} - ({:.2f}/ $/mes)'.format(self.nombre, self.nivel, self.hora * 4)

    def __repr__(self):
        return self.__str__()

class Persona():
    def __init__(self, n, ap):
        self.nombre = n
        self.apellidos = ap
        self.movil = ''
        self.correo_e = ''

        self.asignaturas = []

    def alta_asignatura(self, asignatura):
        if not isinstance(asignatura, Asignatura):
            raise Exception ('{} debe ser deñ tipo Asignatura'.format(asignatura))
    
        self.asignaturas.append(asignatura)
   
    def __str__(self):
        # return 'Persona : {} {} - {}'.format(self.nombre, self.apellidos, self.correo_e)
        return '{}: {} {} - {}'.format(type(self).__name__, self.nombre, self.apellidos, self.correo_e )
 
    def __repr__(self):
        return self.__str__()


class Alumno(Persona): 
    pass 

class Profesor(Persona):
    def __init__(self, n, ap, nif, correo_e, sueldo_base = 200):
        # Persona.__init__(self, n, ap)
        super().__init__(n, ap)

        self.sueldo_base =  sueldo_base
        self.nif = nif

    @property
    def sueldo(self):
        return self.sueldo_base + len(self.asignaturas) * 300
 






