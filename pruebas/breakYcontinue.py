# El comando break rompe con cualquier ciclo
# de python (while, while do y for)

print("While con comando break \n");

contador = 0

while (contador <= 5):
    contador += 1

    print(contador);

    if contador == 3:
        print("Break!")
        break
        
print("Valor actual del contador: " + str(contador));


#el comando continue sirve para que cualquier
# ciclo (while, do while, for) se detenga  
# momentaneamente para luego proseguir
# con el ciclo que se esta realizado
#EJ:

print("\nWhile con comando continue \n")
contador = 0

while(contador <= 5):

    print(contador);
    contador += 1

    if(contador == 4):
        print("Stop! contador = 4");
        continue
        
