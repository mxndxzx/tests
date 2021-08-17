# Utilizando un bucle “while”, elaborar un código
# que imprima en pantalla cada uno de los
# elementos de una lista y simultáneamente los
# elimine, hasta quedar vacía.


lista = [1,2,3,4,5,6,7,8,9,10]

while len(lista) > 0:
    print(lista[0])
    del lista[0] # Delete
    