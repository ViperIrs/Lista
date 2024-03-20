import re
import pytest

def validar_numero_telefone(numero):
    padrao = r'^\([1-9]{2}\) [2-9][0-9]{3,4}-[0-9]{4}$'
    return bool(re.match(padrao, numero))

def test_validar_numero_telefone():
    assert validar_numero_telefone("(11) 91234-5678") == True
    assert validar_numero_telefone("(21) 99876-5432") == True
    assert validar_numero_telefone("(31) 9876-5432") == True
    assert validar_numero_telefone("(41) 87654-3210") == True

    assert validar_numero_telefone("11) 91234-5678") == False  
    assert validar_numero_telefone("(11)91234-5678") == False  
    assert validar_numero_telefone("(11) 912345678") == False 
    assert validar_numero_telefone("(11) 9123-45678") == False  
    assert validar_numero_telefone("(01) 91234-5678") == False 
    assert validar_numero_telefone("(11) 01234-5678") == False  

if __name__ == "__main__":
    pytest.main()
