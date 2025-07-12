import sys
import os

# Agregar el directorio padre al path para importar los módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from clases.menu import Menu

class CLI:
    def __init__(self):
        pass
    
    def obtener_menu(self):
        Menu.mostrar_menu()
    
    def elegir_opcion(self):
        Menu.inicio()

if __name__ == "__main__":
    cli_instance = CLI()
    cli_instance.elegir_opcion()