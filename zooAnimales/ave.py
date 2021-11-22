

from zooAnimales.animal import Animal


class Ave(Animal):
    cantidadAves=0
    halcones=0
    aguilas=0
    listado=[]
    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        from zooAnimales.animal import Animal
        self.nombre=nombre
        self.edad=edad
        self.habitat=habitat
        self.genero=genero
        self.colorPlumas=colorPlumas
        self.zona=None
    
        
        Ave.cantidadAves+=1
        Animal.totalAnimales+=1

    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        Av=Ave(nombre, edad, "montanas", genero, "cafe glorioso")
        cls.halcones+=1
        cls.listado.append(Av)

    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        Av=Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
        cls.aguilas+=1
        cls.listado.append(Av)

    def getListado(self):
        return self.listado

    def getColorPlumas(self):
        return self.colorPlumas

    def movimiento():
        return "volar"