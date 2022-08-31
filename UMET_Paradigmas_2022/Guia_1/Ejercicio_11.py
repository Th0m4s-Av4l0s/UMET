from unicodedata import decimal


mes = int
cantidad_ahorro = decimal
porcentaje = decimal
cantidad_restada = decimal


mes = int(input("En que mes estamos?: "))

while(mes < 1 and mes > 12):
    print("\n---Error: Elegir mes por numero (1-12)---");
    mes = int(input("En que mes estamos?: "))

cantidad_ahorro = float(input("Cantidad de pesos a ahorrar: "));

for mes in range(mes,12):

    porcentaje += cantidad_ahorro - (cantidad_ahorro * 0.10)
    
print(f"{porcentaje}")
print(f"Cantidad de ahorro para diciembre: {cantidad_ahorro}")
print(f"Cantidades mensuales restadas: {cantidad_restada}")
