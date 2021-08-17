"""
Escriba una función que, dado un número máximo,
retorne una lista con todos los números desde 1 hasta
dicho número, que sean simultáneamente múltiplos
de 3 y de 5 (utilice la operación resto con el carácter %)
"""

entry = int(input('Insert a number: '))

def mult(max):
    result = []
    for i in range(1, max+1):
        if i % 3 == 0 and i % 5 == 0:
            result.append(i)
    return result

print(mult(max=entry))
