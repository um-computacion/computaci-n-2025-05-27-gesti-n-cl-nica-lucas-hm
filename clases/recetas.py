from medico import datos_medico
from paciente import paciente

class Receta:
    def __init__(self, id_paciente, medicamentos_indicados):
        self.id_paciente = id_paciente
        self.medicamentos = medicamentos_indicados  # Lista de strings: ["Paracetamol 500mg", "Ibuprofeno 400mg"]

    def generar_receta(self):
        # Obtener datos del médico
        medico = {
            "nombre": datos_medico.nombre,
            "matricula": datos_medico.matricula,
            "especialidad": datos_medico.especialidades[0]  # Primera especialidad
        }
        
        # Obtener datos del paciente
        paciente_seleccionado = None
        for p in paciente.lista_pacientes:
            if p["id"] == self.id_paciente:  # Asumiendo que cada paciente tiene un "id"
                paciente_seleccionado = p
                break
        
        if not paciente_seleccionado:
            raise ValueError("Paciente no encontrado")
        
        # Plantilla de la receta
        receta = f"""
        {'='*50}
        RECETA MÉDICA
        {'='*50}
        Médico: {medico['nombre']}
        Matrícula: {medico['matricula']}
        Especialidad: {medico['especialidad']}
        
        Paciente: {paciente_seleccionado['nombre']}
        ID: {paciente_seleccionado['id']}
        {'-'*50}
        Medicamentos:
        """
        
        for i, med in enumerate(self.medicamentos, 1):
            receta += f"{i}. {med}\n"
        
        receta += f"\nFirma: _________________________\n{medico['nombre']}"
        
        return receta