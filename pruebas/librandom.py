#IMPORTANTE PARA IMPORTAR LIBRERIAS EN GENERAL: EVITAR 
# NOMBRAR MODULOS CON EL NOMBRE DE ALGUNA LIBRERIA, ESTO
# OCASIONA QUE EL PROGRAMA NO FUNCIONE


#Para usar random se debe importar la libreria random
# Comando: import random

print("=========Ejemplo 1=========\n")

import random
from tkinter import N

num = random.randint(1,6)

print(str(num));

#Tambien se puede importar la libreria random pero 
# colocandole un alias
# comando: import 'nombreLibreria' (EJ: random) as alias 
# (EJ: 'rd')

#Tambien se puede importar tanto la libreria random como
# alguna funcion en especifico sin tener que escribir
# random.randint()
# comando: 'from random import randint'
# Esto va a hacer que cuando declare una variable y le de
# un valor random, sea solo (EJ: num = randint(1,6))

#En caso de querer importar todas las funciones de la 
# libreria se debe usar el siguiente comando.
# comando: 'from nombreLibreria import *'


print("\n=========Ejemplo 2=========\n")

# randrange(int1) tiene la misma funcion que el random
# comun solo que elige un numero random entre 0 hasta el
# limite entre parentesis pero sin incluirlo
# EJ: randrange(6) devolvera entre 0 a 5

from random import *
n = randrange(6)
print(f"{n}");

#Tambien se puede colocar un minimo y maximo, pero aun
# asi sin incluir el ultimo numero, osea 4 a 5

n = randrange(4,6)
print(f"{n}");

#Tambien ademas de un minimo y maximo, el tercer argumento
# hace que el numero generado de un salto segun la cantidad
# establecida, aun asi, sin incluir el ultimo numero del
# segundo argumento

n = randrange(0,50,11)
print(f"{n}");


print("\n=========Ejemplo 3=========\n")

#El random sin argumentos siempre devuelve numeros
# flotantes

n = random();
print(f"{n}");

#El random uniform devuelve un numero random segun los
# parametros que se le de pero en tipo float, incluyendo
# los limites a diferencia de randrange()

n = uniform(1,10)
print(f"{n}")

print("\n=========Ejemplo 4=========\n")

# Choice retorna un caracter de forma aleatoria
# comando: choice(str1)

cadena = choice("Hola");
print(cadena);

#Tambien se puede usar choice con una lista de python,
# lo que devolvera aleatoriamente va a ser un elemento 
# de la lista que contenga una cadena
# EJ:

nombres = ["Rose", "Franco", "Harry", "Pablo"]
elemento = choice(nombres)
print(elemento)

print("\n=========Ejemplo 5=========\n")

#Sample() hace lo mismo que choice pero devolviendo varios
# elementos al azar de una lista

nombres = ["Rose", "Franco", "Harry", "Pablo"]
lista = sample(nombres,2)

print(lista)

#Tambien se puede usar sample() con una sola cadena,
# devolviendo asi caracteres aleatorios de la misma

nombre = "Thomas"

caracteres_random = sample(nombre,3)

print(caracteres_random);
