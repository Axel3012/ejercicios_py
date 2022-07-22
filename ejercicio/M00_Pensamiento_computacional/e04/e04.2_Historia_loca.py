nombre = input('como se llama el protagonista?: ')

print('Instrucciones: Lee el desarrollo de la historia y elige la ruta que mas te guste con 1 o 2', '\n')
introduccion = 'Un dia tranquilo en el dia de {} se disponia para ir a la escuela, cuando de repente se dio cuenta que habia olvidado su almuerso en la casa, pero ya tenia el tiempo justo para llegar a la primera clase, due cuando penso \n - rayos!!.\n debo regresar a casa por mi almuerzo? si no lo hago morire de hambre en el dia, pero si voy llegare tarde a la escuela y me regañaran!, ¿que debo hacer?'
selec1 = 'Decidi ir a casa por mi almuerzo, llegue 10 minutos tarde a clases, la directora me llamo a detencion, en detencion me encontre con una amiga que siempre esta ahi.\n- Oye deberiamos escaparnos, se perfectamente como hacerlo, vienes?.\nQue hago? deberia ir?, si me atrapan estare en muchos problemas, pero me muero de aburrimiento!!'    
selec1_1 = 'Pues al final nos escapamos de la escuela, fuimos al cine a ver una pelicula increible, paseamos por la ciudad, fuimos por unos helados y creo que es el inicio de algo mas..., no me imaginaba que mi amiga rebelde fuera tan divertida, en fin la regañiza que me espera en casa valadra la pena!'
selec1_2 = 'E decidido aguantarme el aburrimiento, estube todo el dia en detencion y lo peor que lo he pasado solo, porque mi amiga se a escapado y yo me quede aqui solo desempolbando archivos de hace 2 decadas... bueno almenos me e comido mi almuerzo. '
selec2 = 'Decidi llegar a tiempo a clases, cuando llego la hora de el almuerzo no tenia nada para comer, cuando de repente. \n-Que pasa amigo, no haz trido nada de almorsar?.\nNo conocia a este chico pero parece agradable, \n-Ten te doy la mitad dde mis tacos, pero acambio de que le lleves esta nota a esa chica, es una confecion de amor pero me da un poco de pena entregarcela, que dices se la llevas por la mitad de mis tacos?'
selec2_1 = 'Tengo muchisima hambre y sus tacos se ven deliciosos, que mas da le llevare la nota. \n- Hola, oye ten esta nota... \nEso fue incomodo todos me miraban, pero bueno ahora ire por esos tacos!!. \n- Enserio!!? \nEscuche que me gritaron. \n-Tu tambien me gustas, y si quiero ser tu novia \nQue acaba de pasar??, noo!! es un mal entendido...creo que me acabo de quedar sin tacos, pero con nueva novia!! :o'
selec2_2 = 'A pesar de tener tanta hambre decidi no aceptar, no se quien es el chico y la chica va en mi clase aunque nno hablamos mucho, supongo que tendre que esperar a casa para poder comer algo, intentare no desmayarme en el dia!'
fin = 'FIN.'
print (introduccion.format(nombre), '\n')

ruta = input('1. Volvere a casa por mi almuerzo? \n2. Llegar a tiempo a la escuela? \n1 o 2? ')

print('\n')

if ruta == '1':
    print (selec1, '\n')
    ruta1 = input('1. Me escapare del castigo? \n2. Cumplire el castigo! \n1 o 2? ')
    print('\n')
    if ruta1 == '1':
        print (selec1_1,'\n')
        print(fin)
    else:
        print (selec1_2,'\n')
        print(fin)
        
else:
    print (selec2, '\n')
    ruta2 = input('1. Llevar la nota a la chica a cambio de la mita de los tacos? \n2. Aguantar el hambre! \n1 o 2? ')
    print('\n')
    if ruta2 == '1':
        print (selec2_1,'\n')
        print(fin)
    else:
        print (selec2_2,'\n')
        print(fin)
    
    




    
