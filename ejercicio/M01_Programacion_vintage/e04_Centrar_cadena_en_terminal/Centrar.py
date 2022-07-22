import shutil
def centrar(str1):
    columnas,filas = shutil.get_terminal_size((80,20))
    long = len(str1)
    spaceBack = (columnas-long)//2
    spaceFront = spaceBack*' '+str1

    return spaceFront

def centrar2(str1,columnas):
    if not isinstance(columnas, int):
        fail = 'Dato invalido'
        return fail

    if not isinstance(str1,str):
        fail = 'Dato invalido'
        return fail

    long = len(str1)
    spaceBack = (columnas-long)//2
    spaceFront = spaceBack*' '+str1

    return spaceFront





