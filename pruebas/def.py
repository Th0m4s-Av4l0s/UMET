#def sirve para definir funciones creadas por
# el usuario para una tarea en especifico, son
# el equivalente a un modulo de JAVA

#Importante, las variables las cuales def toma
# con () deben estar declaradas despues del def
# y no antes
#EJ: 

print("=========Ejemplo 1=========")

def suma_tres(n):
    print(n+3);

suma_tres(4);

print("\n")

#primero definimos el nombre del modulo def
# luego en los parentesis el nombre de una
# variable declarada externa, y luego llenar
# dentro de del modulo lo que quieras

print("=========Ejemplo 2=========")

def tablas(n):
    for i in range(1,11):
        print(str(n) + " * " + str(i) + " = " + str(i*n))

tablas(8)

print(f"\n")

#return retorna valores, en este caso una cadena

print("=========Ejemplo 3=========")

def cadena():
    return "Hello world!"

print(cadena());

print("\n")

#Tambien def puede devolver valores si en los
# parametros tanto del def como la "llamada" 
# estan vacios, pero precisa declarar valores
# desde afuera o dentro del mismo def.
#EJ:

print("=========Ejemplo 4=========")

def funcion():
    n = 5
    print(n)

funcion()

print("\n")

#Cuidado cuando declaro variables, ya que es
# posible crear 2 variables con el mismo nombre
# dentro de un def y fuera del def, lo cual 
# puede llegar a causar confusion, por lo que
# la recomendacion es declarar variables con
# nombres diferentes o especificos
# Ej:
print("=========Ejemplo 5=========")

def dato():
    n = 2
    print(n)

#Aca se va a imprimir la variable 'n' del def
dato()

# Y aca se imprime la variable 'n' del main
n = 4
print(n)

# Ambas se llaman identicas pero pertenecen a
# diferentes planos, ademas la ide no lo 
# detectara como error

print("\n")

#Aca un ejemplo de un retorno y envio 
# de valores 

print("=========Ejemplo 6=========")

# Se pueden declarar variables de un def desde
# fuera del mismo, puede ser int, string, etc. 

def suma(a,b):
    return a+b;

respuesta = suma(4,8)
print(respuesta)

#Por medio de comas dentro de los parentesis
# las variables del def pueden ser declaradas

def palabras(a,b,c,d):
    return a + b + c + d

saludo = palabras("hola", " como estas", " amigo", " mio.")
print(saludo)