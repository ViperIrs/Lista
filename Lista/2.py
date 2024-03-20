class ConversorMoedas:
    def __init__(self, taxa_dolar_para_real=5.5, taxa_dolar_para_euro=0.85):
        self.taxa_dolar_para_real = taxa_dolar_para_real
        self.taxa_dolar_para_euro = taxa_dolar_para_euro

    def dolar_para_real(self, valor):
        return valor * self.taxa_dolar_para_real

    def real_para_dolar(self, valor):
        return valor / self.taxa_dolar_para_real

    def dolar_para_euro(self, valor):
        return valor * self.taxa_dolar_para_euro

    def euro_para_dolar(self, valor):
        return valor / self.taxa_dolar_para_euro


import pytest

@pytest.fixture
def conversor():
    return ConversorMoedas()

def test_dolar_para_real(conversor):
    assert conversor.dolar_para_real(10) == 55.0
    assert conversor.dolar_para_real(0) == 0
    assert conversor.dolar_para_real(-5) == -27.5

def test_real_para_dolar(conversor):
    assert conversor.real_para_dolar(55.0) == 10
    assert conversor.real_para_dolar(0) == 0
    assert conversor.real_para_dolar(-27.5) == -5

def test_dolar_para_euro(conversor):
    assert conversor.dolar_para_euro(10) == 8.5
    assert conversor.dolar_para_euro(0) == 0
    assert conversor.dolar_para_euro(-5) == -4.25

def test_euro_para_dolar(conversor):
    assert conversor.euro_para_dolar(8.5) == 10
    assert conversor.euro_para_dolar(0) == 0
    assert conversor.euro_para_dolar(-4.25) == -5

if __name__ == "__main__":
    pytest.main()
