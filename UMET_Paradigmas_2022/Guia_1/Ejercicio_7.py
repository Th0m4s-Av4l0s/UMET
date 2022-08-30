a = 0
b = 0
c = b + a

while(c <= 21):
    if(c == 0):
        print(f"{a}", end = "-")
        b = 1

    a = b
    b = c
    c = a + b
    
    print(f"{c}", end = "-")

    if(c >= 21):
        break
    

