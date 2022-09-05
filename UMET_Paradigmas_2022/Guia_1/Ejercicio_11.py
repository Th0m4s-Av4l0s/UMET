
#Declaracion de variables
mes = 0
x = 0
cantidad_ahorro = 0.0
cantidad_restada = 0.0
porcentaje = 0.0
total_ahorrado = 0.0


#Entrada de mes
mes = int(input("En que mes estamos?: "))


#Control de datos
while(mes < 1 and mes > 12):
    print("\n---Error: Elegir mes comprendido entre (1-12)---");
    mes = int(input("En que mes estamos?: "))


#Entrada de los ahorros mensuales
cantidad_ahorro = float(input("Cantidad de pesos a ahorrar mensualmente: "));


#Este for sirve para que desde el mes introducido hasta el mes 12, 'total_ahorrado' se concatene periodicamente
# con cantidad de ahorro - 10%, este porcentaje restado tambien se mostrará al finalizar el programa.
for x in range(mes,12):

    cantidad_restada += ((cantidad_ahorro * 10) / 100)

    total_ahorrado += cantidad_ahorro - ((cantidad_ahorro * 10) / 100);



#Salida de datos
print(f"Cantidad de ahorro para diciembre: {total_ahorrado}$ (Cantidad restada desde mes ({mes}) hasta mes (12): -{cantidad_restada}$)");


