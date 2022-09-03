# El metodo .startswith() hace lo mismo que 
# count() solo que verifica mediante un valor
# bool si en una cadena de caracteres comienza
# con un caracter o un conjunto de caracteres
# en especifico de izquierda a derecha

# Al igual que count, el metodo .startswith()
# posee 3 parametros:
# .startswith("n" , inicio, fin) 

cadena = "Diana se peina sola"
print(cadena.startswith("se", 6));
#Es true porque comienza en el caracter 6 para 
# adelante, el metodo lee a partir de 6, ve una
# s y lee, ve una e y con eso ya devuelve TRUE


# El metodo -endswith() hace lo mismo que
# startswith solo que comienza de derecha a
# izquierda

#Tambien posee 3 parametros:
# .endswith("n", inicio, fin)

cadena = "Diana se peina sola"
print(cadena.endswith("ola"))