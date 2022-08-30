
#
nombre = input("Ingresar un nombre: ");

# El comando len() me permite contar la cantidad de
# caracteres y pasarlo como un int a otra variable
letras = len(nombre)

# Si el valor de la variable letras se divide por 2 y el
# el resto es 0, entonces es par, sino lo contrario
if(letras % 2 == 0):

    print(f"Este nombre es par");

else:

    print(f"Este nombre es impar")