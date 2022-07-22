def lista():
    print('Primera fila - Segunda fila - Tercera fila - Cuarta fila')
    espacios = '\t\t'
    for i in range(24):
        a = chr(32+i)
        b = chr(56+i)
        c = chr(80+i)
        d = chr(104+i-1)
        print('{}{}{}{}{}{}{}'.format(a,espacios,b,espacios,c,espacios,d))

#Solucion del profe
def listaprofe():
    for c in range(32, 128):
        print("'{}': {:3d}".format(chr(c), c), end="\t")
        if c % 4 == 3:
            print("")

if __name__ == '__main__':
    lista()
