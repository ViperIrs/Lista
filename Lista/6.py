import re
import pytest

def contar_palavras(texto):
    palavras = re.findall(r'\b\w+\b', texto)
    return len(palavras)

def test_contar_palavras():
    assert contar_palavras("Este é um exemplo de texto com algumas palavras.") == 8
    assert contar_palavras("Olá, mundo!") == 2
    assert contar_palavras("123 456 789") == 3
    assert contar_palavras("Palavra") == 1
    assert contar_palavras("Este texto contém algumas repetições. Este é um exemplo de texto.") == 10
    assert contar_palavras("") == 0

if __name__ == "__main__":
    pytest.main()
