class Quarto():
    def __init__(self, numero:int, tipo:str):
        self.__numero = numero
        self.__tipo = tipo
        self.__disponivel = True

    def reservar(self):
        pass

    def liberar(self):
        pass

    def esta_disponivel(self):
        return self.__disponivel
    
    def get_numero(self):
        return self.__numero
    
    def __str__(self):
        return f"quarto {self.__numero} de {self.__tipo}"