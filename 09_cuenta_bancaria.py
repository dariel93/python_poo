# Crear la clase cuenta limitada , que sera una subclase de cuenta y tendra un atributo con la cantidad maxima a extraer. 
# Si el valor del atributo es 0, no hay limite. Si es > 0 sera el limite, y no se podra extraer mas dinero el que marque el limite


class Cuenta:
    def __init__(self, saldo):
        self.saldo = saldo
        
    def ingresar(self, cantidad):
        self.saldo += cantidad
    def extraer(self, cantidad):
        self.saldo = cantidad
    

class Cuenta_Limitada(Cuenta):
    
    def __init__(self, saldo, limite):
        super().__init__(saldo)
        self.limite = limite
    
    def extraer(self, cantidad):
        if self.limite > 0 and cantidad > self.limite:
            super().extraer(self.limite)
        else:
            super().extraer(cantidad)

"""c1=Cuenta_Limitada(200,50)
c1.extraer(20)
print(c1.saldo)
c1.extraer(100)
print(c1.saldo)"""

#Crear una nueva clase, que herede CuentaLimitada, llamada CuentaMovimientos
#Cada vez que se ingrese o extraiga, se deberá registrar dicho movimiento. Un movimiento
#tiene dos propiedades: cantidad y tipo (ingreso o extraccion). La nueva clase clase
#tendrá un método que devuelve la lista de los cinco últimos movimientos

class Movimiento:
    
    def __init__(self, cantidad, tipo):
        self.cantidad = cantidad
        self.tipo = tipo
        
    def __str__(self):
        return f"Tipo: {self.tipo}, Cantidad: {self.cantidad}"
        
        
class Cuenta_Movimientos(Cuenta_Limitada):
    
    def __init__(self, saldo, limite):
        super().__init__(saldo, limite)
        self.movimientos = []
    
    def ingresar(self, cantidad):
        super().ingresar(cantidad)
        self.movimientos.append(Movimiento(cantidad, "Ingreso"))
        
    def extraer(self, cantidad):
        super().extraer(cantidad)
        self.movimientos.append(Movimiento(cantidad, "Extraccion"))
    
    def ultimos_movimientos(self, valor=5):
        return self.movimientos[-valor:]

cm = Cuenta_Movimientos(500, 100)
cm.extraer(20)
cm.extraer(70)
cm.ingresar(50)
cm.extraer(30)
cm.ingresar(40)
cm.ingresar(25)
ultimos = cm.ultimos_movimientos()
for m in ultimos:
    print(m)
    




        

