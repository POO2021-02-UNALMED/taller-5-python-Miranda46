
class Animal:
    totalAnimales=0
    
    def __init__(self, nombre, edad, habitat, genero):
        self.nombre=nombre
        self.edad=edad
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
        return self.habitat

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

if __name__=="__main__":
    an1 = Animal("Perro", 10, "casa", "m")
    ok = False
    if an1.getNombre() == "Perro" and an1.getEdad() == 10 and an1.getHabitat() == "casa" and an1.getGenero() == "m":
        ok=True
    print(an1.getNombre() == "Perro" , an1.getEdad() == 10 , an1.getHabitat(), an1.getGenero() == "m")
    a=Animal("s", 3, "d", "m")
    print(Animal.totalAnimales)