from consulta import consulta
from historia_clinica import historia_clinica
from medico import DatosMedico
from paciente import paciente
from reagendar import consultas
from recetas import Receta
from cli import cli

def crear_receta():
    try:
        id_paciente = input("Ingrese el ID del paciente: ")
        medicamentos = []
        print("Ingrese los medicamentos (escriba 'fin' para terminar):")
        while True:
            medicamento = input("Medicamento: ")
            if medicamento.lower() == 'fin':
                break
            medicamentos.append(medicamento)
        
        if not medicamentos:
            print("Debe ingresar al menos un medicamento.")
            return
        
        receta = Receta(id_paciente, medicamentos)
        print(receta.generar_receta())
    except Exception as e:
        print(f"Error al crear la receta: {e}")

class Menu:  # Las clases en Python por convención usan CamelCase
    @staticmethod
    def mostrar_menu():
        print("Menú Principal")
        print("1. Consulta")
        print("2. Historia Clínica")
        print("3. Médico")
        print("4. Paciente")
        print("5. Reagendar")
        print("6. Recetas")
        print("7. Salir")
    
    @staticmethod
    def inicio():
        while True:
            Menu.mostrar_menu()  # Llamar al método estático correctamente
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                consulta()  # Llama a la función correspondiente en consulta.py
            elif opcion == "2":
                historia_clinica()  # Llama a la función correspondiente en historia_clinica.py
            elif opcion == "3":
                DatosMedico()  # Usar la clase correcta de medico.py
            elif opcion == "4":
                paciente()  # Llama a la función correspondiente en paciente.py
            elif opcion == "5":
                consultas()  # Llama a la función correspondiente en reagendar.py
            elif opcion == "6":
                crear_receta()  # Usar la función para crear recetas
            elif opcion == "7":
                print("Saliendo...")
                break  # Usar break para salir del bucle en lugar de exit
            else:
                print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    cli()
