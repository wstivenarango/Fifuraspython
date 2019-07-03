import math

class Punto:
    def __init__ (self):
        self.x = 0
        self.y = 0

    def getX (self):
        return self.x

    def getY (self):
        return self.y

    def setX (self, valor):
        self.x = valor

    def setY (self, valor):
        self.y = valor

    def calcularDistancia (self, a):
        distancia = 0
        distancia = math.sqrt((self.x-a.x)**2+(self.y-a.y)**2)
        return distancia
