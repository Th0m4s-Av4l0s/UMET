pies = 0.0
pulgadas = 0.0
centimetros = 0.0
eleccion = 0
conversor = 0.0

while(eleccion < 1 or  eleccion > 3):
    print("=====Conversor de distancias=====\n")
    print("1. Pies \n2. Pulgadas \n3. Centimetros \n")
    eleccion = int(input(">Elegir distancia a convertir: "));


    if(eleccion < 1 or eleccion > 3):
        print("\n---¡Error!: Opcion no valida (1-3)---\n");

    elif(eleccion == 1):

        pies = float(input("\n>Ingresar cantidad de pies: "));

        while(eleccion < 2 or eleccion > 3):

            print("\n2. Pulgadas \n3. Centimetros");
            eleccion = int(input(">Convertir " + str(pies) + " pies a: "));


            if(eleccion < 2 or conversor > 3):
                print("\n---¡Error!: Opcion no valida (2 ó 3)---\n ");
            
            elif(eleccion == 2):
                print(f"{pies} pies a pulgadas = {12 * pies} pulgadas");

            elif(eleccion == 3):
                print(f"{pies} pies a centimetros = {30.48 * pies} cm");
       
    elif(eleccion == 2):

        pulgadas = float(input("\n>Ingresar cantidad de pulgadas: "));

        while(eleccion < 1 or eleccion > 3 or eleccion == 2):

            print("\n1. Pies \n3. Centimetros");
            eleccion = int(input(">Convertir " + str(pulgadas) + " pulgadas a: "));

            if(eleccion < 1 or eleccion > 3 or eleccion == 2):
                print("\n---¡Error!: Opcion no valida (1 ó 3)---\n ");
            
            elif(eleccion == 1):
                print(f"{pulgadas} pulgadas a pies = {pulgadas / 12} pies");

            elif(eleccion == 3):
                print(f"{pulgadas} pulgadas a centimetros = {pulgadas * 2.54} cm");
        
    elif(eleccion == 3):

        centimetros = float(input("\n>Ingresar cantidad de centimetros: "));

        while(eleccion < 1 or eleccion > 2):

            print("\n1. Pies \n2. Pulgadas");
            eleccion = int(input(">Convertir " + str(pulgadas) + " pulgadas a: "));

            if(eleccion < 1 or eleccion > 2):
                print("\n---¡Error!: Opcion no valida (1 ó 2)---\n ");
            
            elif(eleccion == 1):
                print(f"{centimetros} centimetros a pies = {centimetros / 30.48} pies");

            elif(eleccion == 2):
                print(f"{centimetros} centimetros a pulgadas = {centimetros / 2.54} pulgadas"); 
                
            
        
            


            



            

        

    






