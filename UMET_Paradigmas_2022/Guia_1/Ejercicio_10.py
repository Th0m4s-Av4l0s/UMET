import random

#Declaracion de variables
dolares = 0.0
pesos = 0.0
opcion = 0
dolar_valor = 0.0


#Este print sirve como menú
print("====Conversor pesos y dolares====\n N° 1. Convertir dolar a peso \n N° 2. Convertir peso a dolar")


#El usuario ingresa su eleccion a la variable
opcion = int(input("Elegir una opción:"))


#La variable 'dolar_variable' recibe un numero random 
# decimal, haciendo que el dolar tenga un diferente valor
# con cada ejecución del programa
dolar_valor = round(random.uniform(200,300),2);


#Este en un control de datos para la variable 'opcion'
while(opcion != 1 and opcion != 2):
    print("\n---Error, opcion no valida---\n");
    print("====Conversor pesos y dolares====\n N° 1. Convertir dolar a peso \n N° 2. Convertir peso a dolar");
    opcion = int(input("Elegir una opción:"))


#Dependiendo el valor de la variable 'opcion', el programa
# mostrara el valor actual de dolar y la cantidad que se
# desee convertir.
if(opcion == 1):


    #Aca los dolares son convertidos a pesos
    print(f"\n===Valor del dolar actual = {dolar_valor} pesos===");

    dolares = float(input("Cantidad de dolares a convertir: "));

    #El programa devuelve el total convertido con centavos
    # incluido
    print(f"{dolares}USD$ convertidos a {round(dolares * dolar_valor,2)}$ pesos")

else:

    #Aca los pesos son convertidos a dolares
    print(f"\n===Valor del dolar actual = {dolar_valor} pesos===");

    pesos = float(input("Cantidad de pesos a convertir: "));

    #De nuevo, el programa devuelve el valor total 
    # convertido con centavos incluido
    print(f"{pesos}$ convertidos a {round(dolar_valor / pesos,2)}USD$")
    

    


    