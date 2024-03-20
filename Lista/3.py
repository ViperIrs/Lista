import re
import pytest

def verificar_senha(senha):
    if len(senha) < 8:
        return False

    if not re.search(r"[A-Z]", senha):
        return False

    if not re.search(r"[a-z]", senha):
        return False

    if not re.search(r"\d", senha):
        return False

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
        return False

    return True

def test_verificar_senha():
    assert verificar_senha("Senha123!") == True
    assert verificar_senha("OlaMundo2022!") == True
    assert verificar_senha("1234abcd!") == True

    assert verificar_senha("1234") == False
    assert verificar_senha("senhafraca") == False
    assert verificar_senha("SENHAFORTE") == False
    assert verificar_senha("Senhaforte") == False
    assert verificar_senha("!@#$%^&*()") == False
    assert verificar_senha("Senha!@#$%^&*()") == False
    assert verificar_senha("senha12345") == False
    assert verificar_senha("Senha!@#$%") == False

if __name__ == "__main__":
    pytest.main()
