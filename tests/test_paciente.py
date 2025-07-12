import datetime
import unittest
from clases import paciente
from paciente import paciente
from unittest import TestCase
from datetime import date

class test_2(unittest.TestCase):
    def test_paciente(self, patch_input):
        b = self.assertEqual(paciente.paciente.lista_pacientes)

if __name__ == "__main__":
    unittest.main()
