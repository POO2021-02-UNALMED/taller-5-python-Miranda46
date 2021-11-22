class Zoologico:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion=ubicacion
        self.zonas=[]

    def cantidadTotalAnimales(self):
        cont=0
        for i in range(len(self.zonas)):
            cont+=self.zonas[i].cantidadAnimales()
        return cont


    def agregarAnimales(self, animal):
        self.animales.append(animal)

    def getNombre(self):
        return self.nombre

    def setNombre(self,nombre):
        self.nombre=nombre

    def getZona(self):
        return self.zonas

    def agregarZonas(self,zona):
        self.zonas.append(zona)

