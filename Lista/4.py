import re
import pytest

def validar_email(email):
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
        return False
    return True

def test_validar_email():
    assert validar_email("usuario@example.com") == True
    assert validar_email("primeiro.ultimo@example.com") == True
    assert validar_email("usuario123@example.com") == True
    assert validar_email("usuario+alias@example.com") == True
    assert validar_email("primeiro.ultimo@example.co.uk") == True
    assert validar_email("primeiro.ultimo@subdominio.example.com") == True
    assert validar_email("primeiro.ultimo@subdominio.example.co.uk") == True
    assert validar_email("primeiro.ultimo@sub.domínio.com") == True
    assert validar_email("primeiro.ultimo@sub.domínio.co.uk") == True

    assert validar_email("usuarioexample.com") == False
    assert validar_email("usuario@examplecom") == False
    assert validar_email("usuario.example.com") == False
    assert validar_email("usuario@example.") == False
    assert validar_email("@example.com") == False
    assert validar_email("usuario@.example.com") == False
    assert validar_email("usuario@-example.com") == False
    assert validar_email("usuario@e_x_a_m_p_l_e.com") == False
    assert validar_email("usuario@example.c") == False

if __name__ == "__main__":
    pytest.main()
