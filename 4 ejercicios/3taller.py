class Electrodomestico:
    def __init__(self, marca, modelo, consumo_energetico):
        self.marca = marca
        self.modelo = modelo
        self.consumo_energetico = consumo_energetico
    
    def encender(self):
        print(f"El electrodoméstico {self.marca} {self.modelo} está encendido.")
        
class Lavadora(Electrodomestico):
    def __init__(self, marca, modelo, consumo_energetico, capacidad):
        super().__init__(marca, modelo, consumo_energetico)
        self.capacidad = capacidad
    
    def encender(self):
        print(f"encendiendo lavadora {self.marca} {self.modelo}")
        self.iniciar_ciclo_de_lavado()

    def iniciar_ciclo_de_lavado(self):
        print(f"se inicio el ciclo de lavado - capacidad: {self.capacidad} kg")
        print("Se esta llenando con agua")
        print("El ciclo esta en progreso")


class Refrigerador(Electrodomestico):
    def __init__(self, marca, modelo, consumo_energetico, congelador):
        super().__init__(marca, modelo, consumo_energetico)
        self.congelador = congelador

    def encender(self):
        print(f"se esta encendiendo el refrigerador {self.marca} {self.modelo}")
        self.regularTemperatura()

    def regularTemperatura(self):
        print("se esta regulando la temperatura del refrigerador")
        if self.congelador:
            print("se esta activando el sistema de congelacion")
            print("temperatura alcanzada")
        else: print(f"el sistema de regulacion temperatura del refrigerador {self.marca} no se inicio por problemas en el congelador")

if __name__ == "__main__":
    print("Prueba de Electrodomesticos")
    print()
    Lavadora1 = Lavadora("Samsung", "CleanMax", "500W", 7)
    Lavadora1.encender()
    print() 

    Refrigerador1 = Refrigerador("Mabe", "IceCool", "300W", True) # o false si no tiene congelador
    Refrigerador1.encender()

    