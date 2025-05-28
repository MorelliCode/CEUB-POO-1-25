class Reserva():
    def __init__(self, hospede:object, quarto:object):
        self.__hospede = hospede
        self.__quarto = quarto

    def __str__(self):
        return f"Reserva do {self.__quarto} por {self.__hospede}"