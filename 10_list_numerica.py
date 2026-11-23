# Crear una subclase de List para el almacenamiento de numeros con las siguientes caracterisitcas:
# Incluira los metodos:
# -sum(). Devuelve la suma de los numeros almacenados 
# -mean() Devuelve la media de los numeros almacenados
# Ademas de esos metodos , el construir recibira un parametro booleano que , en caso de ser true
# Impedira que se repitan los numeros

class Lista_Numerica(list):
    def __init__(self, unique):
        self.unique = unique
        
    def sum(self):
        return sum(self)
    
    def mean(self):
        if len(self)==0:
            return 0
        return sum(self) / len(self)
    
    def append(self, object):
        if not isinstance(object, (int, float)):
            return None
        if self.unique and object in self:
            return
        return super().append(object)
        
        
lst = Lista_Numerica(True)
lst.append(5)
lst.append(10)
lst.append(5.5)
lst.append("Helo")
print(f"Suma total: {lst.sum()}")
print(f"Media:  {lst.mean()}")
print(lst)
