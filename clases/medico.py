from paciente import paciente
from cli import cli

class PacienteNoEncontradoException(Exception):
    """Excepción lanzada cuando no se encuentra un paciente"""
    pass

class MedicoNoDisponibleException(Exception):
    """Excepción lanzada cuando el médico no está disponible"""
    pass

class TurnoOcupadoException(Exception):
    """Excepción lanzada cuando un turno ya está ocupado"""
    pass

class RecetaInvalidaException(Exception):
    """Excepción lanzada cuando una receta es inválida"""
    pass

class DatosMedico():
    especialidades = []
    matricula = []
    nombre = []
    
    try:
        cantidad_especialidad = int(input("¿Cuántas especialidades hay en la clínica? "))
        if cantidad_especialidad <= 0:
            raise ValueError("Debe haber al menos una especialidad")
            
        for i in range(cantidad_especialidad):
            especialidad = str(input("Ingrese su especialidad: "))
            matr_lgj = int(input("Ingrese su matrícula: "))
            nomb = str(input("Ingrese su nombre: "))
            
            if not especialidad:
                raise ValueError("La especialidad no puede estar vacía")
            if matr_lgj <= 0:
                raise ValueError("La matrícula debe ser un número positivo")
            if not nomb:
                raise ValueError("El nombre no puede estar vacío")
                
            especialidades.append(especialidad)
            matricula.append(matr_lgj)
            nombre.append(nomb)
            
    except ValueError as e:
        print(f"Error: {e}")
        # Aquí podrías manejar el error o volver a solicitar los datos

horarios_especialidad = {
    "Pediatría": ["lunes", "miércoles", "viernes"],
    "Psicologia": ["martes", "miércoles", "jueves"],
    "Cardiología": ["lunes", "jueves", "sábado"],
    "Dermatología": ["martes", "viernes"]
}

class Medico:
    @staticmethod
    def obtener_datos(dni, nombre, fecha_nac, hoy, edad):
        try:
            if not dni or not nombre:
                raise PacienteNoEncontradoException("Datos del paciente incompletos")
                
            paciente = paciente()
            paciente.dni = dni
            paciente.nombre = nombre
            paciente.fecha_nac = fecha_nac
            paciente.hoy = hoy
            paciente.edad = edad
            
            # Verificar disponibilidad del médico
            if not paciente.especialidad or paciente.especialidad not in horarios_especialidad:
                raise MedicoNoDisponibleException(f"No hay médicos disponibles para la especialidad {paciente.especialidad}")
                
            return paciente
            
        except PacienteNoEncontradoException as e:
            print(f"Error al encontrar paciente: {e}")
            raise
        except MedicoNoDisponibleException as e:
            print(f"Error de disponibilidad médica: {e}")
            raise

try:
    regresar = input("¿Deseas volver al menú? (Y/n) ").lower()
    if regresar == 'y':
        cli()
    else:
        print("Saliendo del sistema...")
except Exception as e:
    print(f"Error inesperado: {e}")
