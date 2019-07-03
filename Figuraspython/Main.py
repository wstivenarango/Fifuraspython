import Figuras as f
import Punto as p

opc = input ("Seleccione la figura teniendo en cuenta el siguiente menu \n1.Cuadrado \n2.Triangulo  \n3.Rectangulo \n4.Circulo \n5.Elipse \n")
origen = p.Punto()
fin = p.Punto()

def mostrar (fig, origen, fin):
    fig.setOrigen(origen);
    fig.setFin(fin);
    fig.calcularArea();
    fig.calcularPerimetro();
    print "El area de la figura es: " , fig.getArea()
    print "El perimetro de la figura es: =" , fig.getPerimetro()

if opc == 1:
    fig = f.Cuadrado()
    origen.setX(0)
    origen.setY(0)
    fin.setX(5)
    fin.setY(0)
    mostrar (fig, origen, fin)
elif opc == 2:
    fig = f.Triangulo()
    origen.setX(0)
    origen.setY(5)
    fin.setX(10)
    fin.setY(0)
    mostrar (fig, origen, fin)
elif opc == 3:
    fig = f.Rectangulo()
    origen.setX(0)
    origen.setY(5)
    fin.setX(10)
    fin.setY(0)
    mostrar (fig, origen, fin)
elif opc == 4:
    fig = f.Circulo()
    origen.setX(5)
    origen.setY(0)
    mostrar (fig, origen, fin)
elif opc == 5:
    fig = f.Elipse()
    origen.setX(0)
    origen.setY(5)
    fin.setX(10)
    fin.setY(0)
    mostrar (fig, origen, fin)
