cuadro_1 = 0
cuadro_2 = 0
cuadro_3 = 0
antiguedad_cuadro1 = False
antiguedad_cuadro2 = False
antiguedad_cuadro3 = False
total_antiguos = 0


print("Cuadros del siglo XIX\n")

while(cuadro_1 > 2000):

    cuadro_1 = int(input("Ingresar año de creación del primer cuadro:"));

    if(cuadro_1 > 2000):
        print("\n---¡Error!, la fecha de los cuadros no debe exceder del año 2000---\n")
    
    elif(cuadro_1 < 1891):
        antiguedad_cuadro1 = True;
        total_antiguos += 1;
        
        


while(cuadro_2 > 2000):
    
    cuadro_2 = int(input("Ingresar año de creación del segundo cuadro:"));

    if(cuadro_2 > 2000):
        print("\n---¡Error!, la fecha de los cuadros no debe exceder del año 2000---\n")

    elif(cuadro_2 < 1891):
        antiguedad_cuadro2 = True;
        total_antiguos += 1;

while(cuadro_3 > 2000):
    
    cuadro_3 = int(input("Ingresar año de creación del tercer cuadro"));   

    if(cuadro_3 > 2000):
       print("\n---¡Error!, la fecha de los cuadros no debe exceder del año 2000---\n")

    elif(cuadro_3 < 1891):
        antiguedad_cuadro3 = True;
        total_antiguos += 1;


if (antiguedad_cuadro1 == False and antiguedad_cuadro2 == False and antiguedad_cuadro3 == False):
    print("Renovar stock.")

else:
    print(f"Total de cuadros con antiguedad inferior a 10 años anterios al siglo XX = {total_antiguos}");


    







