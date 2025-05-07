import unittest
from calculadora import Calculadora


class TestCalculadora(unittest.TestCase):
    def test_sumar_dos_mas_dos(self):
        calc = Calculadora()
        resultado = calc.sumar(2, 2)
        self.assertEqual(resultado, 4)


if __name__ == '__main__':
    unittest.main()
