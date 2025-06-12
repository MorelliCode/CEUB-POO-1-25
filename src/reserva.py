class Reserva():
    def __init__(self, hospede:object, quarto:object):
        self.__hospede = hospede
        self.__quarto = quarto

    def get_quarto(self):
        return self.__quarto
    
    def get_hospede(self):
        return self.__hospede

    def __str__(self):
        return f"Reserva do {self.__quarto} por {self.__hospede}"