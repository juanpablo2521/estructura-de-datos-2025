class FiguraGeometrica:  
    def calcular_area(self):
        pass
    

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

class Cuadrado(FiguraGeometrica): 
    def __init__(self, lado):
        super().__init__()
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado

if __name__ == "__main__":
    print("calculadora")    

    triangulo1 = Triangulo(25,22)
    cuadrado1 = Cuadrado(9)

    print(f"Triángulo (base=25, altura=22):")
    print(f"Área = {triangulo1.calcular_area()}")
    print()

    print(f"Cuadrado (lado=9):")
    print(f"Área = {cuadrado1.calcular_area()}")
