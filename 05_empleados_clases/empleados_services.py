import csv

class Empleado:
    def __init__(self, name, age, salary, departament):
        self.name = name
        self.age = age
        self.salary = salary
        self.departament = departament

class Empresa:
    def __init__(self, direction):
        self.direction = direction

    def alta_empleado(self, empleado):
        with open(self.direction, "a", newline="") as f:
            csv.writer(f).writerow([empleado.name, empleado.age, empleado.salary, empleado.departament])

    def buscar_empleado(self, name):
        with open(self.direction, "r"):
            for e in csv.reader:
                if e[0] == name:
                    return Empleado(e[0], int(e[1]), float(e[2]), e[3])
            return None

    def empleados_departamento(self, departament):
        with open(self.direction, "r") as f:
            datos=list(csv.DictReader(f))
            return [Empleado(e["name"],int(e["age"]),float(e["salary"]),e["departament"]) for e in datos if e["departament"]==departament] 

