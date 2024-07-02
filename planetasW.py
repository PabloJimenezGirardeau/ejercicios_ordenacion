
class Planeta():
    def __init__(self, nombre, volumen, clasificacion):
        self.nombre = nombre
        self.volumen = volumen
        self.clasificacion = clasificacion

class Concordia(Planeta):
    def __init__(self):
        super().__init__("Concordia", 500, 1)

class Ilum(Planeta):
    def __init__(self):
        super().__init__("Ilum", 1200, 2)

class Kamino(Planeta):
    def __init__(self):
        super().__init__("Kamino", 800, 3)
       
Concordia = Concordia()
Ilum = Ilum()
Kamino = Kamino()