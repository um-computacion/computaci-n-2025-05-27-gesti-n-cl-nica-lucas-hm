import sys
import os
from clases.menu import Menu

# Agregar el directorio padre al path para importar los módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class cli():
    def obtener_menu(self):
        Menu.mostrar_menu
    def elegir_opcion(self):
        Menu.inicio