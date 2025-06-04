from consulta import consulta
from historia_clinica import historia_clinica
from medico import medico
from paciente import paciente
from reagendar import consultas
from recetas import medicamento

def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Consulta")
    print("2. Historia Clínica")
    print("3. Médico")
    print("4. Paciente")
    print("5. Reagendar")
    print("6. Recetas")
    print("7. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            consulta()  # Llama a la función correspondiente en consulta.py
        elif opcion == "2":
            historia_clinica()  # Llama a la función correspondiente en historia_clinica.py
        elif opcion == "3":
            medico()  # Llama a la función correspondiente en medico.py
        elif opcion == "4":
            paciente()  # Llama a la función correspondiente en paciente.py
        elif opcion == "5":
            consultas()  # Llama a la función correspondiente en reagendar.py
        elif opcion == "6":
            medicamento()
        elif opcion == "7":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()