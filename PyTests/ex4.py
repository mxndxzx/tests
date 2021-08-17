"""
Sucesión de Fibonacci: Cree una función que tome como argumento un entero que indique la cantidad de términos
y retorne una lista de una sucesión de Fibonacci. Por ejemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, etc.
"""
entry = int(input('Insert a number: '))

def fib():
    if entry > 2:
        start = [0, 1]
        for i in range(2, entry): # 2 porque la lista ya tiene 2 elementos predefinidos
            start.append(start[-1] + start[-2]) # A la lista start le agrego un elemento al final. Que elemento le agrego? la suma entre el ultimo y el anteúltimo elemento de dicha lista start
        print(f'Fibonacci sequence is {start}')
    elif entry <= 2:
        print('Number must be higher than 2!')
fib()



