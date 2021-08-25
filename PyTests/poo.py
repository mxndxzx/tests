"""
------- Programación orientada a objetos en Python -------

Hay 3 elementos fundamentales:
- Clases: La estructura del objeto, el molde
- Atributos: Las caracteristicas de ese molde (por ej, en una planilla de usuarios, sería el nombre, ID, sexo, etc.)
- Métodos: Las funciones que ese objeto puede realizar (saludar, buscar, apagar, correr, siempre acciones declaradas con funciones)
- Builder: Función constructora __init()__ para inicializar la clase. Se le pasa self y tantos parámetros como valores de atributos necesite
- 
"""

class user:
    name = ""
    surname = ""
    job = ""
    dni = ""
    user_id = ""

    # Builder
    def __init__(self, name, surname, job):
        self.name = name
        self.surname = surname
        self.job = job

    # Método play
    def say_hi(self): # Ese self le dice a la función que tome como parámetros los atributos de la clase. Por eso los métodos se colocan dentro de la misma clase.
        say = f"Hi, my name is {self.name} {self.surname} and I'm a {self.job}"
        return say # Uso return en vez de print porque sino la función me devuelve el print y un none abajo, bastante molesto

# Callback
pappo = user("Norberto Aníbal","Napolitano","guitarrist and singer") # Le paso los 3 parámetros del builder (name, surname y job)
print(pappo.say_hi())
