#" (, end=' ') " -> evita el salto de linea
#de los print() o agrega caracteres en el " "
# pero evitando de todas formas el salto 
# de linea
#EJ: 

print("Esto es", end = " un ")
print("ejemplo")

#" (, sep = ' ') " -> agrega lo que el usuario
#desee a esos espacios automaticos que agrega
#python cuando se usa un print() con
# CARACTERES y con comas.
#print("1","2","3","4","5") -> 1 2 3 4 5
#EJ:

print("1","2","3","4","5", sep = "-");
