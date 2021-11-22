
class Animal:
    totalAnimales=0
    
    def __init__(self, nombre, eadad, habitat, genero):
        self.nombre=nombre
        self.edad=eadad
        self.habitat=habitat
        self.genero=genero
        zona=None
  
        Animal.totalAnimales+=1
    @classmethod
    def getTotalAnimales(cls):
        return cls.totalAnimales

    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def getHabitat(self):
        self.habitat

    def getGenero(self):
        return self.genero

    def getZona(self):
        return self.zona

    def setZona(self, zona):
        self.zona=zona

    def movimiento(self):
        return "desplazarse"

    def totalPorTipo(self):
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.reptil import Reptil
        from zooAnimales.ave import Ave
        from zooAnimales.pez import Pez
        a="Mamiferos: " + Mamifero.cantidadMamiferos() + "\nAves: " + Ave.cantidadAves() + "\nReptiles: "+ Reptil.cantidadReptiles() + "\nPeces: " + Pez.cantidadPeces() +"\nAnfibios: " + Anfibio.cantidadAnfibios()
        return a