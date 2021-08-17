# Crear un bucle que almacene en una variable la
# suma de todos los elementos numéricos de una
# lista, con excepción del último.

num = [1, 2, 3, 4, 5, 6]
res = 0  # Resultado.
for i, x in enumerate(num):
    # Evitar sumar el último número de la lista.
    if i == len(num) - 1:
        break
    res += x
print(res)