class Usuario:
    def __init__(self, nombre_de_usuario, password):
        self.nombre_de_usuario = nombre_de_usuario
        self.password = password

    def iniciar_sesion(self, nombre_usuario_ingresado, password_ingresada):
        if self.nombre_de_usuario == nombre_usuario_ingresado and self.password == password_ingresada:
            print(f"¡Bienvenido {self.nombre_de_usuario}! Sesión iniciada correctamente.")
            print()
            return True
        else:
            print(f"Credenciales del {self.nombre_de_usuario} incorrectas. Acceso denegado.")
            return False

class Administrador(Usuario):
    def __init__(self, nombre_de_usuario, password):
        super().__init__(nombre_de_usuario, password)

    def gestionar_usuarios(self):
        print()
        print(f"Administrador {self.nombre_de_usuario} está gestionando usuarios del sistema")

class Cliente(Usuario):
    def __init__(self, nombre_de_usuario, password):
        super().__init__(nombre_de_usuario, password)

    def realizar_compras(self):
        print(f"Cliente {self.nombre_de_usuario} está realizando una compra")

if __name__ == "__main__":
    print("sistema de control")
    print()
    
    admin = Administrador("admin", "652")
    cliente1 = Cliente("cliente1", "165")
    cliente2 = Cliente("cliente2", "206")
    
  
    print("Pruebas de inicio de sesión:")
    print()
    admin.iniciar_sesion("admin", "652")  
    cliente1.iniciar_sesion("cliente1", "165")  
    cliente2.iniciar_sesion("cliente2", "207")  
    
    print("Funcionalidades específicas:")
    admin.gestionar_usuarios()
    cliente1.realizar_compras()

