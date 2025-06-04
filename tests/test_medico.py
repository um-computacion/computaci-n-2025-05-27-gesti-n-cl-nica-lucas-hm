from clases import medico
import unittest
from unittest import TestCase

class test_2(unittest.TestCase):
    def test_medico(self, patch_input):
        b = self.assertEqual(medico.datos_medico.matr_lgj, "64982")
        c = self.assertEqual(medico.datos_medico.nomb, "Juan Carlos Peralta")
        d = self.assertEqual(medico.datos_medico.especialidad, "Cariologo")

if __name__ == "__main__":
    unittest.main()