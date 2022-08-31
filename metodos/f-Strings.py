#Otro equivalente a printf() en JAVA
# Se usa similar a .format() solo que se agrega
# una f antes de las "" y hay varias formas
# de como usar f-String
# EJ:

#Para simplemente imprimir
print(f"4+1")

#Para realizar operaciones aritmeticas de debe
# agregar "{}" donde este la operacion
print(f"4+1 = {4+1}")

#Tambien puede llamar a variables ya declaradas
nombre = "Tom"
edad = 20
altura = 1.83
print(f"{nombre} tiene {edad} años y una estatura de {altura} cm")

#Tambien se pueden realizar operaciones
# entre variables ya declaradas
num1 = 2
num2 = 2
print(f"{num1} + {num2} es igual a {num1 + num2}.")