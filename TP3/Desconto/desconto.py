import datetime

def calcular_desconto(valor_compra, idade_dependente):
    if idade_dependente < 0 or idade_dependente > 24:
        raise TypeError('Idade inválida')

    if valor_compra < 250:
        raise TypeError('Valor da compra inválido')

    if idade_dependente <= 12:
        return valor_compra * 0.15
    
    elif idade_dependente <= 18:
        return valor_compra * 0.12
    
    elif idade_dependente <= 21:
        return valor_compra * 0.05
    
    elif idade_dependente <= 24:
        return valor_compra * 0.03