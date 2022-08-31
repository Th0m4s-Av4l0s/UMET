#Es el equivalente a los arrays en JAVA

# La diferencia entre el array Python a 
# otros lenguajes es que permite guardar 
# diferente tipo de datos dentro de las casillas

# Además los array de python se pueden expandir
# dinamicamente

# las posiciones de una lista
# [casilla 1, casilla 2, casilla 3, etc.]
# comienza desde 0 en adelante

#EJ:

print("=========Ejemplo 1=========")

lista = ["Hola", " como", " estas", " amigo"]

print(lista[0:4])



print("\n")
print("=========Ejemplo 2=========")
#Es posible agregar valores a las listas, de 
# forma que se expandan, esto se logra con
# .append()

#Cuidado, .append() solo permite agregar 1 solo
# valor a la lista

lista = ["Hola", " como"]

lista.append("estas")

print(lista[:])


print("\n")
print("=========Ejemplo 3=========")
# Tambien se puede insertar valores en una 
# lista pero de forma específica con el
# comando .insert()

lista = ["Hola", "estas"]

lista.insert(1, "como")

print(lista[:])



print("\n")
print("=========Ejemplo 4=========")
#A diferencia de .append() que agrega 1 solo
# valor a una lista, con .extend([]) y mediante
# comas separando cada nuevo valor, se pueden
# agregar mas 1 elemento nuevo a la lista

lista = ["Hola"] 

#Asegurarse de colocar los corchetes dentro de
# los parentesis cuando se usa .extend([])

lista.extend(["como", "estas", "amigo", "mio"])

print(lista[:])



print("\n")
print("=========Ejemplo 5=========")
#Cuando queremos saber en que casilla se
# encuentra un valor, se utiliza un .index()
# Ej:

lista = ["Hola", "como", "estas"]

print(lista.index("como"))

#Esto tambien se puede hacer con una lista
# que fue extendida con un .extend()

lista.extend(["amigo" , "mio"])

print(lista.index("mio"))



print("\n")
print("=========Ejemplo 6=========")
#Tambien se pueden devolver valores de tipo
# booleano cuando se solicita saber si 
# existe un valor y que devuelva TRUE si es asi

lista = ["Hola", "como"]

print("Hola" in lista)


print("\n")
print("=========Ejemplo 7=========")
#Varios tipos de datos pueden ser almacenados
# en una lista de Python

lista = ["Hola", 9, False, 55.3]

lista.extend([True, "Amigo"])

print(lista[2])


print("\n")
print("=========Ejemplo 8=========")
#Para eliminar datos de una lista se utiliza
# el comando .remove()

lista = [1,2,3,4]

lista.remove(3);

#Imprimiria todo menos el 3
print(lista[:])

#Para eliminar el ultimo valor de una lista
# utilizo el comando .pop()

lista = [1,2,3,4]

lista.pop()

print(lista[:]);


print("\n")
print("=========Ejemplo 9=========")
#Ademas de .entend() se pueden concatenar listas
# distintas si se usa una simple concatenacion

lista1 = ["Hola", "Como"]

lista2 = ["Estas", "Amigo"]

lista3 = lista1 + lista2

print(lista3)

#Tambien se puede multiplicar una lista si 
# se usa un asteristco

lista1 = ["Hola", "Como"] * 3

print(lista1);