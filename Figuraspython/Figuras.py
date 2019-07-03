import Punto as p
import math
class Figura:

    def __init__ (self):
        self.origen = p.Punto()
        self.fin = p.Punto()
        self.area = 0
        self.perimetro = 0

    def getOrigen(self):
        return self.origen

    def setOrigen(self, valor):
        self.origen = valor

    def getFin(self):
        return self.fin

    def setFin(self, valor):
        self.fin = valor

    def getArea (self):
        return self.area

    def setArea (self, valor):
        self.area = valor

    def getPerimetro (self):
        return self.perimetro
    
    def setPerimetro (self, valor):
        self.perimetro = valor

    def calcularArea(self):
        pass

    def calcularPerimetro(self):
        pass 

class Cuadrado (Figura):

    def calcularArea(self):
        lado = self.origen.calcularDistancia(self.fin)
        self.area = lado*lado

    def calcularPerimetro(self):
        lado = self.origen.calcularDistancia(self.fin)
        self.perimetro = lado*4

class Triangulo (Figura):
    
    def calcularArea(self):

        temp = p.Punto()
        temp.setX(self.origen.getX())
        temp.setY(self.fin.getY())
        base = temp.calcularDistancia(self.fin)
        print base
        altura = self.origen.calcularDistancia(temp)
        print altura
        self.area = (base * altura)/2

    def calcularPerimetro(self):

        temp = p.Punto()
        temp.setX(self.origen.getX())
        temp.setY(self.fin.getY())
        base = temp.calcularDistancia(self.fin)
        altura = self.origen.calcularDistancia(temp)
        h = self.origen.calcularDistancia(self.fin)
        self.perimetro = base+altura+h

class Rectangulo(Figura):
    
    def calcularArea(self):

        temp = p.Punto()
        temp.setX(self.origen.getX())
        temp.setY(self.fin.getY())
        base = temp.calcularDistancia(self.fin)
        altura = self.origen.calcularDistancia(temp)
        self.area = base * altura

    def calcularPerimetro(self):

        temp = p.Punto()
        temp.setX(self.origen.getX())
        temp.setY(self.fin.getY())
        base = temp.calcularDistancia(self.fin)
        altura = self.origen.calcularDistancia(temp)
        self.perimetro = (base+altura)*2

class Circulo (Figura):

    def calcularArea(self):

        radio = self.origen.calcularDistancia(self.fin)
        self.area = math.pi * (radio **2)

    def calcularPerimetro(self):
        
	radio = self.origen.calcularDistancia(self.fin)
	self.perimetro = 2*(math.pi*radio)

class Elipse (Figura):

    def calcularArea(self):

        temp = p.Punto()
        temp.setX(self.origen.getX())
        temp.setY(self.fin.getY())
        a = temp.calcularDistancia(self.fin);
        b = self.origen.calcularDistancia(temp);
        self.area = math.pi * a * b ;
        
    def calcularPerimetro(self):

        temp = p.Punto()
        temp.setX(self.origen.getX())
        temp.setY(self.fin.getY())
        a = temp.calcularDistancia(self.fin)
        b = self.origen.calcularDistancia(temp)
        self.perimetro = (2* math.pi)* (math.sqrt (((a**2)+(b**2))/2))

        
