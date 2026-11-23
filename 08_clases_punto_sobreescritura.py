class Punto:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def dibujar(self):
        print(f"x: {self.x}, y:{self.y}", end="")
        

class Punto3D(Punto):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z=z
        
    def dibujar(self):
        print(f"z: {self.z}")

