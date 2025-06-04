from paciente import paciente

class datos_medico():
    matr_lgj = int(input("ingrese su matricula: "))
    nomb = str(input("ingrese su nombre: "))
    especialidad = str(input("ingrese su especialidad: "))

class medico():
    def obtener_datos(dni, nombre, fecha_nac, hoy, edad):
        paciente.dni = dni
        paciente.nombre = nombre
        paciente.fecha_nac = fecha_nac
        paciente.hoy = hoy
        paciente.edad = edad
        paciente.lista_pacientes