class Quarto:
    def __init__(self, numero: int, tipo: str):
        self.__numero = numero
        self.__tipo = tipo
        self.__disponivel = True

    def reservar(self):
        if self.__disponivel == False:
            print("Este quarto já está reservado.")
        else:
            self.__disponivel = False
            print(f"Quarto {self.__numero} reservado com sucesso.")

    def liberar(self):
        pass

    def esta_disponivel(self):
        return self.__disponivel
    
    def __str__(self):
        return f"quarto {self.__numero}, {self.__tipo}"