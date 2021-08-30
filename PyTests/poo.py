"""
------- Programación orientada a objetos en Python -------

Hay 3 elementos fundamentales:
- Clases: La estructura del objeto, el molde
- Atributos: Las caracteristicas de ese molde (por ej, en una planilla de usuarios, sería el nombre, ID, sexo, etc.)
- Métodos: Las funciones que ese objeto puede realizar (saludar, buscar, apagar, correr, siempre acciones declaradas con funciones)
- Builder: Función constructora __init()__ para inicializar la clase. Se le pasa self y tantos parámetros como valores de atributos necesite
- Inherit: Una clase puede heredar atributos de otra, basta con pasarle ese parámetro
- Callback: Llamar a la clase, darle atributos y llamar sus métodos. OJO en los métodos siempre usar return, sino aparece un 'none' que es re molesto
- Self: Atributo que indica que los parámetros a utilizar son los atributos de la clase. Por esto es que los métodos se escriben dentro de la propia clase
"""

class user: # Clase como tal
    name = "" # Atributos
    surname = ""
    artist_name = ""
    job = ""
    dni = ""
    user_id = ""

    # Builder
    # def __init__(self, name, surname, artist_name, job):
    #    self.name = name
    #    self.surname = surname
    #    self.artist_name = artist_name
    #    self.job = job

    # Método
    def say_hi(self): # Ese self le dice a la función que tome como parámetros los atributos de la clase. Por eso los métodos se colocan dentro de la misma clase.
        say = f"Hi, my name is {self.name} {self.surname} and I'm a {self.job}"
        return say # Uso return en vez de print porque sino la función me devuelve el print y un none abajo, bastante molesto

class best_albums(user): # Inherit, herencia de la clase 'user' (todo, atributos, builder y métodos)
    top1 = ""
    top2 = ""
    top3 = ""
    top4 = ""
    top5 = ""
    
    def __init__(self, name, surname, artist_name, job, t1, t2, t3, t4 ,t5): # Builder para las dos clases (user es la main y best_albums la child)
        self.name = name
        self.surname = surname
        self.artist_name = artist_name
        self.job = job
        self.top1 = t1
        self.top2 = t2
        self.top3 = t3
        self.top4 = t4
        self.top5 = t5

    def legend(self):
        text = f"--- Artist Info ---\nName: {self.name} {self.surname}\nArtist Name: {self.artist_name}\nTop 5 Best Albums:\n1 - {self.top1}\n2 - {self.top2}\n3 - {self.top3}\n4 - {self.top4}\n5 - {self.top5}"
        return text

# Callback
# pappo = user("Norberto Aníbal","Napolitano", "Pappo", "guitarrist and singer") # Le paso los 4 parámetros del builder (name, surname, artist_name y job)
# pappo_legend = best_albums("Norberto Aníbal","Napolitano", "Pappo", "guitarrist and singer", input('Write your top 1 album: '), input('Write your top 2 album: '), input('Write your top 3 album: '), input('Write your top 4 album: '), input('Write your top 5 album: '))
pappo_legend = best_albums("Norberto Aníbal","Napolitano", "Pappo", "guitarrist and singer", "Volumen 3", "Volumen 5", "Volumen 2", "Aeroblus", "Volumen 1")

# print(pappo.say_hi())
print(pappo_legend.legend())
