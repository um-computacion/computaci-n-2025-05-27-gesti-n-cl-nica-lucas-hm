import unittest
from clases.medico import datos_medico
from clases.recetas import Receta
from clases.paciente import paciente

# Configura datos de prueba (mock)
datos_medico.nombre = "Dr. Pérez"
datos_medico.matricula = "M-123456"
datos_medico.especialidades = ["Cardiología"]  # Asegúrate de que coincida con tu estructura real

paciente.lista_pacientes = [
    {"id": 1, "nombre": "Juan García", "edad": 35},
    {"id": 2, "nombre": "Ana López", "edad": 28}
]

class TestReceta(unittest.TestCase):
    def setUp(self):
        # Crear una receta para un paciente existente (id=1)
        self.receta_valida = Receta(
            id_paciente=1,
            medicamentos_indicados=["Paracetamol 500mg", "Ibuprofeno 400mg"]
        )
        
        # Receta para un paciente inexistente (id=99)
        self.receta_invalida = Receta(
            id_paciente=99,
            medicamentos_indicados=["Amoxicilina 250mg"]
        )

    def test_generar_receta_valida(self):
        """Prueba que la receta se genera correctamente para un paciente válido."""
        resultado = self.receta_valida.generar_receta()
        
        # Verifica que los datos clave estén en el resultado
        self.assertIn("Dr. Pérez", resultado)  # Nombre del médico
        self.assertIn("Juan García", resultado)  # Nombre del paciente
        self.assertIn("Paracetamol 500mg", resultado)  # Medicamento 1
        self.assertIn("Ibuprofeno 400mg", resultado)  # Medicamento 2

    def test_generar_receta_paciente_invalido(self):
        """Prueba que falla cuando el paciente no existe."""
        with self.assertRaises(ValueError):
            self.receta_invalida.generar_receta()

    def test_formato_receta(self):
        """Prueba que el formato de la receta incluye secciones clave."""
        resultado = self.receta_valida.generar_receta()
        self.assertIn("RECETA MÉDICA", resultado)  # Encabezado
        self.assertIn("Firma:", resultado)  # Pie de firma

if __name__ == "__main__":
    unittest.main()