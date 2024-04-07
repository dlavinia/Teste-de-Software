# tests.py
import unittest
import triangulo

class TrianguloTest(unittest.TestCase):

    def test_valores_limites(self):
        # Testes limite inferior
        self.assertTrue(triangulo.Triangulo(1, 1, 1).validarForma())  
        self.assertTrue(triangulo.Triangulo(1, 1, 1).ehEquilatero())  
        self.assertTrue(triangulo.Triangulo(1, 2, 2).ehIsosceles())  
        self.assertTrue(triangulo.Triangulo(2, 3, 4).ehEscaleno())  

        # Testes limite superior
        self.assertTrue(triangulo.Triangulo(100, 100, 100).validarForma())  
        self.assertTrue(triangulo.Triangulo(100, 100, 100).ehEquilatero())  
        self.assertFalse(triangulo.Triangulo(100, 100, 100).ehIsosceles())  
        self.assertFalse(triangulo.Triangulo(100, 100, 100).ehEscaleno())  

        # Testes com valores extremos
        self.assertTrue(triangulo.Triangulo(50, 51, 51).validarForma())  
        self.assertFalse(triangulo.Triangulo(50, 51, 51).ehEquilatero())  
        self.assertTrue(triangulo.Triangulo(50, 51, 51).ehIsosceles())  
        self.assertFalse(triangulo.Triangulo(50, 51, 51).ehEscaleno())  

        # Testes com valores nulos ou negativos
        self.assertFalse(triangulo.Triangulo(0, 1, 1).validarForma()) 
        self.assertFalse(triangulo.Triangulo(0, 1, 1).ehEquilatero()) 
        self.assertFalse(triangulo.Triangulo(0, 1, 1).ehIsosceles()) 
        self.assertFalse(triangulo.Triangulo(0, 1, 1).ehEscaleno()) 

        self.assertFalse(triangulo.Triangulo(-1, 1, 1).validarForma())  
        self.assertFalse(triangulo.Triangulo(-1, 1, 1).ehEquilatero())  
        self.assertFalse(triangulo.Triangulo(-1, 1, 1).ehIsosceles())  
        self.assertFalse(triangulo.Triangulo(-1, 1, 1).ehEscaleno())  
        self.assertFalse(triangulo.Triangulo(1, 0, 1).validarForma())  

if __name__ == '__main__':
    unittest.main()