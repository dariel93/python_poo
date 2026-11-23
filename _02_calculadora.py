class Calculadora:
    
    def __init__(self,op1 ,op2):
        self.operando_1 = op1
        self.operando_2 = op2
            
    def sumar(self):
        return self.operando_1 + self.operando_2
    def restar(self):
        return max(self.operando_1, self.operando_2) - min(self.operando_1, self.operando_2)
    def multiplicar(self):
        return self.operando_1 * self.operando_2
    def dividir(self):
        return max(self.operando_1, self.operando_2) / min(self.operando_1, self.operando_2)
        