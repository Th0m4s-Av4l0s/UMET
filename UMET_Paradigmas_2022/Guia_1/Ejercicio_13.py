
#Declaracion de variables
nombre = " ";
apellido = " ";
dominio = " ";
email = " ";


#Este while controla que el dominio sea correcto
while(email.endswith("@umet.edu.ar") != True):


    #Ingreso de caracteres para crear el email
    nombre = input("Ingresar un nombre: ");
    apellido = input("Ingresar un apellido: ");
    dominio = input("Ingresar dominio: ");

    #Aca suma los 3 datos ingresados
    email = nombre + apellido + dominio;


    #En caso de que el dominio sea incorrecto se repetira
    # el ingreso de datos, caso contrario el programa 
    # devuelve el email y termina.
    if(email.endswith("@umet.edu.ar") == False):
       
        print("\n===¡Error!: asegurarse de que el email contenga '@umet.com.ar'===\n")

    else:
        print(f"\nEmail creado exitosamente!: '{email}'");
        


    

