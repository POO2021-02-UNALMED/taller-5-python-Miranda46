from zooAnimales.animal import Animal


class Mamifero:
    cantidadMamiferos=0
    caballos=0
    leones=0
    listado=[]
    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        self.nombre=nombre
        self.edad=edad
        self.habitat=habitat
        self.genero=genero
        self.pelaje=pelaje
        self.patas=patas
    
        
        Mamifero.cantidadMamiferos+=1
        Animal.totalAnimales+=1

    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        Av=Mamifero(nombre, edad, "pradera", genero, True, 4)
        cls.caballos+=1
        cls.listado.append(Av)

    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        Av=Mamifero(nombre, edad, "selva", genero, True, 4)
        cls.leones+=1
        cls.listado.append(Av)

    def getListado(self):
        return self.listado

    def getPatas(self):
        return self.patas

    @staticmethod
    def cantidadMamifero(cls):
        return cls.cantidadMamiferos

    def isPelaje(self):
        return self.pelaje