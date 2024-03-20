import pytest
def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b


def test_adicao():
    assert adicao(3, 5) == 8
    assert adicao(-1, 1) == 0
    assert adicao(0, 0) == 0

def test_subtracao():
    assert subtracao(10, 5) == 5
    assert subtracao(-1, 1) == -2
    assert subtracao(0, 0) == 0

def test_multiplicacao():
    assert multiplicacao(3, 4) == 12
    assert multiplicacao(-2, 5) == -10
    assert multiplicacao(0, 10) == 0

def test_divisao():
    assert divisao(10, 2) == 5
    assert divisao(-10, 2) == -5
    assert divisao(0, 5) == 0
    try:
        divisao(1, 0)
    except ValueError as e:
        assert str(e) == "Não é possível dividir por zero."


