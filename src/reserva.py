class Reserva:
    def __init__(self, hospede, quarto):
        self.__hospede = hospede
        self.__quarto = quarto

    def __str__(self):
        f"reserva quarto: {self.__quarto}, hóspede: {self.__hospede}"