# tests.py

import unittest
import model, datetime
import unittest

class TestTriangulo(unittest.TestCase):

    def test_validar_forma(self):
        # Forma válida
        self.assertTrue(model.Triangulo(3, 4, 5).validarForma())  
        self.assertTrue(model.Triangulo(5, 5, 5).validarForma())  
        self.assertTrue(model.Triangulo(5, 5, 7).validarForma())  

        # Forma inválida
        self.assertFalse(model.Triangulo(1, 2, 3).validarForma())
        self.assertFalse(model.Triangulo(2, 3, 6).validarForma())
        self.assertFalse(model.Triangulo(0, 2, 3).validarForma())

    def test_eh_equilatero(self):
        self.assertTrue(model.Triangulo(5, 5, 5).ehEquilatero())  
       
    def test_nao_eh_equilatero(self):
        # A != C
        self.assertFalse(model.Triangulo(10, 10, 15).ehEquilatero()) 

        # A != B
        self.assertFalse(model.Triangulo(15, 10, 15).ehEquilatero())  

        # B != C
        self.assertFalse(model.Triangulo(10, 10, 15).ehEquilatero()) 

    def test_eh_isosceles(self):
        self.assertTrue(model.Triangulo(5, 5, 7).ehIsosceles())  
    
    def test_nao_eh_isoceles(self):
        # A = B e A = C
        self.assertFalse(model.Triangulo(3, 3, 3).ehIsosceles())

        # A != B e B != C
        self.assertFalse(model.Triangulo(10, 15, 20).ehIsosceles())

    def test_eh_escaleno(self):
        self.assertTrue(model.Triangulo(3, 4, 5).ehEscaleno()) 

    def test_nao_eh_escaleno(self):
       # A = B e A != C
       self.assertFalse(model.Triangulo(5, 5, 10).ehEscaleno())

       # A = C e A != B
       self.assertFalse(model.Triangulo(10, 5, 10).ehEscaleno())

       # B = C e A != B
       self.assertFalse(model.Triangulo(5, 10, 10).ehEscaleno())

       # A = B e A = C
       self.assertFalse(model.Triangulo(10, 10, 10).ehEscaleno())

if __name__ == '__main__':
    unittest.main()