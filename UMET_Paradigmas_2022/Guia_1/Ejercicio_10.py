import random

dolares = 0.0
pesos = 0.0

print("====Conversor pesos y dolares====\n N° 1. Convertir dolar a peso \n N° 2. Convertir peso a dolar")

opcion = int(input("Elegir una opción:"))

dolar_valor = round(random.uniform(200,300),2);

while(opcion != 1 and opcion != 2):
    print("\n---Error, opcion no valida---\n");
    print("====Conversor pesos y dolares====\n N° 1. Convertir dolar a peso \n N° 2. Convertir peso a dolar");
    opcion = int(input("Elegir una opción:"))


if(opcion == 1):
    print(f"\n===Valor del dolar actual = {dolar_valor} pesos===");

    dolares = float(input("Cantidad de dolares a convertir: "));

    print(f"{dolares}USD$ convertidos a {dolares * dolar_valor}$ pesos")

else:
    print(f"\n===Valor del dolar actual = {dolar_valor} pesos===");

    pesos = float(input("Cantidad de pesos a convertir: "));

    print(f"{pesos}$ convertidos a {dolar_valor / pesos}USD$")
    

    


    