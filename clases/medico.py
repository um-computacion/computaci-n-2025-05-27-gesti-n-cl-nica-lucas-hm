from paciente import paciente
from menu import menu
class datos_medico():
    especialidades = []
    matricula = []
    nombre = []
    cantidad_especialidad = int(input("cuantas especialidades hay en la clinica? "))
    for i in range(cantidad_especialidad):
        especialidad = str(input("ingrese su especialidad: "))
        matr_lgj = int(input("ingrese su matricula: "))
        nomb = str(input("ingrese su nombre: "))
        
        especialidades.append(especialidad)
        matricula.append(matr_lgj)
        nombre.append(nomb)

horarios_especialidad = (
    "Pediatría",
    ["lunes", "miércoles", "viernes"],
    "Psicologia",
    ["Martes", "Miercoles", "Jueves"],
    "Cardiología",  # Nueva especialidad
    ["lunes", "jueves", "sábado"],  # Días de Cardiología
    "Dermatología",  # Otra especialidad
    ["martes", "viernes"],  # Días de Dermatología
)

class medico():
    def obtener_datos(dni, nombre, fecha_nac, hoy, edad):
        paciente.dni = dni
        paciente.nombre = nombre
        paciente.fecha_nac = fecha_nac
        paciente.hoy = hoy
        paciente.edad = edad
        paciente.lista_pacientes
        paciente.especialidad
regresar = int(input("Deseas volver al menu? (Y/n) "))
if regresar = y:
    menu.menu
else:
    break
