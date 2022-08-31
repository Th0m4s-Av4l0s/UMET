#Los operadores relacionales sirven para
#comparar entre valores mayormente 
# util en numericos


num1 = 4
num2 = 7
num3 = 5
num4 = 4
num5 = 6
num6 = 9

menor_que = bool
mayor_que = bool
igual_que = bool
diferente_que = bool
menorigual_que = bool
mayorigual_que = bool


#Menor que
menor_que = num1 < 5

if(menor_que == True):
    print(str(num1) + " es menor a " + str(5))

mayor_que = num2 > 5

if(mayor_que == True):
    print(str(num2) + " es mayor que " + str(5))

igual_que = (num3 == 5)

if(igual_que == True):
    print(str(num3) + " es igual que " + str(5))

diferente_que = (num4 != 5)

if(diferente_que == True):
    print(str(num4) + " es diferente que " + str(5))

#Aca aprovecho a ver operadores logicos AND
menorigual_que = (num5 <= 6 and num5 <= 5)

if(menorigual_que == True):
    print(str(num5) + " es menor o igual que " + str(6) + " o " + str(5))


mayorigual_que = (num6 <= 9 and num6 <= 10)

if(mayorigual_que == True):
    print(str(num6) + " es mayor o igual que " + str(9) + " o " + str(10))
    
