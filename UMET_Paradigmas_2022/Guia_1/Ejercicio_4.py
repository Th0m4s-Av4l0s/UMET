#Declaracion de variable e ingreso de dato
x = int(input("Ingresar numero entero: "))

#Para que un valor devuelva el ultimo digito se divide 
# el valor ingresado % 10, esto devuelve el resto

#En caso de que el valor ingresado sea mayor a 10 y 100
# mostrará el ultimo digito y los 2 ultimos
if(x > 10 and x > 100):
    print(f"\nUltimo digito: {x % 10} | Ultimos dos digitos: {x % 100}");

#En caso de que el valor ingresado sea menor a 100 solo
# mostrará el ultimo digito
elif(x > 10):
    print(f"\nUltimo digito: {x % 10}");

    
    