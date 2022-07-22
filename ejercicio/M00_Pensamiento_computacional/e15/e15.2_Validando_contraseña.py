def acceder():
    print('\nAccede al sistema')
    usuarioAcceso = str(input('Nombre de usuario: ')) 
    contraseñaAcceso = str(input('Contraseña: '))

    if usuarioAcceso in usuarios and usuarios[usuarioAcceso] == contraseñaAcceso: #Valida que el usuario ingresado exista en la lista de usuarios y que la contraseña sea el valor de el usuario en el diccionario
        print('Entro al sistema :)')
    else: 
        print('No te conozco!, No entras >:(')




usuarios = {}                                       #Lista que contiene usuario y contraseña
print('\nRegistrate! ')
nombredeUsuario = str(input('Nombre de usuario: ')) 
contraseña = str(input('Contraseña: '))
usuarios[nombredeUsuario] = contraseña              #Añade el nombre de usuario como clave y la contraseña como valor de esa clave dentro del diccionario de usuarios

acceder()



