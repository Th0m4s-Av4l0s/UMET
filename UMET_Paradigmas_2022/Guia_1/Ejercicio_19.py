#Declaracion de variables
primera_formula = 0.0
segunda_formula = 0.0
tercera_formula = 0.0
control_votos = 100.0
formula_electa = 0
eleccion_final = 0


#Titulo
print("=========ELECCIONES=========\n");


#Este print permite controlar el porcentaje de votos a
# ingresar
print(f"Cantidad de personas aún sin votar: {control_votos}")


#Ingreso de datos 
primera_formula = float(input("\nIngresar porcentaje de votos (Primera formula): "));


#Control de datos
while(primera_formula < 0.0 or primera_formula > control_votos):

    print(f"\n---¡Error! cantidad de votos comprendida entre 0.0% a {control_votos}---");

    print(f"\nCantidad de personas aún sin votar: {control_votos}")

    primera_formula = float(input("Ingresar porcentaje de votos (Primera formula): "));

#Una vez ingresado el primer porcentaje de votos, este se
# le resta a la cantidad de personas aún sin votar. 
control_votos -= primera_formula;

if(primera_formula >= 45.0):
    formula_electa = 1;



#Aca ocurre el mismo caso que la primera formula
print(f"\nCantidad de personas aún sin votar: {control_votos}")

segunda_formula = float(input("\nIngresar porcentaje de votos (Segunda formula): "));

while(segunda_formula < 0.0 or segunda_formula > control_votos):

    print(f"\n---¡Error! cantidad de votos comprendida entre 0.0% a {control_votos}---");

    print(f"\nCantidad de personas aún sin votar: {control_votos}")

    segunda_formula = float(input("Ingresar porcentaje de votos (Segunda formula): "));

control_votos -= segunda_formula;

if(segunda_formula >= 45.0):
    formula_electa = 2;


#En caso de el control de votos restado por las formulas
# anteriores sea inferior a 40%, el resto se le dara a la
# tercera formula.
if(control_votos > 40.0):

    print(f"\nCantidad de personas aún sin votar: {control_votos}")

    tercera_formula = float(input("\nIngresar porcentaje de votos (Tercera formula): "));

    while(tercera_formula < 0.0 or tercera_formula > control_votos):

        print(f"\n---¡Error! cantidad de votos comprendida entre 0.0% a 100.0%---");

        print(f"\nCantidad de personas aún sin votar: {control_votos}")

        tercera_formula = float(input("\nIngresar porcentaje de votos (Tercera formula): "));

    control_votos -= tercera_formula;

    if(tercera_formula >= 45.0):
        formula_electa = 3;

else:
    tercera_formula = control_votos;



print(f"\nResultados: {primera_formula} | {segunda_formula} | {tercera_formula}");



#Dependiendo el valor de la variable 'formula_electa' la
# condicion imprime la formula electa
if(formula_electa == 1):

    print(f"La primera formula quedó electa con {primera_formula}% de los votos.");

elif(formula_electa == 2):

    print(f"La segunda formula quedó electa con {segunda_formula}% de los votos.");

elif(formula_electa == 3):

    print(f"La tercera formula quedó electa con {tercera_formula}% de los votos.");



#En caso de un empate de 2 formulas con 40.0% de votos, se
# realiza de nuevo una votacion para definir la formula
# electa
elif(primera_formula >= 40.0 and segunda_formula >= 40.0):


    control_votos = 100.0;

    print("\n--Empate entra la primera y segunda formula.--")

    eleccion_final = int(input("\n¿A quien votarás? \n1. Primera formula \n2. Segunda formula \nEleccion: "));



    while(eleccion_final < 1 or eleccion_final > 2):
        print("\n¡Error! Opcion no valida, comprendida en (1-2).")

        print("\n--Empate entra la primera y segunda formula.--")

        eleccion_final = int(input("\n¿A quien votarás? \n1. Primera formula \n2. Segunda formula \nEleccion: "));



    if(eleccion_final == 1):

        print(f"\nCantidad de personas aún sin votar (Segunda vuelta): {control_votos}")

        primera_formula = int(input("\nCantidad de votos?: "));

    elif(eleccion_final == 2):

        print(f"\nCantidad de personas aún sin votar (Segunda vuelta): {control_votos}")

        primera_formula = int(input("\nCantidad de votos?: "));

    
    if(primera_formula > segunda_formula):

        print("La primera formula quedó electa en la segunda vuelta");

    elif(segunda_formula > primera_formula):

        print("La segunda formula quedó electa en la segunda vuelta");

    else:
        
        print("Otro empate electoral.");



    

elif(primera_formula >= 40.0 and tercera_formula >= 40.0):

    control_votos = 100.0;

    print("\n--Empate entra la primera y tercera formula.--")

    eleccion_final = int(input("\n¿A quien votarás? \n1. Primera formula \n3. Tercera formula \nEleccion: "));



    while(eleccion_final < 1 or eleccion_final > 3 or eleccion_final == 2):
        print("\n¡Error! Opcion no valida, comprendida en (1 ó 3).")

        print("\n--Empate entra la primera y Tercera formula.--")

        eleccion_final = int(input("\n¿A quien votarás? \n1. Primera formula \n3. Tercera formula \nEleccion: "));



    if(eleccion_final == 1):

        print(f"\nCantidad de personas aún sin votar (Segunda vuelta): {control_votos}")

        primera_formula = int(input("\nCantidad de votos?: "));

    elif(eleccion_final == 3):

        print(f"\nCantidad de personas aún sin votar (Segunda vuelta): {control_votos}")

        tercera_formula = int(input("\nCantidad de votos?: "));

    
    if(primera_formula > tercera_formula):

        print("La primera formula quedó electa en la segunda vuelta");

    elif(tercera_formula > primera_formula):

        print("La segunda formula quedó electa en la segunda vuelta");

    else:
        
        print("Otro empate electoral.");



elif(segunda_formula >= 40.0 and tercera_formula >= 40.0):

    control_votos = 100.0;

    print("\n--Empate entra la segunda y tercera formula.--")

    eleccion_final = int(input("\n¿A quien votarás? \n2. Segunda formula \n3. Tercera formula \nEleccion: "));



    while(eleccion_final < 2 or eleccion_final > 3):
        print("\n¡Error! Opcion no valida, comprendida en (2-3).")

        print("\n--Empate entra la segunda y tercera formula.--")

        eleccion_final = int(input("\n¿A quien votarás? \n2. Segunda formula \n3. Tercera formula \nEleccion: "));



    if(eleccion_final == 2):

        print(f"\nCantidad de personas aún sin votar (Segunda vuelta): {control_votos}")

        segunda_formula = int(input("\nCantidad de votos?: "));

    elif(eleccion_final == 3):

        print(f"\nCantidad de personas aún sin votar (Segunda vuelta): {control_votos}")

        tercera_formula = int(input("\nCantidad de votos?: "));

    
    if(segunda_formula > tercera_formula):

        print(f"La Segunda formula quedó electa en la segunda vuelta con {segunda_formula} de los votos");

    elif(tercera_formula > segunda_formula):

        print(f"La tercera formula quedó electa en la segunda vuelta con {tercera_formula} de los votos");

    else:
        
        print("Otro empate electoral.");



    