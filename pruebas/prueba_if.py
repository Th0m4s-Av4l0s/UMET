numero = 0

num_float = 0.0

numero = int(input("Ingresar numero 1 a 5: "))

if(numero > 5):
    print("Tu numero ingresado es mayor a 5")

elif(numero < 1):
    print("tu numero es menor a 1")

else:
    #con Str() se puede convertir int a Str
    print("Tu numero ingresado es: " + str(numero))


num_float = float(input("Ingresar float: "))

print(round(num_float,2))