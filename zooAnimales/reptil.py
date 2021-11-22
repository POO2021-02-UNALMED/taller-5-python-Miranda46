from zooAnimales.animal import Animal


class Reptil:
    cantidadReptiles=0
    iguanas=0
    serpientes=0
    listado=[]
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        self.nombre=nombre
        self.edad=edad
        self.habitat=habitat
        self.genero=genero
        self.colorEscamas=colorEscamas
        self.largoCola=largoCola
    
        
        Reptil.cantidadReptiles+=1
        Animal.totalAnimales+=1

    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        Av=Reptil(nombre, edad, "humedal", genero, "verde", 3)
        cls.iguanas+=1
        cls.listado.append(Av)

    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        Av=Reptil(nombre, edad, "jungla", genero, "blanco", 1)
        cls.serpientes+=1
        cls.listado.append(Av)

    def getListado(self):
        return self.listado

    def getcolorEscamas(self):
        return self.colorEscamas

    @staticmethod
    def cantidadPeces(cls):
        return cls.cantidadPeces

    def getLargoCola(self):
        return self.largoCola

    def movimiento(self):
        return "reptar"