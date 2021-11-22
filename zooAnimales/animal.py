
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

    @classmethod
    def totalPorTipo(cls):
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.reptil import Reptil
        from zooAnimales.ave import Ave
        from zooAnimales.pez import Pez
        a=str("Mamiferos : " + str(Mamifero.cantidadMamiferos) + "\nAves : " + str(Ave.cantidadAves) + "\nReptiles : "+ str(Reptil.cantidadReptiles) + "\nPeces : " + str(Pez.cantidadPeces) +"\nAnfibios : " + str(Anfibio.cantidadAnfibios))
        return a

    def toString(self):
	    if (self.zona !=None) :

		        return "Mi nombre es "+str(self.nombre)+ ", tengo una edad de " + str(self.edad)+", habito en "+str(self.habitat)+ " y mi genero es "+str(self.genero)+"la zona en la que me ubico es "+str(self.zona)+", en el "+str(self.zona.getZoo())
	    else:
                return "Mi nombre es "+str(self.nombre)+ ", tengo una edad de " + str(self.edad)+", habito en "+str(self.habitat)+ " y mi genero es "+str(self.genero)
					

if __name__=="__main__":
    Anfibio.crearRana("test", 11, "M")
    Anfibio.crearSalamandra("test", 11, "M")
    Mamifero.crearCaballo("test", 11, "M")
    Mamifero.crearCaballo("test", 11, "M")
    Mamifero.crearLeon("test", 11, "M")
    Reptil.crearIguana("test", 11, "M")
    Pez.crearSalmon("test", 11, "M")
    Ave.crearHalcon("test", 11, "M")
    Ave.crearHalcon("test", 11, "M")
    ok = False
    comp = "Mamiferos : 3\nAves : 2\nReptiles : 1\nPeces : 1\nAnfibios : 2"
    print(comp.replace('\n', ''))
    print(Animal.totalPorTipo().replace('\n', ''))
    if Animal.totalPorTipo().replace('\n', '') == comp.replace('\n', ''):
        ok = True
  