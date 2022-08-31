#El metodo .count() sirve para contar en una
# cadena de caracteres, algun caracter en 
# especifico que el usuario desee saber
# .count() utiliza 3 parametros, 2 de ellos
# son opcionales

#variable.count("n", inicio, fin)

#.count() comenzaria de izquierda a derecha, y
# debido a que cuenta el inicio antes del primer
# caracter, siempre se suma 1 al total de 
# caracteres contados

# El orden de contar para .count() puede ser
# invertido si en inicio se le da un numero 
# negativo, y comenzaria a contar de derecha
# a izquierda

cadena = "mi mamá me mima"
print(cadena.count("m", 3, 7))

#El count empezaria en i y terminaria en la 
# segunda m (i||m|a|m|)

cadena = "mi mamá me mima"
print(cadena.count("m", -4, -1))

#Cuando se usa inicio negativo, se invertiria
# el inicio y fin, siendo -4 fin y -1 inicio
