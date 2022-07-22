numeros ={  1:'Primero', 2:'Segundo', 3:'Tercero', 4:'Cuarto', 
            5:'Quinto', 6:'Sexto', 7:'Septimo', 8:'Octavo',
            9:'Noveno', 10:'Decimo', 11:'Undecimo', 12:'Duodecimo'
         }

def numeroAordinal(num):
    if num > 0 and num <= 12:
        print('La traduccion al ordinal del {} es el {}'.format(num,numeros[num]))
    else:
        print('')

if __name__ == '__main__':
    for i in range(1, len(numeros)):
        print('{:2d} - {}'.format(i, numeros[i]))


