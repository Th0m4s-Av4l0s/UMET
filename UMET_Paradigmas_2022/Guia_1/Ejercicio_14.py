#Mismo ejercicio que el "Ejercicio_15.py"
num_1 = 0
num_2 = 0
num_3 = 0
resultado = 0

num_1 = int(input(">Ingresar primer numero a sumar: "));
num_2 = int(input(">Ingresar segundo numero a sumar: "));
num_3 = int(input(">Ingresar tercer numero a sumar: "));

resultado = num_1 + num_2 + num_3;
print(f"\n///El resultado de la suma es = {resultado}///");

if(resultado > 10):
    print("\nEl resultado es mayor a 10, debe dividirse por 2.");
    print(f"{resultado} // 2 = {resultado // 2}");

elif(resultado < 10):
    print("El resultado es menor a 10, debe potenciarse al cubo.");
    print(f"{resultado} ** 3 = {resultado ** 3}")