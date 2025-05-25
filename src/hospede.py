from pessoa import Pessoa

class Hospede(Pessoa):
    def __init__(self, id, nome, email):
        super().__init__(id, nome, email)
        self.__reservas = []

    def fazer_reserva(reserva):
        pass

    def cancelar_reserva(reserva):
        pass

    def consultar_reservas():
        pass

    def __str__(self):
        return "hóspede " + super().__str__()