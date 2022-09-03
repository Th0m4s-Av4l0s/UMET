import random

#Declaracion de variables
numeros_aleatorios = list(range(0, 15))
x = 0
num_1 = 0
num_2 = 0
num_3 = 0
num_acertado1 = False
num_acertado2 = False
num_acertado3 = False

print("==========BINGO==========")


#Con este for le doy los valores a cada espacio de la
# lista 'numeros_aleatorios' , el print de abajo es para
# testear que funcione, se puede borrar.
for x in range(0, 15):
    numeros_aleatorios [x]  = random.randint(1,100)
    print(numeros_aleatorios[x], end = "-")


#Aca se ingresan los valores para los 3 numeros
num_1 = int(input("\nIngresar primer numero: "));
num_2 = int(input("Ingresar segundo numero: "));
num_3 = int(input("Ingresar tercer numero: "));


#De nuevo uso el range pero para confirmar que se 
# acertaron los numeros elegidos
for x in range (0, 15):

    if(num_1 == numeros_aleatorios[x]):
        num_acertado1 = True

    elif(num_2 == numeros_aleatorios[x]):
        num_acertado2 = True

    elif(num_3 == numeros_aleatorios[x]):
        num_acertado3 = True


#Dependiendo si el usuario falla todos los numeros,
# acierta todos los numeros, o algunos, el programa
# devolvera un mensaje distinto.

#Aca use las 3 variables tipo bool
if(num_acertado1 == False and num_acertado2 == False and num_acertado3 == False):
    print("Mala suerte!, no acertaste ningun numero.");

elif(num_acertado1 == True and num_acertado2 == True and num_acertado3 == True):
    print("Buena suerte!, acertaste todos los numeros");

else:

    #De nuevo uso range, en este caso si el usuario no
    # acertó todos los numeros
    for x in range(0, 15):
        
        if(num_1 == numeros_aleatorios[x]):
            print(f"Lograste marcar el numero {num_1}");

        elif(num_2 == numeros_aleatorios[x]):
            print(f"Lograste marcar el numero {num_2}");
        

        elif(num_3 == numeros_aleatorios[x]):
            print(f"Lograste marcar el numero {num_3}");



