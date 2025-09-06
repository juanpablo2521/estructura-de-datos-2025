
class Vehiculo:
        def __init__(self, marca, combustible, tipo, nivel_combustible, nivel_tanque):
                self.marca = marca
                self.combustible = combustible
                self.tipo = tipo
                self.nivel_combustible = nivel_combustible
                self.nivel_tanque = nivel_tanque

        def encender(self):
                porcentaje = (self.nivel_combustible / self.nivel_tanque) * 100
                if porcentaje < 10:
                        print(f"Cuidado papi, {self.tipo} '{self.marca}' nivel de gasolina muy bajo {porcentaje:.1f}%.")
                        print(f"El vehiculo {self.marca} no ha podido encender")
                else:
                        print(f"{self.tipo.capitalize()} '{self.marca}' encendido correctamente. Nivel de combustible: {porcentaje:.1f}%.")
                    
        def marcha(self, consumo_km=0.5, km=15):
                print(f"{self.tipo.capitalize()} '{self.marca}' inicia la marcha")
                for i in range(1, km + 1):
                        if self.nivel_combustible <= 0:
                                print(f"{self.tipo.capitalize()}'{self.marca}' se ha detenido, no tiene combustible")
                                break
                        self.nivel_combustible -= consumo_km
                        if self.nivel_combustible < 0:
                                self.nivel_combustible = 0
                        porcentaje = (self.nivel_combustible / self.nivel_tanque) * 100
                        print(f"kilometro {i}: Combustible restante: {self.nivel_combustible:.1f} gal ({porcentaje:.1f}%)")

                        if porcentaje < 10 and self.nivel_combustible > 0:
                                print(f"El tanque esta al: {porcentaje:.1f} busque una gasolinera")
                        
                else: 
                        print(f" {self.tipo.capitalize()} '{self.marca}' se termino el recorrido")

       
        def imprimir(self):
                print(f"Tipo: {self.tipo}, Marca: {self.marca}, Combustible: {self.combustible}")

class Moto(Vehiculo):
        def __init__(self, marca, combustible, nivel_combustible=5, nivel_tanque=5):
                super().__init__(marca, combustible, "moto", nivel_combustible, nivel_tanque)

class Carro(Vehiculo):
        def __init__(self, marca, combustible, nivel_combustible=12, nivel_tanque=12):
                super().__init__(marca, combustible, "carro", nivel_combustible, nivel_tanque)

mi_moto = Moto('Yamaha', 'Gasolina')
mi_carro = Carro('Chevrolet', 'Gasolina')

mi_moto.imprimir()
mi_moto.encender()
mi_moto.marcha(consumo_km=0.9, km=15)


mi_carro.imprimir()
mi_carro.encender()
mi_carro.marcha(consumo_km=0.5, km=20)
