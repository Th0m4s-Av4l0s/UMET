#Declaracion de variables
codigo = 0
cantidad_horas = 0


#Menu y entrada de dato
print("=======JORNADAS DE TRABAJO=======\n1. Turno diurno (Salario: 35.50$) \n2.Turno nocturno (Salario: 40.60$)\n");
codigo = int(input("En que turno trabajó el operario?: "))


#Control de datos
while(codigo < 1 or codigo > 2):

    print("\n¡Error!, Valor introducido no valido\n");

    print("=======JORNADAS DE TRABAJO=======\n1. Turno diurno (Salario: 35.50$) \n2. Turno nocturno (Salario: 40.60$)\n");

    codigo = int(input("En que turno trabajó el operario?: "))


#Condicional de la varibale 'codigo'
if(codigo == 1):

    cantidad_horas = int(input("Cantidad de horas trabajadas? (Turno diurno): "));

    #Contol de datos
    while(cantidad_horas < 0):

        print("\n¡Error! solo valores positivos\n")

        cantidad_horas = int(input("Cantidad de horas trabajadas? (Turno diurno): "));


    #Imprime la conversion horas * salario
    print(f"Total a pagar: {round(cantidad_horas * 35.50,2)}$")


#Mismo caso que la primera condición
elif(codigo == 2):

    cantidad_horas = int(input("Cantidad de horas trabajadas? (Turno nocturno): "));

    while(cantidad_horas < 0):

        print("\n¡Error! solo valores positivos\n")

        cantidad_horas = int(input("Cantidad de horas trabajadas? (Turno nocturno): "));

    print(f"Total a pagar: {round(cantidad_horas * 40.60,2)}$")








    