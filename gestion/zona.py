class Zona():
    def __init__(self, nombre, zoo):
        self.nombre = nombre
        self.zoo=zoo
        self.animales=[]

    def getAnimales(self):
        return self.animales

    def agregarAnimales(self, animal):
        self.animales.append(animal)

    def getNombre(self):
        return self.nombre

    def setNombre(self,nombre):
        self.nombre=nombre

    def getZoo(self):
        return self.zoo

    def cantidadAnimales(self):
        return len(self.animales)
