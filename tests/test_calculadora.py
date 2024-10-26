import unittest
from src.calculadora import sumar, restar, multiplicar, dividir

class TestCalculadora(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(1, 2), 3)

    def test_restar(self):
        self.assertEqual(restar(5, 3), 2)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(2, 3), 6)

    def test_dividir(self):
        self.assertEqual(dividir(6, 3), 2)

    def test_dividir_por_cero(self):
        with self.assertRaises(ValueError):
            dividir(1, 0)

if __name__ == '__main__':
    unittest.main()

