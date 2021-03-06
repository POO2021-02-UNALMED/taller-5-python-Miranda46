
from zooAnimales.animal import Animal

class Anfibio(Animal):
    cantidadAnfibios=0
    ranas=0
    salamandras=0
    listado=[]
    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        from zooAnimales.animal import Animal
        self.nombre=nombre
        self.edad=edad
        self.habitat=habitat
        self.genero=genero
        self.colorPiel=colorPiel
        self.venenoso=venenoso
        
        Anfibio.cantidadAnfibios+=1
        Animal.totalAnimales+=1

    @classmethod
    def crearRana(cls, nombre, edad, genero):
        Av=Anfibio(nombre, edad, "selva", genero, "rojo", True)
        Anfibio.ranas+=1
        Anfibio.listado.append(Av)

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        Av=Anfibio(nombre, edad, "selva", genero, "negro y amarillo", True)
        Anfibio.salamandras+=1
        Anfibio.listado.append(Av)

    def getListado(self):
        return self.listado

    def isVenenoso(self):
        return self.venenoso

    def getColorPiel(self):
        return self.colorPiel

    def movimiento():
        return "saltar"
