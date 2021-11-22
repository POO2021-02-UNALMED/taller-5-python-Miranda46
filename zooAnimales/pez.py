
from zooAnimales.animal import Animal

class Pez(Animal):
    cantidadPeces=0
    salmones=0
    bacalaos=0
    listado=[]
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        from zooAnimales.animal import Animal
        self.nombre=nombre
        self.edad=edad
        self.habitat=habitat
        self.genero=genero
        self.colorEscamas=colorEscamas
        self.cantidadAletas=cantidadAletas
    
        
        Pez.cantidadPeces+=1
        Animal.totalAnimales+=1

    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        Av=Pez(nombre, edad, "oceano", genero, "rojo", 6)
        cls.salmones+=1
        cls.listado.append(Av)

    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        Av=Pez(nombre, edad, "oceano", genero, "gris", 6)
        cls.bacalaos+=1
        cls.listado.append(Av)

    def getListado(self):
        return self.listado

    def getColorEscamas(self):
        return self.colorEscamas

 

    def getCantidadAletas(self):
        return self.cantidadAletas

    def movimiento(self):
        return "nadar"