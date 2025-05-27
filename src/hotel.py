class Hotel:
    def __init__(self):
        self.__quartos = []
        self.__hospedes = []
        self.__reservas = []

    def add_quarto(self, quarto):
        for quarto_existente in self.__quartos:
            if quarto.get_numero() == quarto_existente.get_numero():
                print("Este quarto já existe.")
            else:
                self.__quartos.append(quarto)
                print(f"Quarto {quarto.get_number()} adicionado com sucesso.")

    def remover_quarto(self, quarto):
        pass

    def registrar_hospede(self, hospede):
        self.__hospedes.append(hospede)

    def cancelar_reserva(self, reserva):
        pass
    
    def get_quartos(self):
        for quarto in self.__quartos:
            print(quarto)
    
    def get_hospedes(self):
        return self.__hospedes
    
    def get_reservas(self):
        return self.__reservas
    
    def add_hospede(self, hospede):
        self.__hospedes.append(hospede)

    def add_reserva(self, reserva):
        self.__reservas.append(reserva)