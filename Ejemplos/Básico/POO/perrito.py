class perrito:
    patas = 4
    dientes = True
    orejas = 2
    nariz = 1

    def saltar(self):
        print("Yuju!")

    def encriptar(self):


        return self.__nombre
    
    def rastrear(self):
        print("Encontré algo")

    @classmethod
    def ladrar(ladrar):
        print("Hola")

    @staticmethod
    def saluda(llamar, numeroTelefonico):
        print(llamar,numeroTelefonico)

    def __init__(self,nombreU,razaU,sexoU,tamanioU):
        self.__nombre = nombreU
        self.raza = razaU
        self.sexo = sexoU
        self.tamanio = tamanioU

print("Patas de cualquier perro:",perrito.patas)

perrito.ladrar()
perrito.ladrar()
perrito.ladrar()

chihuahua = perrito("Firulais","Chihuahua","Macho",30)
rottweiler = perrito("Cloe","Rottweiler","Hembra",100)

chihuahua.dimeNombre()
chihuahua.rastrear()
chihuahua.ladrar()

print("El chichuahua se llama: "+chihuahua.nombre)

#print("El número de patas en el chihuahua es: "+str(chihuahua.patas))
#print("El número de patas del Rott es: "+str(rottweiler.patas))
#print("El chichuahua se llama: "+chihuahua.nombre)
#print("El Rot se llama: "+rottweiler.nombre)


## chihuahua.comer()
## chihuahua.ladrar()

## rottweiler.comer()
##rottweiler.ladrar()
