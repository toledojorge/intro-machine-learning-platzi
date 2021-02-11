import unittest

def es_mayor_edad(edad):
    if edad >= 18:
        return True
    else:
        return False
        
class TestCajaCristal(unittest.TestCase):

    def test_es_mayor_edad(self):
        edad = 20

        resultado = es_mayor_edad(edad)

        self.assertEqual(resultado, True)

    def test_es_menor_edad(self):
        edad = 14

        resultado = es_mayor_edad(edad)

        self.assertEqual(resultado, False)


if __name__ == '__main__':
    unittest.main()