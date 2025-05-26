class Hotel:
    def __init__(self):
        self.__quartos = []
        self.__hospedes = []
        self.__reservas = []

    def add_quarto(quarto):
        pass

    def remover_quarto(quarto):
        pass

    def registrar_hospede(self, hospede):
        self.__hospedes.append(hospede)

    def cancelar_reserva(reserva):
        pass
    
    def get_quartos(self):
        return self.__quartos
    
    def get_hospedes(self):
        return self.__hospedes
    
    def get_reservas(self):
        return self.__reservas