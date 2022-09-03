#Declaracion de variables
cuadro_1 = 0
cuadro_2 = 0
cuadro_3 = 0
antiguedad_cuadro1 = False
antiguedad_cuadro2 = False
antiguedad_cuadro3 = False
total_antiguos = 0


print("Cuadros del siglo XIX\n")


#Aca se ingresa el dato para la variable del 'cuadro_1'
cuadro_1 = int(input("Ingresar año de creación del primer cuadro:"));


#En caso de tener un valor menor al minimo, la variable
# 'total_antiguos' se concatena con un 1
if(cuadro_1 < 1891):
    total_antiguos += 1;



#Este while sirve como control de datos
while(cuadro_1 > 2000):

    print("\n---¡Error!, la fecha de los cuadros no debe exceder del año 2000---\n")


    cuadro_1 = int(input("Ingresar año de creación del primer cuadro:"));


    if(cuadro_1 < 1891):
        total_antiguos += 1;
        
        

#Nuevamente, el mismo caso que el primer while

cuadro_2 = int(input("Ingresar año de creación del segundo cuadro:"));


while(cuadro_2 > 2000):


    print("\n---¡Error!, la fecha de los cuadros no debe exceder del año 2000---\n")

    
    cuadro_2 = int(input("Ingresar año de creación del segundo cuadro:"));


    if(cuadro_2 < 1891):
        total_antiguos += 1;


# El mismo caso que en el primer while
cuadro_3 = int(input("Ingresar año de creación del tercer cuadro"));   

while(cuadro_3 > 2000):

    print("\n---¡Error!, la fecha de los cuadros no debe exceder del año 2000---\n")
    
    cuadro_3 = int(input("Ingresar año de creación del tercer cuadro"));   

    if(cuadro_3 < 1891):
        total_antiguos += 1;


#Dependiendo el valor de la variable 'total_antiguos, el
# programa finaliza con un mensaje.
if (total_antiguos == 0):
    print("\nRenovar stock.")

else:
    print(f"\nTotal de cuadros con antiguedad inferior a 10 años anterios al siglo XX = {total_antiguos}");


    







