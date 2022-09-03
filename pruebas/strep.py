#El metodo .strip() elimina caracteres, saltos
# de linea o tabulaciones especificados por
# el usuario. 

# el problema es que esta borra 
# los caracteres en orden de ambos costados
# de la cadena, y si un caracter o espacio
# no esta definido en el metodo adjunto a la
# variable declarada, este no lo borrará
#EJ:

cadena = "Hola soy tom"
print("Cadena original -> " + cadena);

cadena = cadena.strip("H m o")
print("Cadena con strip -> " + cadena)

#rstrip() hace lo mismo pero en orden de
# derecha a izquierda en la cadena

cadena = "Hola soy tom"
cadena = cadena.rstrip(" om") 
print("Cadena con rstrip -> " + cadena)

#lstrip() hace lo mismo pero en orden de 
# izquierda a derecha en la cadena

cadena = "Hola soy tom"
cadena = cadena.lstrip(" aHHol")
print("Cadena con lstrip -> " + cadena)
