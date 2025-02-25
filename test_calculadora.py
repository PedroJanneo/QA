import pytest
from calculadora import calculadora  # Importa a função calculadora do arquivo calculadora.py

def test_soma():
    # Testa a operação de soma
    assert calculadora('soma', 2, 3) == 5
    assert calculadora('soma', -1, 1) == 0
    assert calculadora('soma', 0, 0) == 0

def test_subtracao():
    # Testa a operação de subtração
    assert calculadora('subtracao', 5, 3) == 2
    assert calculadora('subtracao', -1, -1) == 0
    assert calculadora('subtracao', 10, 20) == -10

def test_multiplicacao():
    # Testa a operação de multiplicação
    assert calculadora('multiplicacao', 3, 4) == 12
    assert calculadora('multiplicacao', -2, 5) == -10
    assert calculadora('multiplicacao', 0, 10) == 0

def test_divisao():
    # Testa a operação de divisão
    assert calculadora('divisao', 10, 2) == 5
    assert calculadora('divisao', 9, 3) == 3
    assert calculadora('divisao', 1, 2) == 0.5

def test_divisao_por_zero():
    # Testa a divisão por zero
    with pytest.raises(ValueError, match="Divisão por zero não é permitida."):
        calculadora('divisao', 10, 0)

def test_operacao_invalida():
    # Testa uma operação inválida
    with pytest.raises(ValueError, match="Operação inválida. Use 'soma', 'subtracao', 'multiplicacao' ou 'divisao'."):
        calculadora('potencia', 2, 3)
