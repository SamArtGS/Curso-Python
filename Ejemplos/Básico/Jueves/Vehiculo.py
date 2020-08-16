class vehiculo:
    llantas = 4
    puertas = 4

    def __init__(self,color):
        self.color = color

    def desplazarse(self):
        print("Se está desplazando")

tracktor = vehiculo("Rojo")
tracktor.desplazarse()