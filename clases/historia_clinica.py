import paciente
from paciente import paciente
from cli import cli
class historia_clinica:
    for i in range(paciente.n):
        historial = paciente.lista_pacientes
        Edad = paciente.edad
        print("el historial de la persona es: ", historial," y la edad es: ", Edad)
regresar = str(input("Deseas volver al menu? (Y/n) "))
if regresar == "y":
    cli()
else:
    exit
