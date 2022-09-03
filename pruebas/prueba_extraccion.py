#Dentro una cadena, este metodo saca una porcion dentro 
#de la misma, a diferencia del metodo find este saca strings

mensaje = "Que onda"

#Si se imprime de 0:2 solo sera "Qu" en lugar de "Que"
#Se debe siempre sumar 1 al max [0: 2<-(+1)]
extraer_subcadena = mensaje[0:3]

print(extraer_subcadena)