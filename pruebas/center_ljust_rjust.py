#El metodo center hace que en una cadena 
# se puedan definir espacios y el texto que se
# desea centrar en esos espacios

#Este metodo es ideal para adornar un codigo

cadena = "menu"
print(cadena.center(16, "="))

#Cuando se una el .center() el numero de 
# espacios debe ser mayor a la longitud de la
# cadena, y cuando se quiere colocar un
# caracter para rellenar los espacios, este
# debe ser un unico caracter (no mas de 1)

#El metodo .ljust() funciona igual que center
# solo que los espacios o caracteres agregados
# se colocan despues de la cadena

cadena = "menu"
print(cadena.ljust(16, "="))


#El metodo .rjust() funciona igual que center
# solo que los espacios o caracteres agregados
# se colocan antes de la cadena

cadena = "menu"
print(cadena.rjust(16, "="))