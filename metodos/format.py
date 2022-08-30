#Es el equivalente al printf() de JAVA pero
#en forma de metodo para Python, hay distintas
#formas validas de usar este metodo
#EJ:

from hashlib import algorithms_guaranteed


palabra = "papel"
letras = 5

print("La palabra {} tiene {} letras".format(palabra, letras));

#O tambien se puede usar asi:

print("La palabra {palabra} tiene {letras} letras".format(palabra = "tijera", letras = 6))
#Las variables se deben colocar dentro de las llaves

#O tambien se puede usar asi:

palabra1 = "agua"
palabra2 = "mano"
letras = 4

print("Las palabras {0} y {1} ambas tienen {2} letras".format(palabra1, palabra2, letras))
#el orden dentro de .format() tiene que ver con
#el orden de escala numerica en programacion
#osea: 0,1,2,3...