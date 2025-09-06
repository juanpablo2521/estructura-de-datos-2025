class Empleado:
 
    def __init__(self, nombre, salario, departamento):
   
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento
    
    def trabajar(self):
        print(f"{self.nombre} está trabajando en el departamento de {self.departamento}.")
        


empleado1 = Empleado("Juan", 30000, "Ventas")
empleado1.trabajar()


class Desarrollador(Empleado):
    def __init__(self, nombre, salario, departamento, lenguaje_programacion):
        super().__init__(nombre, salario, departamento)
        self.lenguaje_programacion = lenguaje_programacion
    
    def trabajar(self):
        print(f"{self.nombre} esta escribiendo codigo en {self.lenguaje_programacion}")
        self.escribir_codigo()

    def escribir_codigo(self):
        print(f"Escribiendo condigo en {self.lenguaje_programacion}")
        print("¡Codigo completado exitosamente!")

dev1 = Desarrollador("Ana", 50000, "IT", "Python")
dev1.trabajar()


lista_empleados = [empleado1, dev1]

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento, equipo):
        super().__init__(nombre, salario, departamento)
        self.equipo = equipo

    def trabajar(self):
        print(f"{self.nombre}  esta gestionando el departamento de {self.departamento}")
        self.supervisar_equipo()

    def supervisar_equipo(self):
        if self.equipo:
            print(f"supervisando a {len(self.equipo)} empleados: ")
            for empleado in self.equipo:
                print(f" - {empleado.nombre}")
        else:
            print("no tiene ningun empleado en supervisión")

gerente1 = Gerente("Carlos", 70000, "IT", lista_empleados)
gerente1.trabajar()
gerente_sin_equipo = Gerente("Laura", 60000, "HR", [])
gerente_sin_equipo.trabajar()





