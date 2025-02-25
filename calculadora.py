def calculadora(operacao, num1, num2):
    """
    Função que realiza operações básicas de calculadora: soma, subtração, multiplicação e divisão.

    :param operacao: String que indica a operação ('soma', 'subtracao', 'multiplicacao', 'divisao').
    :param num1: Primeiro número (float ou int).
    :param num2: Segundo número (float ou int).
    :return: Resultado da operação (float).
    :raises ValueError: Se a operação não for válida ou se houver divisão por zero.
    """
    if operacao == 'soma':
        return num1 + num2
    elif operacao == 'subtracao':
        return num1 - num2
    elif operacao == 'multiplicacao':
        return num1 * num2
    elif operacao == 'divisao':
        if num2 == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return num1 / num2
    else:
        raise ValueError("Operação inválida. Use 'soma', 'subtracao', 'multiplicacao' ou 'divisao'.")
