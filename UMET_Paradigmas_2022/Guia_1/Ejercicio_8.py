#Declaracion de variables
numero = 0;
multiplicador = 0;


#Aca se ingresa un valor entero a la variable 'numero'
numero = int(input("Ingresar numero para mostrar su tabla: \n"));


#La variable 'multiplicador' al concatenar su valor 
# gradualmente, permite imprimir el producto del numero
# ingresado y el multiplicador de forma dinamica
for multiplicador in range(1,11):
    print(f"{numero} x {multiplicador} = {numero * multiplicador}")

