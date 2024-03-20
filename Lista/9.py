class Voo:
    def __init__(self, origem, destino, data, hora, assentos_disponiveis):
        self.origem = origem
        self.destino = destino
        self.data = data
        self.hora = hora
        self.assentos_disponiveis = assentos_disponiveis

class SistemaReservas:
    def __init__(self):
        self.voos = []

    def adicionar_voo(self, voo):
        self.voos.append(voo)

    def pesquisar_voos(self, origem, destino, data):
        voos_disponiveis = []
        for voo in self.voos:
            if voo.origem == origem and voo.destino == destino and voo.data == data and voo.assentos_disponiveis > 0:
                voos_disponiveis.append(voo)
        return voos_disponiveis

    def realizar_reserva(self, voo):
        if voo.assentos_disponiveis > 0:
            voo.assentos_disponiveis -= 1
            return True
        else:
            return False

    def visualizar_reservas(self):
        reservas = []
        for voo in self.voos:
            if voo.assentos_disponiveis < voo.assentos_totais:
                reservas.append(voo)
        return reservas

    def cancelar_reserva(self, voo):
        voo.assentos_disponiveis += 1


import pytest

def test_sistema_reservas():
    sistema = SistemaReservas()

    voo1 = Voo("São Paulo", "Rio de Janeiro", "2024-04-01", "08:00", 100)
    voo2 = Voo("Rio de Janeiro", "São Paulo", "2024-04-02", "10:00", 50)
    sistema.adicionar_voo(voo1)
    sistema.adicionar_voo(voo2)

    assert sistema.voos == [voo1, voo2]

    voos_disponiveis = sistema.pesquisar_voos("São Paulo", "Rio de Janeiro", "2024-04-01")
    assert voos_disponiveis == [voo1]

    assert sistema.realizar_reserva(voo1) == True
    assert voo1.assentos_disponiveis == 99

    reservas = sistema.visualizar_reservas()
    assert reservas == [voo1]

    sistema.cancelar_reserva(voo1)
    assert voo1.assentos_disponiveis == 100

if __name__ == "__main__":
    pytest.main()
