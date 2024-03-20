from datetime import datetime
import pytest

def diferenca_entre_datas(data1, data2):
    delta = data2 - data1
    dif_dias = delta.days
    dif_meses = delta.days // 30  
    dif_anos = delta.days // 365  
    dif_horas = delta.total_seconds() // 3600
    dif_minutos = delta.total_seconds() // 60
    return dif_dias, dif_meses, dif_anos, dif_horas, dif_minutos

def test_diferenca_entre_datas():
    data1 = datetime(2022, 1, 1)
    data2 = datetime(2022, 1, 10)
    assert diferenca_entre_datas(data1, data2) == (9, 0, 0, 216, 12960)

    data1 = datetime(2022, 1, 1, 12, 30)
    data2 = datetime(2022, 1, 10, 10, 45)
    assert diferenca_entre_datas(data1, data2) == (8, 0, 0, 214, 12868)

    data1 = datetime(2021, 12, 1)
    data2 = datetime(2022, 2, 1)
    assert diferenca_entre_datas(data1, data2) == (31, 1, 0, 744, 44640)

    data1 = datetime(2020, 1, 1)
    data2 = datetime(2024, 1, 1)
    assert diferenca_entre_datas(data1, data2) == (1461, 48, 4, 35064, 2103840)

if __name__ == "__main__":
    pytest.main()
