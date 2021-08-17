# Crear un bucle que almacene en una variable la
# suma de todos los elementos numéricos de una
# lista, con excepción del último.

values = [1,2,3,4,5,6,7,8,9,10] # Var de entrada
result = 0 # Cero de la suma, por donde comienza

for i in values: # Main loop
    

result = None # Var de salida
print(result)
# ------- PRE ------- 



numeros = [1, 2, 3, 4, 5, 6]
res = 0  # Resultado.
for i, carlos in enumerate(numeros):
    # Evitar sumar el último número de la lista.
    if i == len(numeros) - 1:
        break
    res += carlos
print(res)