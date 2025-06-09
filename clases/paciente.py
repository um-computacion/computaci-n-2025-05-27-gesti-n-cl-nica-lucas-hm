from datetime import date
from menu import menu
class paciente():
    lista_pacientes = []
    n = int(input("cuantos pacientes vas a tener?"))
    for i in range(n):
        dni = int(input("ingrese su DNI: "))
        nombre = str(input("ingrese su nombre: "))
        entrada = date(input("Ingresa tu fecha de nacimiento (YYYY-MM-DD): "))
        anio, mes, dia = map(int, entrada.split('-'))
        fecha_nac = date(anio, mes, dia)
        especialidad =str(input("que especialidad desea consultar? "))
    
        # Calcular edad aproximada
        hoy = date(input("ingresa la fecha de pedido de turno: "))
        edad = hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))
    lista_pacientes.append(dni, nombre, fecha_nac, edad, hoy, especialidad)
regresar = int(input("Deseas volver al menu? (Y/n) "))
if regresar = y:
    menu.menu
else:
    break
