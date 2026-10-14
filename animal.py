
class Animal: 
    def __init__(self, param_nombre, param_especie, param_edad):
        self.nombre = param_nombre
        self.especie = param_especie
        self.edad = param_edad
        self.energia = 50


    def presentarse (self):
       print (f"Hola, soy{self.nombre}. Especie: {self.especie}. Edad {self.edad} años")

    def jugar(self):
        pass
    def comer (self):
        pass
    def dormir (self):
        pass

mascota1 = Animal("Jorge", "Golden", 3)

mascota1.presentarse()

