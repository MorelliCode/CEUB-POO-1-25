class Reserva:
    def __init__(self, hospede, quarto):
        self.__hospede = hospede
        self.__quarto = quarto

    def __str__(self):
        return f"reserva: {self.__quarto} - {self.__hospede}"