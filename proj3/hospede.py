from pessoa import Pessoa

class Hospede(Pessoa):
    def __init__(self, id, nome, email):
        super().__init__(id, nome, email)
        self.__reservas = []
    
    def fazer_reserva(self, reserva):
        pass

    def cancelar_reserva(self, reserva):
        pass

    def consultar_reservas(self):
        pass

    