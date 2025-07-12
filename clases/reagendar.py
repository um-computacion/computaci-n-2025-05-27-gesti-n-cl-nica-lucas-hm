from medico import DatosMedico
from paciente import paciente
from datetime import date
from cli import cli

class consultas():
    def agendar(reagenda):
        reagenda = date(input("ingrese fecha del nuevo turno: "))
        paciente.dni
        paciente.fecha_nac
        paciente.nombre
        
        DatosMedico.nombre
        DatosMedico.matricula
        DatosMedico.especialidades
    print("turno reagendado")
regresar = str(input("Deseas volver al menu? (Y/n) "))
if regresar == "y":
    cli()
else:
    exit
