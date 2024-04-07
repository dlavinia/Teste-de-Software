# tests.py
import unittest
import desconto

class DescontoTest(unittest.TestCase):
    def test_idade_dependente_invalida(self):
        with self.assertRaises(TypeError):
            desconto.calcular_desconto(300, -1) # logo abaixo do limite
            desconto.calcular_desconto(300, 25)  # logo acima do limite

    def test_valor_compra_abaixo_minimo(self):
        with self.assertRaises(TypeError):
            desconto.calcular_desconto(249, 10)  # logo abaixo do limite

    def test_valor_desconto_por_idade(self):
        self.assertEqual(desconto.calcular_desconto(300, 10), 45.0)  # 15% - idade <= 12
        self.assertEqual(desconto.calcular_desconto(300, 15), 36.0)  # 12% - 12 < idade <= 18
        self.assertEqual(desconto.calcular_desconto(300, 20), 15.0)  # 5% - 18 < idade <= 21
        self.assertEqual(desconto.calcular_desconto(300, 24), 9.0)  # 3% - 21 < idade <= 24

    def test_valores_limites(self):
        self.assertEqual(desconto.calcular_desconto(250, 0), 37.5)  # Limite inferior de compra e idade
        self.assertEqual(desconto.calcular_desconto(250, 24), 7.5)   # Limite inferior de compra e superior de idade

        self.assertEqual(desconto.calcular_desconto(1000, 24), 30.0)  # Limite superior de idade



if __name__ == '__main__':
    unittest.main()