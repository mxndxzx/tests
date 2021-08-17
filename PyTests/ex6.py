# TP1 algoritmos UTN 2021
"""
Una empresa desea calcular el sueldo de un empleado e imprimir su recibo detallando: 
- Nombre y Apellido, Sueldo Básico, Premio, Comida, Viáticos, Ausentes, Obra social (3%), Ley 19032 (3%), y Jubilación (11%). 
- Por los ausentes, se descuenta un monto fijo por día de ausencia. Los porcentajes se calculan sobre los montos remunerativos.
Viáticos, premios y comida no se consideran remunerativos.
"""

employees = {
    1:{
        'name' : 'Maximo Cozetti',
        'salary' : 170000,
        'prize' : 30000,
        'food' : 10000,
        'travel' : 5000,
        'out' : 2,
    },
    2:{
        'name' : 'Emilio Ravenna',
        'salary' : 200000,
        'prize' : 10000,
        'food' : 15000,
        'travel' : 3000,
        'out' : 1,
    },
    3:{
        'name' : 'Mario Santos',
        'salary' : 270000,
        'prize' : 15000,
        'food' : 20000,
        'travel' : 8000,
        'out' : 3,
    },
    4:{
        'name' : 'Pablo Lampone',
        'salary' : 170000,
        'prize' : 20000,
        'food' : 7000,
        'travel' : 7000,
        'out' : 0,
    },
    5:{
        'name' : 'Gabriel Medina',
        'salary' : 180000,
        'prize' : 40000,
        'food' : 12000,
        'travel' : 5000,
        'out' : 1,
    }
}

out_fix = 1500 #Monto fijo por ausente

def total(salary, prize, food, travel, out, name): # Main function
    out_prize = out * out_fix
    health = (salary - out_fix) * 0.03
    law = (salary - out_fix) * 0.03
    retirement = (salary - out_fix) * 0.11
    total_sum = salary + prize - food - travel - out_prize - health - law - retirement
    print(f'Bienvenido {name}! Su recibo es:')
    print(f'- Sueldo base: {salary}\n- Premio mensual: {prize}\n- Catering: -{food}\n- Viáticos: -{travel}\n- Días ausente: {out}\n- Total ausentes: -{out_prize}')
    print(f'- Descuento por Obra Social: -{health}\n- Ley 19032: -{law}\n- Jubilación: -{retirement}')
    print(f'Su total es de ${total_sum}\n-------------------------------')
    

print("Bienvenido! Los empleados actuales son: ")

for x in employees:
    print(x,"=", employees[x]['name'])
print("0 = Salir")

search = int(input('Ingrese el número de empleado: '))

while search != 0:
    if search == 1:
        total(employees[1]['salary'], employees[1]['prize'], employees[1]['food'], employees[1]['travel'], employees[1]['out'], employees[1]['name'])
    elif search == 2:
        total(employees[2]['salary'], employees[2]['prize'], employees[2]['food'], employees[2]['travel'], employees[2]['out'], employees[2]['name'])
    elif search == 3:
        total(employees[3]['salary'], employees[3]['prize'], employees[3]['food'], employees[3]['travel'], employees[3]['out'], employees[3]['name'])
    elif search == 4:
        total(employees[4]['salary'], employees[4]['prize'], employees[4]['food'], employees[4]['travel'], employees[4]['out'], employees[4]['name'])
    elif search == 5:
        total(employees[5]['salary'], employees[5]['prize'], employees[5]['food'], employees[5]['travel'], employees[5]['out'], employees[5]['name'])
    else:
        print('Ingrese un número válido')   
    
    print("Bienvenido! Los empleados actuales son: ")

    for x in employees:
        print(x,"=", employees[x]['name'])
    print("0 = Salir")

    search = int(input('Ingrese el número de empleado: ')) #Se repite el input para que while no entre en bucle infinito
    
else:
    print('Gracias por utilizar nuestro sistema!') #Mensaje de salida