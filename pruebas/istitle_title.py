#El metodo .istitle() es que sirve como un
# bool que determina si una cadena de caracteres
# estan en minusculas o no.

# Si lo esta es True
# y de lo contrario que no esté en minusculas
# todos los caracteres es False
#EJ:

cadena = "hOlA"
cadena = cadena.istitle()
print(cadena)

#El metodo .title() hace que cualquier cadena
# de caracteres se convierta de forma que:

# el caracter inicial de cada cadena este
# en mayusculas y el resto en minusculas
# este metodo es mas ideal para nombres
#EJ:

cadena = "Hola como estas"
print(cadena.title())

#Una vez usado el .title() en una variable Str
#Esta queda permanente a menos que se edite
print(cadena)


