from argparse import BooleanOptionalAction


tupla = ("Tom", 13, 1, 1995)

print(tupla)


print("\n")
print("=========Ejemplo 2=========")
#Para convertir una tupla en una lista se 
# debe usar el comando list

tupla = ("tom", 12)

lista = list(tupla)

print(lista)

#Tambien una lista puede convertirse en una 
# tupla con el comando tuple

lista = ("tom", 12)

tupla = tuple(lista)

print(tupla)


print("\n")
print("=========Ejemplo 3=========")
# Se pueden comprobar si existen elementos
# dentro de una tupla usando el comando 'in'

tupla = ("tom", 12)
print("tom" in tupla)



print("\n")
print("=========Ejemplo 4=========")
# Se puede averiguar la cantidad de un
# elemento en especifico si existe 1 o mas
# dentro de una tupla con el comando '.count()'
# En este caso contara cuantos 'tom' hay
# EJ:

tupla = ("tom", 12, "tom")

print(tupla.count("tom"))



print("\n")
print("=========Ejemplo 5=========")
#Para averiguar la longitud de una tupla
#(y posiblemente funcione con listas) se debe 
# utilizar el comando 'len()'

tupla = (5,5,5,5,5)

print(len(tupla))

#Una tupla unitaria significa que es una tupla
# con un unico valor dentro, para lograr esto
# cuando se coloca el primer y unico valor,
# le sigue una coma
tupla = ("tom",)

print(len(tupla))



print("\n")
print("=========Ejemplo 6=========")
#Por lo general cuando declaro una tupla, esta
# se le conoce como un 'empaquetado de tupla'
# pero es posible desempaquetarla, osea,
# poner sus valores en variables independientes

tupla = ("tom", 2, True, 1.5)

cadena, num_entero, boleano, n_real = tupla

print(cadena)
print(num_entero)
print(boleano)
print(n_real)