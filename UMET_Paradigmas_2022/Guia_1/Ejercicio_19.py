#Declaracion de variables
primera_formula = 0.0
segunda_formula = 0.0
tercera_formula = 0.0
control_votos = 100.0
formula_electa = 0


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



print(f"{primera_formula} | {segunda_formula} | {tercera_formula}");

if(formula_electa == 1):

    print(f"La primera formula quedó electa con {primera_formula}% de los votos.");

elif(formula_electa == 2):

    print(f"La segunda formula quedó electa con {segunda_formula}% de los votos.");

elif(formula_electa == 3):

    print(f"La tercera formula quedó electa con {tercera_formula}% de los votos.");

elif(primera_formula and segunda_formula >= 40.0):

    control_votos = 100.0;

elif(primera_formula and tercera_formula >= 40.0):

    control_votos = 100.0;

elif(segunda_formula and tercera_formula >= 40.0):

    control_votos = 100.0;


    