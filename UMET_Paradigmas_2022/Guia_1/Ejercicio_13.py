from tokenize import String


nombre = String
apellido = String
dominio = String
email = String

while(email.endswith("@umet.edu.ar") != True):

    nombre = input("Ingresar un nombre: ");
    apellido = input("Ingresar un apellido: ");
    dominio = input("Ingresar dominio: ");
    email = nombre + apellido + dominio;

    if(email.endswith("@umet.edu.ar") == False):
       
        print("\n===¡Error!: asegurarse de que el email contenga '@umet.com.ar'===\n")

    else:
        print(f"\nEmail creado exitosamente!: '{email}'");
        


    

