class Quarto():
    def __init__(self, numero:int, tipo:str, disponivel:bool = True):
        self.__numero = numero
        self.__tipo = tipo
        self.__disponivel = disponivel

    def reservar(self):
        pass

    def liberar(self):
        pass

    def esta_disponivel(self):
        return self.__disponivel