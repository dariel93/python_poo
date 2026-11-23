class Rectangulo:
    alto=0
    ancho=0
    
    def __init__(self,a ,b):
        self.alto = a
        self.ancho = b
    
    def area(self):
        return self.alto * self.ancho
    def perimetro(self):
        return 2*(self.ancho+self.alto)
    def aumentar(self, valor):
        self.alto+= valor
        self.ancho+=valor
        
# ejemplo de uso

r1 = Rectangulo()
r2 = Rectangulo()
r1.alto=5
r1.ancho=10
r2.alto=6
r2.alto=3
print(f"Area del primer rectangulo {r1.area()}")
print(f"Perimetro del segundo rectangulo {r2.perimetro()}")

# A raiz del init

r1 = Rectangulo(3,9)
r2 = Rectangulo(7,2)