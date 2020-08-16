import Vehiculo ##Nombre archivo

class trailer(Vehiculo.vehiculo):
    marca = "VW"


class coche(Vehiculo.vehiculo):
    marca = "VW"
    radio = False
    cantidad = 12

    def __init__(self,tapetes,numCristales):
        self.tapetes = tapetes
        self.numCristales = numCristales
    
    @staticmethod
    def disponibilidad():
        return coche.cantidad<10
    
    @classmethod
    def meterBocinas(numBocinas):
        if not coche.radio:
            return "No puedes meter bocinas"
        else:
            return "Que suene!"

jetta = coche(4,10)
nuevoTrailer = trailer("Rojo")

print(trailer.llantas)
print(coche.llantas)
