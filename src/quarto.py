class Quarto:
    def __init__(self, numero, tipo):
        self.__numero = numero
        self.__tipo = tipo
        self.__disponivel = True

    def reservar():
        pass

    def liberar():
        pass

    def esta_disponivel(self):
        return self.__disponivel
    
    def __str__(self):
        return f"quarto {self.__numero}, {self.__tipo}"