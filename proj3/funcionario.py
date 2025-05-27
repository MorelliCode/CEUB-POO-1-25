from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, id, nome, email):
        super().__init__(id, nome, email)
    
    def add_quarto(self, hotel, quarto):
        hotel.add_quarto(quarto)

    def remover_quarto(self, hotel, quarto):
        hotel.remover_quarto(quarto)

    def registrar_hospede(self, hotel, hospede):
        pass

    def cancelar_reserva(self, hotel, reserva):
        pass
    