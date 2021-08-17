# Presentar las tablas de multiplicar con un ciclo for y un input del usuario
# Es decir, el usuario ingresa la tabla y el ciclo for me imprime los valores

mult = int(input('Type a number to show its multiplies: '))

for i in range(0,10):
    result = i * mult
    print(f'{i}x{mult} = {result}')